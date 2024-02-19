import heapq
from concurrent.futures import (
    ThreadPoolExecutor,
)
from json import (
    JSONDecodeError,
)
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Optional,
    Tuple,
)

from django.db import (
    transaction,
)
from django.db.models import (
    QuerySet,
)
from uploader_client.adapters import (
    adapter,
)

from educommon import (
    logger,
)

from edu_rdm_integration.enums import (
    FileUploadStatusEnum,
)
from edu_rdm_integration.export_data.base.requests import (
    RegionalDataMartStatusRequest,
)
from edu_rdm_integration.models import (
    DataMartRequestStatus,
    ExportingDataSubStageUploaderClientLog,
    UploadStatusRequestLog,
)


if TYPE_CHECKING:
    from uploader_client.models import (
        Entry,
    )


class UploadStatusHelper:
    """Хелпер проверки статуса загрузки данных в витрину."""

    def __init__(self, in_progress_uploads: QuerySet) -> None:
        self._in_progress_uploads = in_progress_uploads

    def run(self, thread_count: int = 1) -> None:
        """Запускает проверки статусов."""
        if thread_count > 1:
            with ThreadPoolExecutor(max_workers=thread_count) as pool:
                pool.map(self._process_upload, self._in_progress_uploads)
        else:
            for upload in self._in_progress_uploads:
                self._process_upload(upload)

    @classmethod
    def send_upload_status_request(cls, request_id: str) -> Tuple[Optional[Dict[str, Any]], 'Entry']:
        """Формирует и отправляет запрос для получения статуса загрузки данных в витрину."""
        request = RegionalDataMartStatusRequest(
            request_id=request_id,
            method='GET',
            parameters={},
            headers={
                'Content-Type': 'application/json',
            },
        )

        result = adapter.send(request)

        response = None

        if result.error:
            logger.error(
                f'Ошибка при получении статуса загрузки данных в витрину. Идентификатор загрузки: {request_id}. '
                f'Ошибка: {result.error}, запрос: {result.log.request}, ответ: {result.log.response}',
            )
        else:
            logger.info(
                f'Получен ответ со статусом {result.response.status_code} и содержимым {result.response.text}. '
                f'Идентификатор загрузки: {request_id}',
            )
            try:
                response = result.response.json()
            except JSONDecodeError:
                logger.error(
                    f'Не удалось получить данные из ответа запроса статуса загрузки данных в витрину. '
                    f'Идентификатор загрузки: {request_id}, ответ: {result.response.text}',
                )

        return response, result.log

    @classmethod
    def update_upload_status(
        cls,
        upload: ExportingDataSubStageUploaderClientLog,
        response: Optional[Dict[str, Any]],
        log_entry: 'Entry',
    ) -> None:
        """Обновляет статус загрузки данных в витрину."""
        request_status = None

        if isinstance(response, dict):
            request_status = DataMartRequestStatus.get_values_to_enum_data().get(response.get('code'))

            if not request_status:
                logger.error(
                    'Не удалось определить статус загрузки данных в витрину. Идентификатор загрузки: '
                    f'{upload.request_id}, данные ответа: {response}',
                )

        with transaction.atomic():
            UploadStatusRequestLog.objects.create(
                upload=upload,
                entry=log_entry,
                request_status_id=getattr(request_status, 'key', None),
            )

            if request_status in {DataMartRequestStatus.FAILED_PROCESSING, DataMartRequestStatus.REQUEST_ID_NOT_FOUND}:
                upload.file_upload_status = FileUploadStatusEnum.ERROR

            elif request_status == DataMartRequestStatus.SUCCESSFULLY_PROCESSED:
                upload.file_upload_status = FileUploadStatusEnum.FINISHED

            if upload.file_upload_status != FileUploadStatusEnum.IN_PROGRESS:
                upload.save()

    def _process_upload(self, upload: ExportingDataSubStageUploaderClientLog) -> None:
        """Обрабатывает запись загрузки данных в витрину."""
        response, log_entry = self.send_upload_status_request(upload.request_id)
        self.update_upload_status(upload, response, log_entry)


class Graph:
    """Граф связей между моделями.

    Предназначен для поиска кратчайшей связи между моделями и дальнейшего построения lookup`а
    до необходимого поля модели с последующим использованием его в фильтре.
    Вершинами графа выступают наименования моделей. Ребро содержит наименования модели связанной
    с другой моделью и наименования поля, через которое осуществляется связь.
    Вместо наименования поля может быть наименование обратной связи между моделями,
    в случае если данная связь является связью OneToOne.
    """

    def __init__(self):
        self.vertices: Dict[str, Dict[str,  Optional[str]]] = {}
        """Словарь для хранения данных графа."""

    def add_vertex(self, vertex: str):
        """Добавление вершины."""
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, vertex1: str, vertex2: str, edge_name: str):
        """Добавление связи."""
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1][vertex2] = edge_name
            if vertex1 not in self.vertices[vertex2]:
                self.vertices[vertex2][vertex1] = None

    def remove_vertex(self, vertex: str):
        """Удаление вершины."""
        if vertex in self.vertices:
            del self.vertices[vertex]

            # Удаляем связанные с удаленной вершиной ребра
            for neighbour in self.vertices:
                if vertex in self.vertices[neighbour]:
                    self.vertices[neighbour].pop(vertex)

    def remove_edge(self, vertex1: str, vertex2: str):
        """Удаление связи."""
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].pop(vertex2, None)
            self.vertices[vertex2].pop(vertex1, None)

    def get_vertices(self) -> List[str]:
        """Получение списка всех вершин."""
        return list(self.vertices)

    def get_edges(self) -> List[Tuple[str, str, Optional[str]]]:
        """Получение всех связей."""
        edges = []

        for vertex, neighbors in self.vertices.items():
            for neighboring_vertex, edge_name in neighbors.items():
                edge = (vertex, neighboring_vertex, edge_name)
                edges.append(edge)

        return edges

    def __contains__(self, vertex: str) -> bool:
        return vertex in self.vertices

    def __iter__(self):
        return iter(self.vertices)

    def __getitem__(self, vertex: str):
        return self.vertices.get(vertex, {})

    def get_edges_between_vertices(
        self, from_vertex: str, to_vertex: str, required_edge_name: bool = True
    ) -> List[str]:
        """Получение списка наименований ребер между вершинами."""
        if from_vertex not in self.vertices and to_vertex not in self.vertices:
            return []

        path = []
        edge_weight = 1

        # Инициализация расстояния между вершинами
        distances = {vertex: float('inf') for vertex in self}
        distances[from_vertex] = 0

        priority_queue = [(0, from_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Если достигнута конечная вершина, заканчиваем цикл
            if current_vertex == to_vertex:
                break

            # Проверяем все смежные вершины и обновляем расстояния, если находим более короткий путь
            for neighbor, edge_name in self[current_vertex].items():
                distance = current_distance + edge_weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Восстанавливаем путь от конечной вершины к начальной
        current_vertex = to_vertex
        while current_vertex != from_vertex:
            previous_vertex = edge_name = None

            for neighbor in self[current_vertex]:
                if distances[current_vertex] == distances[neighbor] + 1:
                    for neighbor_vertex, edge_name in self[neighbor].items():
                        if neighbor_vertex == current_vertex:
                            break

                    previous_vertex = neighbor
                    break

            if required_edge_name and not edge_name:
                path = []
                break

            path.append(edge_name)
            current_vertex = previous_vertex

        # Инвертируем путь и возвращаем его
        path.reverse()

        return path
