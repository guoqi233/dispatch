from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.twisted import TwistedExecutor


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': TwistedExecutor(),
}
job_defaults = {
    'coalesce': True,
    'max_instances': 1,
    'misfire_grace_time': 40,
}
