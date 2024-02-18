import celery
from celery.schedules import (
    crontab,
)
from django.conf import (
    settings,
)

from educommon.async_task.models import (
    AsyncTaskType,
)
from educommon.async_task.tasks import (
    PeriodicAsyncTask,
)

from edu_rdm_integration.collect_data.helpers import (
    set_failed_status_suspended_collecting_data_stages,
)
from edu_rdm_integration.consts import (
    TASK_QUEUE_NAME,
)
from edu_rdm_integration.enums import (
    FileUploadStatusEnum,
)
from edu_rdm_integration.export_data.helpers import (
    set_failed_status_suspended_exporting_data_stages,
)
from edu_rdm_integration.helpers import (
    UploadStatusHelper,
)
from edu_rdm_integration.models import (
    ExportingDataSubStageUploaderClientLog,
)


class RDMCheckUploadStatus(PeriodicAsyncTask):
    """Периодическая задача для сбора статусов по загрузке файла в витрину."""

    queue = TASK_QUEUE_NAME
    routing_key = TASK_QUEUE_NAME
    description = 'Сбор статусов загрузки данных в витрину "Региональная витрина данных"'
    task_type = AsyncTaskType.UNKNOWN
    run_every = crontab(
        minute=settings.RDM_UPLOAD_STATUS_TASK_MINUTE,
        hour=settings.RDM_UPLOAD_STATUS_TASK_HOUR,
        day_of_week=settings.RDM_UPLOAD_STATUS_TASK_DAY_OF_WEEK,
    )

    def process(self, *args, **kwargs):
        """Выполнение."""
        super().process(*args, **kwargs)

        # Получаем незавершенные загрузки данных в витрину
        in_progress_uploads = ExportingDataSubStageUploaderClientLog.objects.filter(
            file_upload_status=FileUploadStatusEnum.IN_PROGRESS,
            is_emulation=False,
        )

        UploadStatusHelper(in_progress_uploads).run()


class CheckSuspendedExportedStagePeriodicTask(PeriodicAsyncTask):
    """Периодическая задача поиска зависших этапов/подэтапов экспорта."""

    queue = TASK_QUEUE_NAME
    routing_key = TASK_QUEUE_NAME
    description = 'Поиск зависших этапов/подэтапов экспорта в "Региональная витрина данных"'
    task_type = AsyncTaskType.SYSTEM
    run_every = crontab(
        minute=settings.RDM_CHECK_SUSPEND_TASK_MINUTE,
        hour=settings.RDM_CHECK_SUSPEND_TASK_HOUR,
        day_of_week=settings.RDM_CHECK_SUSPEND_TASK_DAY_OF_WEEK,
    )

    def process(self, *args, **kwargs):
        """Выполнение задачи."""
        super().process(*args, **kwargs)

        change_status_collecting_result = set_failed_status_suspended_collecting_data_stages()
        change_status_exporting_result = set_failed_status_suspended_exporting_data_stages()

        task_result = {
            'Прервано сборок': (
                f'Этапов {change_status_collecting_result["change_stage_count"]}'
                f' и подэтапов {change_status_collecting_result["change_sub_stage_count"]}'
            ),
            'Прервано выгрузок': (
                f'Этапов {change_status_exporting_result["change_stage_count"]}'
                f' и подэтапов {change_status_exporting_result["change_sub_stage_count"]}'
            ),
        }

        self.set_progress(
            values=task_result
        )


celery_app = celery.app.app_or_default()
celery_app.register_task(RDMCheckUploadStatus)
celery_app.register_task(CheckSuspendedExportedStagePeriodicTask)
