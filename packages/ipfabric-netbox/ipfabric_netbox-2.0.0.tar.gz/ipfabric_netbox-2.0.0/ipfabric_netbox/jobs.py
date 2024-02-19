import logging
from datetime import timedelta

from core.choices import DataSourceStatusChoices
from core.choices import JobStatusChoices
from core.exceptions import SyncError
from core.models import Job
from rq.timeouts import JobTimeoutException
from utilities.utils import local_now

from .models import IPFabricBranch
from .models import IPFabricSource
from .models import IPFabricSync

logger = logging.getLogger(__name__)


def sync_ipfabricsource(job, *args, **kwargs):
    ipfsource = IPFabricSource.objects.get(pk=job.object_id)

    try:
        job.start()
        ipfsource.sync(job=job)
        job.terminate()
    except Exception as e:
        job.terminate(status=JobStatusChoices.STATUS_ERRORED)
        IPFabricSource.objects.filter(pk=ipfsource.pk).update(
            status=DataSourceStatusChoices.FAILED
        )
        if type(e) in (SyncError, JobTimeoutException):
            logging.error(e)
        else:
            raise e


def sync_ipfabric(job, *args, **kwargs):
    obj = IPFabricSync.objects.get(pk=job.object_id)

    try:
        job.start()
        obj.sync(job=job)
        job.terminate()
    except Exception as e:
        job.terminate(status=JobStatusChoices.STATUS_ERRORED)
        IPFabricSync.objects.filter(pk=obj.pk).update(
            status=DataSourceStatusChoices.FAILED
        )
        if type(e) in (SyncError, JobTimeoutException):
            logging.error(e)
        else:
            raise e
    finally:
        if obj.interval and not kwargs.get("adhoc"):
            new_scheduled_time = local_now() + timedelta(minutes=obj.interval)
            job = Job.enqueue(
                sync_ipfabric,
                name=f"{obj.name} - (scheduled)",
                instance=obj,
                user=obj.user,
                schedule_at=new_scheduled_time,
                interval=obj.interval,
            )


def merge_ipfabric_branch(job, *args, **kwargs):
    branch = IPFabricBranch.objects.get(pk=job.object_id)

    try:
        job.start()
        branch.sync_merge()
        job.terminate()
    except Exception as e:
        job.terminate(status=JobStatusChoices.STATUS_ERRORED)
        IPFabricSync.objects.filter(pk=branch.sync.pk).update(
            status=DataSourceStatusChoices.FAILED
        )
        if type(e) in (SyncError, JobTimeoutException):
            logging.error(e)
        else:
            raise e
