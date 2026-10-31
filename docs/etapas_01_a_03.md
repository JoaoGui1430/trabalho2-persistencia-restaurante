# Etapas 1 a 3 — o que foi feito e como entender

## Etapa 1 — Estrutura e API mínima

`main.py` cria FastAPI e inclui `routers/inicio.py`. A rota `GET /` devolve uma
mensagem JSON. FastAPI gera `/docs` e `/openapi.json`. As dependências estão fixadas
em `requirements.txt`; `__init__.py` identifica os pacotes Python.

O padrão é o mesmo que será aplicado aos recursos: o router define as operações
e o main reúne os routers. Este passo inicia F7, mas não implementa CRUD.

## Etapa 2 — Configuração, logs e regras

1. `core/config.py` localiza e lê `config.yaml` com `yaml.safe_load`.
2. `validar_configuracao` confere seções, textos obrigatórios e nível do log.
3. `lru_cache` evita reler o arquivo em cada chamada; alterações no YAML exigem reinício.
4. `core/logging_config.py` lê `logging.yaml` e prepara logger, console e arquivo
   rotativo UTF-8, usando nível/caminho definidos em `config.yaml`.
5. `main.py` usa nome/descrição/versão do YAML e registra início/fim pelo ciclo de vida.
6. Acesso à rota inicial e erros HTTP também são registrados.
7. `app/estados.py` reúne os enums de situação do pedido, modalidade e preparo.
8. `docs/regras_negocio.md` define decisões e exemplos de aceitação, incluindo preço
   histórico, alterações permitidas, cancelamento e ocupação das mesas.

O código usa funções diretas e nomes em português. Os enums limitam o vocabulário;
não aplicam sozinhos as transições ou as regras de negócio. Isso prepara F13 e F17.
Os handlers iniciais preparam parte de F18; falhas do banco serão tratadas depois.

## Etapa 3 — Modelo relacional

`docs/modelo_relacional.md` contém sete entidades, dicionário de dados, chaves,
restrições, diagrama Mermaid e justificativas dos relacionamentos. O GitHub pode
renderizar o diagrama diretamente no Markdown.

Decisões centrais:

- Guardar dinheiro em centavos inteiros.
- Guardar o preço aplicado no item, separado do preço atual do produto.
- Permitir várias linhas do mesmo produto no mesmo pedido.
- Calcular ocupação da mesa pelos pedidos ABERTOS.
- Proteger a ocupação com unicidade parcial no banco futuro.
- Usar fechamento único por pedido e operações transacionais.
- Manter as mesmas entidades ao alternar PostgreSQL e SQLite.

Isso conclui o desenho da etapa 3; os relacionamentos ORM de F6 ainda serão
implementados e utilizados nas etapas seguintes.

## Verificação das etapas

Execute os testes de configuração e logs com:

```powershell
python -m unittest discover -s tests -v
```

Inicie a API com `python -m uvicorn main:app --reload` e confira `/`, `/docs`,
`/openapi.json`, uma rota inexistente e o arquivo `storage/logs/sistema.log`.

Para conferir configuração externa, altere temporariamente `aplicacao.nome`,
reinicie, veja o novo título na documentação e restaure o valor original.

## Continuidade

Os arquivos ficam diretamente na raiz do repositório, como no trabalho anterior:
`main.py`, `config.yaml`, `logging.yaml`, `app/`, `core/`, `routers/`, `services/`,
`utils/` e `storage/`. Documentação e testes ficam em `docs/` e `tests/`.

Próximo passo: etapa 4, conexão/sessões e configuração dos bancos. O status de
cada F está em `requisitos.md`. Não apresentar documentação ou enums como se
fossem operações de pedidos já implementadas.
