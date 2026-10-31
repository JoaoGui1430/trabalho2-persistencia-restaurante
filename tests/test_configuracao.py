import logging
import tempfile
import unittest
from pathlib import Path

import yaml

from core.config import BASE_DIR, ErroConfiguracao, carregar_configuracao
from core.logging_config import configurar_logging


class TestConfiguracao(unittest.TestCase):
    def setUp(self):
        # Usa somente um diretório temporário dentro deste projeto.
        raiz = (BASE_DIR / "tmp" / "testes").resolve()
        raiz.mkdir(parents=True, exist_ok=True)
        temporario = tempfile.TemporaryDirectory(dir=raiz)
        self.pasta = Path(temporario.name).resolve()
        assert self.pasta.parent == raiz
        self.addCleanup(temporario.cleanup)
        self.addCleanup(self.fechar_logs)
        self.addCleanup(carregar_configuracao.cache_clear)
        self.caminho = self.pasta / "config.yaml"

    def fechar_logs(self):
        logger = logging.getLogger("restaurante_api")
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
            handler.close()

    def config_valida(self):
        return {
            "aplicacao": {"nome": "Restaurante de teste", "descricao": "API de teste", "versao": "0.1.0"},
            "logging": {"nivel": "INFO", "arquivo": "logs/teste.log"},
        }

    def gravar(self, config):
        self.caminho.write_text(yaml.safe_dump(config, allow_unicode=True), encoding="utf-8")
        carregar_configuracao.cache_clear()

    def test_carrega_arquivo_externo(self):
        config = self.config_valida()
        self.gravar(config)
        self.assertEqual(carregar_configuracao(self.caminho), config)

    def test_rejeita_arquivo_ausente_e_yaml_invalido(self):
        with self.assertRaises(ErroConfiguracao):
            carregar_configuracao(self.caminho)
        self.caminho.write_text("aplicacao: [", encoding="utf-8")
        with self.assertRaises(ErroConfiguracao):
            carregar_configuracao(self.caminho)

    def test_rejeita_campos_ausentes_vazios_e_nivel_invalido(self):
        casos = [None, [], {"aplicacao": []}]
        config = self.config_valida()
        config["aplicacao"]["nome"] = " "
        casos.append(config)
        config = self.config_valida()
        config["logging"]["nivel"] = "QUALQUER"
        casos.append(config)
        for config in casos:
            with self.subTest(config=config):
                self.gravar(config)
                with self.assertRaises(ErroConfiguracao):
                    carregar_configuracao(self.caminho)

    def test_logging_aplica_nivel_utf8_e_nao_duplica_mensagens(self):
        config = self.config_valida()
        config["logging"]["nivel"] = "WARNING"
        logger = configurar_logging(config, base_dir=self.pasta)
        logger.info("EVENTO_OCULTO")
        logger.warning("ATENÇÃO_TESTE")
        logger = configurar_logging(config, base_dir=self.pasta)
        logger.warning("EVENTO_UNICO")
        self.fechar_logs()
        conteudo = (self.pasta / "logs" / "teste.log").read_text(encoding="utf-8")
        self.assertNotIn("EVENTO_OCULTO", conteudo)
        self.assertIn("ATENÇÃO_TESTE", conteudo)
        self.assertEqual(conteudo.count("EVENTO_UNICO"), 1)

    def test_rejeita_configuracao_logging_ausente_ou_yaml_invalido(self):
        caminho_logging = self.pasta / "logging.yaml"
        with self.assertRaises(ErroConfiguracao):
            configurar_logging(self.config_valida(), base_dir=self.pasta, caminho_config=caminho_logging)
        caminho_logging.write_text("handlers: [", encoding="utf-8")
        with self.assertRaises(ErroConfiguracao):
            configurar_logging(self.config_valida(), base_dir=self.pasta, caminho_config=caminho_logging)


if __name__ == "__main__":
    unittest.main()
