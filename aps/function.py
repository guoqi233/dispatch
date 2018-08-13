from aps import scheduler
from aps.dl import changeJobProperties
import logging


def add_job(job_id, interval):
    logger = logging.getLogger('apscheduler.deadline')
    scheduler.add_job(changeJobProperties,
                      kwargs=dict(job_id=job_id),
                      trigger="interval",
                      minutes=interval,
                      replace_existing=True,
                      id=job_id)
    logger.info("Add job {0} interval {1}".format(job_id, interval))


def remove_job(job_id):
    scheduler.remove_job(job_id)
    pass
