import asyncio
import functools
import logging
from concurrent.futures import ThreadPoolExecutor

from .file_logger import FileLogger
from .request_statistics import RequestStatisticsRecord

class MonitorDaemon:
    def __init__(self, queue):
        self.logger = logging.getLogger("sparse")
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.queue = queue
        self.file_logger = FileLogger()

    async def start(self):
        self.logger.debug("Monitor daemon listening to queue.")
        loop = asyncio.get_running_loop()
        while True:
            record = await self.queue.get()
            await loop.run_in_executor(self.executor, functools.partial(self.file_logger.log_record, record))
            self.queue.task_done()

