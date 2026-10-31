# Sistema de Restaurante

Trabalho Prático 2 — Desenvolvimento de Software para Persistência.
Tema 8 — Sistema de Restaurante.

## Integrantes

- João Guilherme Gadelha Abreu de Souza.
- Demais integrantes: confirmar antes da entrega.

## Objetivo

Gerenciar o cardápio, as mesas e os pedidos de um restaurante por uma API REST,
calculando a conta a partir dos itens e preservando o histórico das vendas.

## Estado atual

Etapas 1, 2 e 3 realizadas: estrutura e API mínima; configuração, logs e definição
das regras; desenho do modelo relacional. A única operação funcional de domínio
exposta é a mensagem de início em `GET /`.

Os estados já estão definidos em Python, mas as regras de negócio ainda não são
executadas por serviços. Não existem conexão com banco, tabelas ORM, migrações,
cadastros, filtros, estatísticas ou povoamento. Eles pertencem às etapas seguintes.

## Tecnologias

- Python 3.14.3: ambiente local conferido.
- FastAPI 0.141.1: aplicação REST e documentação OpenAPI.
- Uvicorn 0.52.4: servidor ASGI.
- PyYAML 6.0.3: leitura da configuração externa.
- `logging`, `enum` e `unittest`: biblioteca padrão do Python.

SQLAlchemy, Alembic, PostgreSQL e SQLite fazem parte do planejamento; ainda não
foram integrados. As respectivas dependências serão adicionadas quando utilizadas.

## Preparar o ambiente

Abra um terminal na raiz deste repositório e confira `python --version`.
Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Opcionalmente, para isolar as dependências, crie um ambiente virtual e utilize o
Python dele nos comandos seguintes:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

Não é necessário alterar a política de execução do PowerShell, pois esses comandos
utilizam diretamente o executável do ambiente.

## Executar

Na raiz deste repositório, onde está `main.py`:

```powershell
python -m uvicorn main:app --reload
```

- Rota inicial: <http://127.0.0.1:8000/>.
- Documentação interativa: <http://127.0.0.1:8000/docs>.
- Esquema OpenAPI: <http://127.0.0.1:8000/openapi.json>.
- Encerrar: `Ctrl+C` no terminal do servidor.

Resposta de `GET /`:

```json
{"mensagem": "Sistema de restaurante em funcionamento"}
```

## Configuração e logs

`config.yaml` define nome, descrição e versão da aplicação, nível e caminho do log.
`logging.yaml` define formato, handlers de console/arquivo e rotação, seguindo a
mesma separação de responsabilidades do trabalho anterior.
O arquivo é localizado em relação ao diretório da aplicação. Reinicie o servidor
depois de alterar o YAML: a configuração é lida uma vez por processo.

Os níveis aceitos são DEBUG, INFO, WARNING, ERROR e CRITICAL. A aplicação utiliza
o nome, descrição e versão na documentação e aplica o nível ao logger
`restaurante_api`. Logs são gravados no console e em `storage/logs/sistema.log`,
com rotação de aproximadamente 1 MiB e até três cópias anteriores.

Para conferir o uso real da configuração, altere temporariamente o nome ou o nível,
reinicie e veja o título em `/docs` ou os eventos no arquivo. Restaure o valor depois.
Uma configuração ausente ou inválida impede a inicialização e produz uma mensagem
clara no terminal. Falha ao abrir o arquivo de log também é tratada.

Eventos atuais: inicialização, acesso à rota inicial, encerramento e erros HTTP.
Os handlers para dados inválidos e erros inesperados estão preparados para as
operações futuras. Isso ainda não conclui F18.

## Estrutura

```text
trabalho2-persistencia-restaurante/
├── main.py
├── config.yaml
├── logging.yaml
├── requirements.txt
├── README.md
├── app/
│   └── estados.py
├── core/
│   ├── config.py
│   └── logging_config.py
├── routers/
│   └── inicio.py
├── services/
│   └── __init__.py
├── utils/
│   └── __init__.py
├── storage/
│   └── logs/
├── docs/
│   ├── regras_negocio.md
│   ├── modelo_relacional.md
│   ├── requisitos.md
│   ├── etapas_01_a_03.md
│   └── roteiro_trabalho2.md
└── tests/
    └── test_configuracao.py
```

Os diretórios Python possuem `__init__.py`. A estrutura coloca o código diretamente
na raiz, como no repositório do trabalho anterior. `services/` e `utils/` estão
preparados para as próximas etapas e ainda não possuem funções implementadas.
Em `storage/`, apenas o marcador da pasta de logs é versionado; logs, bancos,
temporários e caches ficam fora do Git. Modelos ORM e schemas serão criados nas
etapas correspondentes.

## Regras e modelo

O modelo contém Categoria, Produto, Mesa, Garcom, Pedido, ItemPedido e FechamentoConta.
Categoria–Produto, Mesa–Pedido e Garcom–Pedido representam 1:N; Pedido–Produto é N:N
por ItemPedido; Pedido–FechamentoConta é 1:1, opcional enquanto não finalizado.

- [Regras e exemplos de aceitação](docs/regras_negocio.md).
- [Campos, restrições e diagrama relacional](docs/modelo_relacional.md).
- [Situação de F1 a F18](docs/requisitos.md).
- [Explicação das etapas realizadas](docs/etapas_01_a_03.md).
- [Roteiro completo das 16 etapas](docs/roteiro_trabalho2.md).

## Verificar

```powershell
python -m unittest discover -s tests -v
```

Com o servidor iniciado, acessar `/` deve retornar 200 e a mensagem de funcionamento;
`/docs` e `/openapi.json` devem abrir; uma rota inexistente deve retornar 404 e gerar
um evento WARNING. Esses resultados não comprovam persistência, que ainda é pendente.

## Próximos passos

A etapa 4 implementará conexão e sessões. A etapa 5 implementará modelos ORM e a
estrutura inicial com Alembic. A documentação de `DATABASE_URL`, PostgreSQL,
SQLite, migrações e povoamento será completada junto das implementações reais.
