import logging

from fastapi import APIRouter


router = APIRouter(tags=["Início"])
logger = logging.getLogger("restaurante_api")


@router.get("/")
def inicio():
    logger.info("CONSULTA_INICIO metodo=GET rota=/")
    return {"mensagem": "Sistema de restaurante em funcionamento"}
