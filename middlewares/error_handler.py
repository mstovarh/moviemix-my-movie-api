from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

#Creación de clase hija de BaseHTTPMiddlewarepara manejo de errores
class ErrorHandler(BaseHTTPMiddleware):
    #Inicializar el middleware con la aplicación FastAPI.
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    #Auditador de cada solicitud que pasa por medio del middleware para captura de errores
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)}) 