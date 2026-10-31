import logging
import logging.config
from pathlib import Path

import yaml

from core.config import BASE_DIR, ErroConfiguracao


def configurar_logging(config, base_dir=BASE_DIR, caminho_config=None):
    caminho_config = Path(caminho_config) if caminho_config is not None else BASE_DIR / "logging.yaml"

    try:
        with caminho_config.open("r", encoding="utf-8") as arquivo:
            config_logging = yaml.safe_load(arquivo)
    except FileNotFoundError as erro:
        raise ErroConfiguracao(f"Arquivo de configuração de log não encontrado: {caminho_config}") from erro
    except (OSError, UnicodeDecodeError) as erro:
        raise ErroConfiguracao(f"Não foi possível ler a configuração de log: {caminho_config}") from erro
    except yaml.YAMLError as erro:
        raise ErroConfiguracao("O logging.yaml contém YAML inválido.") from erro

    arquivo_log = Path(base_dir) / config["logging"]["arquivo"]
    try:
        arquivo_log.parent.mkdir(parents=True, exist_ok=True)
        config_logging["handlers"]["file"]["filename"] = str(arquivo_log)
        config_logging["loggers"]["restaurante_api"]["level"] = config["logging"]["nivel"].strip().upper()
        logging.config.dictConfig(config_logging)
    except (TypeError, KeyError) as erro:
        raise ErroConfiguracao("O logging.yaml não tem a estrutura esperada de handlers e loggers.") from erro
    except (OSError, ValueError, AttributeError) as erro:
        raise ErroConfiguracao(f"Não foi possível configurar o log em {arquivo_log}.") from erro

    return logging.getLogger("restaurante_api")
