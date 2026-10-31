import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

from core.config import ErroConfiguracao, carregar_configuracao
from core.logging_config import configurar_logging
from routers import inicio


try:
    config = carregar_configuracao()
    logger = configurar_logging(config)
except ErroConfiguracao as erro:
    print(f"ERRO DE CONFIGURAÇÃO: {erro}", file=sys.stderr)
    raise SystemExit(1) from erro


@asynccontextmanager
async def ciclo_vida(app):
    logger.info("INICIALIZACAO aplicacao=%s versao=%s", app.title, app.version)
    try:
        yield
    finally:
        logger.info("ENCERRAMENTO aplicacao=%s", app.title)


app = FastAPI(
    title=config["aplicacao"]["nome"],
    description=config["aplicacao"]["descricao"],
    version=config["aplicacao"]["versao"],
    lifespan=ciclo_vida,
)

app.include_router(inicio.router)


@app.exception_handler(HTTPException)
async def tratar_erro_http(request: Request, erro: HTTPException):
    logger.warning("ERRO_HTTP status=%s metodo=%s rota=%s", erro.status_code, request.method, request.url.path)
    return await http_exception_handler(request, erro)


@app.exception_handler(RequestValidationError)
async def tratar_dados_invalidos(request: Request, erro: RequestValidationError):
    campos = [".".join(str(parte) for parte in item["loc"]) for item in erro.errors()]
    logger.warning("DADOS_INVALIDOS metodo=%s rota=%s campos=%s", request.method, request.url.path, campos)
    return await request_validation_exception_handler(request, erro)


@app.exception_handler(Exception)
async def tratar_erro_inesperado(request: Request, erro: Exception):
    logger.exception("ERRO_INESPERADO metodo=%s rota=%s", request.method, request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Erro interno inesperado"})
