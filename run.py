from twisted.application import service
import logging
import pytz
import sys
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)
logging.basicConfig()
log = logging.getLogger('apscheduler')
log.setLevel(logging.INFO)
try:
    from rpc import DispatchService
    from aps import scheduler
    import config
except ImportError as error:
    print error
    sys.exit(1)

scheduler.configure(jobstores=config.jobstores,
                    executors=config.executors,
                    job_defaults=config.job_defaults,
                    timezone=pytz.timezone("Asia/Shanghai"))
scheduler.start()

application = service.Application("dispatch")
app = DispatchService(8080)
app.setServiceParent(application)
