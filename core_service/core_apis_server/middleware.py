from starlette.middleware.base import BaseHTTPMiddleware
import time

class LoggingMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        end = time.time()
        print(f"[CORE SERVICE] {request.method} {request.url} completed in {end - start:.4f} seconds")
        return response
