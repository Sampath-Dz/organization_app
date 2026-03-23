import logging
import time
from starlette.middleware.base import BaseHTTPMiddleware

LOG = logging.getLogger("core_service")

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        LOG.info("→ %s %s", request.method, request.url.path)
        response = await call_next(request)
        duration = (time.time() - start) * 1000
        LOG.info("← %s %s %s (%.2f ms)", request.method, request.url.path, response.status_code, duration)
        return response