from functools import lru_cache
from pathlib import Path

import yaml


BASE_DIR = Path(__file__).resolve().parent.parent
NIVEIS_LOG = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


class ErroConfiguracao(Exception):
    """Configuração ausente, ilegível ou com valores inválidos."""


def validar_configuracao(config):
    if not isinstance(config, dict):
        raise ErroConfiguracao("O config.yaml deve conter seções e valores.")

    problemas = []
    campos = {
        "aplicacao": ("nome", "descricao", "versao"),
        "logging": ("nivel", "arquivo"),
    }

    for secao, chaves in campos.items():
        valores = config.get(secao)
        if not isinstance(valores, dict):
            problemas.append(f"A seção '{secao}' deve conter chaves e valores.")
            continue
        for chave in chaves:
            valor = valores.get(chave)
            if not isinstance(valor, str) or not valor.strip():
                problemas.append(f"'{secao}.{chave}' deve ser um texto não vazio.")

    logging_config = config.get("logging")
    if isinstance(logging_config, dict):
        nivel = logging_config.get("nivel")
        if isinstance(nivel, str) and nivel.strip():
            if nivel.strip().upper() not in NIVEIS_LOG:
                problemas.append("'logging.nivel' deve ser DEBUG, INFO, WARNING, ERROR ou CRITICAL.")

    if problemas:
        raise ErroConfiguracao("Configuração inválida:\n- " + "\n- ".join(problemas))


@lru_cache
def carregar_configuracao(caminho=None):
    caminho = Path(caminho) if caminho is not None else BASE_DIR / "config.yaml"
    try:
        with caminho.open("r", encoding="utf-8") as arquivo:
            config = yaml.safe_load(arquivo)
    except FileNotFoundError as erro:
        raise ErroConfiguracao(f"Arquivo de configuração não encontrado: {caminho}") from erro
    except (OSError, UnicodeDecodeError) as erro:
        raise ErroConfiguracao(f"Não foi possível ler a configuração: {caminho}") from erro
    except yaml.YAMLError as erro:
        raise ErroConfiguracao("O config.yaml contém YAML inválido.") from erro

    validar_configuracao(config)
    return config
