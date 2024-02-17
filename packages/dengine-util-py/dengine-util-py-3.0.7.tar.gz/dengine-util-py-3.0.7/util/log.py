import logging
import re
import os
import time
from safe_logger import TimedRotatingFileHandlerSafe

from util.path import get_project_dir

# 设置日志文件的最大大小（可选）
max_file = 1024 * 1024 * 1024 * 1
# 最大备份小时
backup_count = 24 * 30

ext_match = r"^\d{10}$"
suffix = '%Y%m%d%H'

LOG_FILE = get_project_dir() + "/log/public.log"
log_handler = TimedRotatingFileHandlerSafe(LOG_FILE, when='H', interval=1,
                                            backupCount=backup_count, utc=True)
hander.suffix = suffix
hander.extMatch = re.compile(ext_match, re.ASCII)


logging.basicConfig(
    level=logging.INFO,
    format="%(logTag)s||timestamp=%(asctime)s||%(message)s",
    handlers=[
        hander
    ],
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger(__name__)
