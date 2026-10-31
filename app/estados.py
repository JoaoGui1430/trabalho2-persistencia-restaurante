"""Vocabulário do restaurante; as validações das operações serão implementadas nos serviços."""

from enum import Enum


class SituacaoPedido(str, Enum):
    ABERTO = "ABERTO"
    FINALIZADO = "FINALIZADO"
    CANCELADO = "CANCELADO"


class ModalidadePedido(str, Enum):
    MESA = "MESA"
    RETIRADA = "RETIRADA"


class SituacaoItem(str, Enum):
    PENDENTE = "PENDENTE"
    EM_PREPARO = "EM_PREPARO"
    PRONTO = "PRONTO"
