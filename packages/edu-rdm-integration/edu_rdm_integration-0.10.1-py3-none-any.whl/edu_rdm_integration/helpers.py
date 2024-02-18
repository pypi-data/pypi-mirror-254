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
