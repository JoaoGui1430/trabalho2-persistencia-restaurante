# Roteiro de orientação — Trabalho Prático 2

Tema 8 — Sistema de Restaurante.

Estado: etapas 1 a 3 implementadas/documentadas a pedido do aluno em 31/10/2026.
A aplicação está na raiz do repositório. API mínima, configuração e logging
estão implementados; regras e modelo relacional estão definidos. Banco, ORM,
migrações, CRUD e operações de pedidos seguem pendentes das etapas 4 a 16.
O acompanhamento atual de cada F está em `requisitos.md`, nesta pasta `docs/`.

## Fontes e método

- Enunciado geral: PDF de nove páginas fornecido pelo aluno, no Desktop.
- Tema: fotografia fornecida pelo aluno, intitulada “Tema 8 — Sistema de Restaurante”.
- Referência de estilo: projeto `Trabalho1_Persistencia/cofre_documentacao` e conversa anterior sobre sua implementação.

Seguiremos o método anterior: compreender a necessidade, deduzir dados e regras, escolher o arquivo responsável, escrever um trecho pequeno, explicar seu funcionamento e verificar o resultado antes de avançar. Os nomes em português, as funções diretas e a separação entre configuração, serviços e routers serão preservados quando adequados. O Trabalho 2 terá modelos ORM e schemas de entrada/saída separados. Em 31/10/2026, o aluno autorizou a implementação direta das três primeiras etapas e a criação do repositório GitHub.

As escolhas propostas neste roteiro não são novas exigências do professor. O roteiro não transfere automaticamente requisitos do Trabalho 1 para o Trabalho 2.

## Exigências gerais, fora da lista F1–F18

- Python e FastAPI, com API REST.
- SQLAlchemy ou SQLModel como ORM principal.
- PostgreSQL como banco principal e efetivamente utilizado no desenvolvimento.
- Execução também em SQLite, alterando a configuração da conexão, sem reescrever entidades, routers ou CRUD.
- Pelo menos cinco entidades principais coerentes com o domínio, com atributos, PKs, FKs e restrições de integridade.
- Relacionamentos 1:1, 1:N e N:N, efetivamente utilizados pela aplicação.
- Persistência real: dados continuam disponíveis após reiniciar a API.
- Organização clara das responsabilidades. A estrutura sugerida no PDF é uma referência, não um formato obrigatório.
- Dados previamente cadastrados para a apresentação.
- README suficiente para outra pessoa executar o projeto.
- Equipe capaz de explicar o código e as bibliotecas utilizadas.

O PDF deste trabalho não estabelece logging ou Git como requisitos específicos. Logging desde o início será uma escolha de organização e diagnóstico, semelhante ao trabalho anterior. O PDF também não exige uma interface gráfica. Prazo, plataforma e formato da entrega não aparecem no documento analisado.

## Matriz completa das funcionalidades obrigatórias

As rotas abaixo são propostas; o enunciado exige o comportamento, não estes endereços literais.

| Item | Exigência | Aplicação proposta ao restaurante | Etapas |
|---|---|---|---|
| F1 — Cadastro das entidades | Receber, validar e persistir dados; considerar campos obrigatórios, unicidade, relacionamentos e regras; retornar HTTP adequado. | Cadastrar categorias, produtos, mesas e garçons; abrir pedidos; adicionar itens; gerar fechamento pelo fluxo de finalização. | 6–9 |
| F2 — Listagem de registros | Buscar as entidades principais no banco por meio do ORM. | Listar categorias, produtos, mesas, garçons e pedidos, incluindo consultas aos itens e fechamentos quando pertinentes. | 7–11 |
| F3 — Consulta por identificador | Localizar um registro persistido e tratar inexistência. | Consultar os recursos por ID; consultar um pedido com seus itens; retornar 404 quando não encontrado. | 7–9 e 15 |
| F4 — Atualização de dados | Validar e persistir somente alterações permitidas, mantendo relacionamentos íntegros. | Atualizar cadastros e dados permitidos do pedido aberto; alterar quantidade apenas quando permitido; impedir mudanças financeiras no pedido finalizado. | 7–9 |
| F5 — Exclusão de registros | Oferecer exclusão ou desativação adequada ao domínio, considerando dependências. | Desativar cadastros com histórico, remover itens elegíveis e cancelar pedidos segundo as regras; impedir apagamento de histórico financeiro. | 7–9 |
| F6 — Relacionamentos entre entidades | Implementar e utilizar 1:1, 1:N e N:N no ORM. | Pedido–FechamentoConta; Categoria–Produto, Mesa–Pedido e Garçom–Pedido; Pedido–Produto por ItemPedido. | 3, 5, 8, 9 e 11 |
| F7 — CRUD Routers | Organizar recursos principais em APIRouter próprios. | Routers de categorias, produtos, mesas, garçons e pedidos; relatórios em router próprio. O main.py configura e reúne a aplicação. | Base em 1; recursos em 7–12 |
| F8 — Paginação e limitação de resultados | Paginar pelo menos uma listagem principal, limitando a consulta no banco. | Listagem de pedidos com offset e limit, validação dos limites e ordenação estável; opcionalmente metadados de total. | 10 |
| F9 — Filtragem de dados | Pelo menos três critérios: um geral e dois do domínio, aplicados na consulta ao banco. | Geral: status do pedido. Domínio: mesa_id e produto_id; adicionais: categoria_id, modalidade e período. No filtro por produto, evitar duplicar pedidos que tenham várias linhas do mesmo produto. | 10 |
| F10 — Consultas envolvendo relacionamentos | Pelo menos três consultas com duas ou mais entidades relacionadas, usando os relacionamentos. | Produtos de uma categoria; histórico de pedidos de uma mesa; itens de um pedido com informações dos produtos. | 11 |
| F11 — Consultas complexas | Pelo menos duas consultas elaboradas; busca por ID ou um atributo isolado não basta. | Ranking de produtos vendidos no período, somando quantidades de pedidos finalizados; faturamento diário no período, agrupando fechamentos válidos. | 12 |
| F12 — Estatísticas e agregações | Pelo menos um endpoint de agregação sobre dados persistidos, com estatística específica do tema. | GET /estatisticas com quantidade de pedidos por status, faturamento de contas finalizadas e ticket médio; agregações executadas no banco. | 12 |
| F13 — Regras de negócio | Pelo menos três regras relevantes, integradas às operações e demonstradas; validação automática de tipo não basta. | Disponibilidade, preço histórico, total calculado pelo servidor, bloqueio após finalização, ocupação de mesas e limites para alteração/cancelamento. | Planejamento em 2–3; implementação em 7–9 |
| F14 — Migrações com Alembic | Evoluir o esquema existente com pelo menos uma alteração estrutural posterior à definição inicial. | Criar versão inicial e, posteriormente, adicionar observacao a Pedido por nova migração, preservando registros existentes. Somente a migração inicial não encerra F14. | 5 e 13 |
| F15 — PostgreSQL ⇔ SQLite | Alternar a conexão por configuração e verificar o funcionamento nos dois bancos. | DATABASE_URL configura o backend; o módulo de banco cuida de detalhes específicos da conexão. Executar migrações, povoamento e verificações nos dois bancos. | 4, 5, 13 e 15 |
| F16 — Povoamento inicial do banco | Mecanismo para inserir dados iniciais respeitando a integridade. | Script de povoamento com todas as entidades, pelo menos dez produtos, pedidos variados e relacionamentos demonstráveis. | 14 |
| F17 — Funcionalidade específica do tema | Funcionalidade integrada à API, com dados persistidos, entidades e regras reais; documentada e demonstrada. | Registrar e atualizar pedidos de múltiplos itens, calcular total a partir das quantidades e preços aplicados e finalizar a conta preservando sua consistência. | 8, 9, 15 e 16 |
| F18 — Tratamento de erros | Tratar inexistência, ID inválido, duplicidade, FKs, associações inválidas, regras de negócio, exclusões inconsistentes, dados inválidos e falhas de conexão/persistência. | Respostas HTTP claras; 200/201 para sucesso, 400/404/409/422 conforme a situação e 500 para falha interna; rollback em falhas transacionais, sem expor mensagens internas do SGBD. | Desde 4; revisão em 15 |

## Dedução do modelo de dados

| Entidade | Origem na descrição | Responsabilidade |
|---|---|---|
| Categoria | Cardápio organizado por categorias. | Identificar entradas, pratos, bebidas e sobremesas. |
| Produto | Produtos com descrição, preço e disponibilidade. | Manter o cardápio atual e permitir indisponibilidade sem apagar histórico. |
| Mesa | Atendimento em mesas e acompanhamento da ocupação. | Identificar mesas, sua habilitação para atendimento e seus pedidos. |
| Garcom | Garçons registram pedidos. | Identificar o responsável pelo atendimento e consultar seus pedidos. |
| Pedido | Atendimento em mesa ou retirada; pedidos abertos, finalizados ou cancelados. | Agrupar o atendimento e controlar modalidade, datas, estado e vínculos. |
| ItemPedido | Vários produtos por pedido, quantidades e preços aplicados. | Associar pedido e produto, guardar quantidade, preço aplicado e estado de preparo. |
| FechamentoConta | Fechamento e consistência das informações financeiras. | Registrar data e total consolidado da conta finalizada. |

Categoria, Produto, Mesa, Garcom e Pedido formam as cinco entidades principais. ItemPedido é uma entidade associativa com dados próprios; FechamentoConta tem responsabilidade financeira concreta. Não dependemos de contar somente a tabela associativa para atingir o mínimo.

Relacionamentos propostos:

- Categoria 1:N Produto.
- Mesa 1:N Pedido ao longo do tempo. Um pedido de retirada não possui mesa. Um pedido de mesa deve possuir mesa válida.
- Garcom 1:N Pedido. A obrigatoriedade do responsável em cada modalidade será documentada na etapa de regras.
- Pedido N:N Produto por ItemPedido. O ORM deve mapear e utilizar a associação, que possui quantidade e preço próprios.
- Pedido 1:1 FechamentoConta, com pedido_id único na tabela de fechamento. Um pedido aberto/cancelado tem zero fechamentos; um finalizado possui exatamente um. Portanto, a associação é opcional enquanto o atendimento não foi finalizado.

PK, FK, UNIQUE, NOT NULL e CHECK serão usadas conforme cada regra. A unicidade do fechamento será garantida também pelo banco, e não apenas por uma consulta prévia na aplicação.

Não há exigência de cadastro nominal de clientes ou de pagamentos divididos no material recebido. Essas funções não são necessárias para a proposta inicial.

## Regras do tema e decisões a documentar

Exigências extraídas do tema:

1. Um pedido pode conter vários itens e várias unidades de um produto.
2. Há pedidos de mesa e pedidos de retirada.
3. Produtos podem ficar indisponíveis sem perder o histórico de vendas.
4. Itens podem ser acrescentados enquanto o pedido estiver aberto.
5. Alteração de quantidades e remoção dependem das regras de atendimento e preparo.
6. O total é calculado pelos itens registrados: soma de quantidade × preço aplicado.
7. Alterar o preço atual do produto não pode modificar indevidamente pedidos anteriores.
8. Após fechar a conta, as informações financeiras devem permanecer consistentes.
9. Não podem existir atendimentos simultâneos incompatíveis para uma mesma mesa.
10. Finalização do atendimento libera a mesa.
11. É necessário tratar cancelamento e tentativa de alteração de pedido finalizado.
12. A administração precisa consultar períodos, produtos mais vendidos, pedidos abertos e faturamento.

Decisões adotadas nas etapas 2 e 3 (detalhadas nos documentos da aplicação):

- Estados do pedido: ABERTO, FINALIZADO e CANCELADO. Não permitir reabertura no escopo inicial.
- Estados mínimos do item: PENDENTE, EM_PREPARO e PRONTO. Prever uma operação real para iniciar o preparo; não apenas declarar um campo sem utilizá-lo.
- Permitir alteração de quantidade e remoção somente enquanto o item estiver PENDENTE e o pedido estiver ABERTO.
- Permitir cancelamento do pedido aberto somente quando nenhum item tiver iniciado o preparo. O tema não fixa a política exata; esta é uma proposta de escopo, não uma regra atribuída ao professor.
- Impedir inclusão de produto indisponível e novas associações com cadastros desativados.
- Capturar o preço do produto ao adicionar cada item. Se o mesmo produto for acrescentado novamente após mudança de preço, preservar a linha anterior e registrar o novo preço em uma nova linha, sem reprecificar o que já foi registrado.
- Usar centavos inteiros para dinheiro, sem cálculos com float, e verificar o comportamento nos dois bancos durante a implementação da persistência.
- Calcular o total no servidor; não aceitar do cliente um total arbitrário ou preço de venda manipulado.
- Rejeitar fechamento sem itens. Criar fechamento e finalizar pedido na mesma transação.
- Manter histórico financeiro: produtos referenciados são desativados e pedidos históricos não são apagados fisicamente pela API.
- Proposta inicial de ocupação: uma mesa pode ter somente um pedido ABERTO por vez. Garantir proteção no banco/transação contra duas aberturas concorrentes e verificar nos dois bancos. Ao finalizar ou cancelar validamente, liberar a mesa na mesma transação.
- Faturamento considera apenas contas finalizadas. Pedidos abertos e cancelados ficam fora do total vendido.

## Sequência de execução

### Etapa 1 — Preparar a estrutura e a API mínima

Após a análise inicial do enunciado, criar main.py, routers/__init__.py, routers/inicio.py, requirements.txt e um README na raiz do repositório, seguindo a estrutura do trabalho anterior. Usar FastAPI e Uvicorn com versões verificadas no Python do aluno. Criar a rota inicial em APIRouter separado e incluí-lo no main.py. Arquivos criados pelo Codex conforme autorização posterior do aluno.

Concluída quando GET / e /docs funcionarem. Este passo prepara F7 e a documentação; não conclui os CRUD routers dos recursos nem os demais F's. Não implementa banco, cadastro ou regra de negócio.

### Etapa 2 — Definir regras e configurações iniciais

Organizar F1–F18 e o tema; separar exigências de escolhas; definir estados, cancelamento, preparo, preço histórico e política de ocupação. Preparar configuração externa e logging simples, semelhante ao projeto anterior. Logging é uma escolha de apoio, não uma exigência adicional do PDF. As dependências de banco e migração serão acrescentadas nas etapas que as utilizarem.

Concluída quando cada regra tiver uma operação e um exemplo verificável, e as configurações iniciais forem utilizadas pela API. Prepara F13, F17, F18 e a futura configuração de F15, sem considerar essas funcionalidades concluídas. A estrutura crescerá com core/, models/, schemas/, services/, alembic/ e scripts/ conforme o uso.

### Etapa 3 — Desenhar o modelo relacional

Detalhar as sete entidades, atributos, chaves, nulabilidade e restrições; representar os relacionamentos e justificar sua utilidade no restaurante. Decidir a representação de valores monetários e a garantia de ocupação de mesas.

Concluída quando o modelo representar todos os fluxos e os três tipos de relacionamento sem entidades artificiais.

### Etapa 4 — Configurar o acesso ao PostgreSQL e ao SQLite

Criar configuração DATABASE_URL, conexão e sessões; preparar rollback/encerramento da sessão e tratamento básico de falhas. Detalhes de backend ficam no módulo de banco. Configurar a aplicação e o Alembic para o mesmo banco selecionado. Garantir a aplicação das FKs no SQLite.

Concluída quando ambos os bancos puderem ser acessados alternando a configuração.

### Etapa 5 — Implementar os modelos ORM e a estrutura inicial

Criar classes, relacionamentos e restrições. Inicializar Alembic e aplicar uma versão inicial nos dois bancos. Não esconder alterações futuras com recriação automática das tabelas a cada inicialização.

Concluída quando o esquema inicial existir nos dois bancos, corresponder ao modelo e possuir histórico de versão.

### Etapa 6 — Criar os schemas Pydantic

Separar entrada de cadastro, entrada de atualização e saída. Proteger campos controlados pelo servidor, como total, preço capturado e estado final. Definir quais campos podem ser omitidos ou nulos.

Concluída quando dados válidos forem aceitos e entradas indevidas forem rejeitadas de forma clara.

### Etapa 7 — Implementar CRUD dos cadastros básicos

Implementar categorias, produtos, mesas e garçons, com APIRouter próprios. Tratar unicidade, associação com categoria existente, atualização, desativação e dependências históricas. Tratar erros junto de cada operação.

Concluída quando cadastrar, listar, consultar, atualizar e excluir/desativar esses recursos funcionar com persistência e sem comprometer relacionamentos.

### Etapa 8 — Implementar pedidos, itens e total

Abrir pedido de mesa ou retirada; validar mesa/responsável; adicionar produtos disponíveis; capturar preço; alterar/remover itens elegíveis; iniciar preparo; consultar pedido e calcular total. Operações envolvendo várias alterações devem ser atômicas.

Concluída quando um pedido puder reunir vários produtos, receber acréscimos e manter o preço dos itens anteriores após mudança no cardápio.

### Etapa 9 — Implementar fechamento, cancelamento e liberação de mesa

Finalizar com total calculado; criar o fechamento único; impedir novas alterações; cancelar conforme a política documentada; liberar a mesa sem perder histórico. Não oferecer edição ou exclusão genérica de fechamento que viole a regra financeira.

Concluída quando o fluxo completo funcionar e operações proibidas forem bloqueadas, inclusive tentativas de fechar duas vezes e abrir dois atendimentos incompatíveis na mesma mesa.

### Etapa 10 — Implementar filtros e paginação

Aplicar status, mesa_id e produto_id diretamente na consulta ORM; adicionar filtros úteis de categoria, modalidade e período. Paginar pelo menos pedidos com ordenação estável e limites válidos, sem carregar tudo e fatiar uma lista.

Concluída quando os filtros isolados/combinados e páginas sucessivas retornarem os registros corretos.

### Etapa 11 — Implementar três consultas relacionadas

Propostas: GET /categorias/{id}/produtos; GET /mesas/{id}/pedidos; GET /pedidos/{id}/itens com dados dos produtos. São três consultas diferentes que utilizam os relacionamentos do ORM.

Concluída quando todas recuperarem vínculos reais persistidos e tratarem inexistência adequadamente.

### Etapa 12 — Implementar consultas complexas e estatísticas

Criar pelo menos duas consultas: ranking de produtos vendidos no período e faturamento diário por período. Ranking soma quantidades de itens vinculados a pedidos finalizados; faturamento soma fechamentos sem multiplicar valores ao fazer JOIN com itens. Criar GET /estatisticas com faturamento, ticket médio e contagem por status. Definir data usada em cada relatório, limites do intervalo e critério para dias sem vendas.

Concluída quando os resultados conferirem com contas manuais sobre um conjunto conhecido e excluírem cancelamentos e pedidos abertos.

### Etapa 13 — Fazer uma evolução real com Alembic

Após o esquema inicial estar em uso e possuir registros, adicionar observacao a Pedido por uma segunda versão de migração. Conferir o script e aplicar ao banco existente, sem apagar ou recriar tudo. Verificar também a atualização no outro backend.

Concluída quando a versão nova estiver aplicada e os dados antigos permanecerem disponíveis. A versão inicial, sozinha, não atende integralmente F14.

### Etapa 14 — Preparar o povoamento e os dados de demonstração

Criar script reproduzível, sem apagar a base silenciosamente nem duplicar registros ao repetir a execução. Povoar todas as entidades principais; cadastrar pelo menos dez produtos; distribuir categorias; criar pedidos de mesa/retirada, abertos/finalizados/cancelados, com múltiplos itens e fechamentos válidos. Usar datas suficientes para relatórios e dados suficientes para mais de uma página.

Concluída quando o banco puder ser preparado pelo script respeitando regras e integridade e demonstrar todas as funções exigidas.

### Etapa 15 — Conferir erros e integração nos dois bancos

Revisar F18 e executar os fluxos em PostgreSQL e SQLite: migrações, povoamento, CRUD, vínculos, reinício, paginação, filtros, regras, relatórios e preservação de dados. Verificar duplicidade, FK inexistente, ID inválido, transação incompleta, pedido bloqueado e falha de conexão. Usar testes direcionados para regras financeiras, estados e operações atômicas, sem repetir verificações sem necessidade.

Concluída quando o mesmo código funcionar nos dois bancos e os erros não vazarem mensagens internas do SGBD.

### Etapa 16 — Finalizar README e preparar apresentação

Documentar execução do zero, variáveis, bancos, migrações e povoamento. Demonstrar cada F com dados reais. Preparar a equipe para explicar modelos, ORM, schemas, routers, transações, consultas e regras. Conferir prazo/plataforma/formato conforme orientação específica da disciplina, sem presumir que as regras de entrega do Trabalho 1 foram mantidas.

Concluída quando outra pessoa conseguir iniciar o sistema seguindo somente o README e houver uma demonstração para cada requisito.

## Conteúdo obrigatório do README

- Nome do projeto, integrantes, Tema 8 e objetivo.
- Tecnologias utilizadas.
- Entidades, relacionamentos e diagrama ou representação do modelo relacional.
- Instalação, criação/preparação do ambiente e dependências.
- Configuração de PostgreSQL, SQLite e DATABASE_URL.
- Execução das migrações, do povoamento e da aplicação.
- Endpoints principais e filtros disponíveis.
- Consultas específicas e complexas.
- Regras de negócio e decisões sobre preparo/cancelamento/fechamento.
- Descrição da funcionalidade específica do restaurante.

## Verificações essenciais para a apresentação

1. Mostrar registros em todas as entidades principais e dez ou mais produtos.
2. Mostrar os relacionamentos 1:1, 1:N e N:N em operações reais.
3. Criar um pedido com dois produtos e quantidades diferentes; conferir o total.
4. Alterar preço no cardápio e provar que o item já registrado mantém o preço aplicado.
5. Acrescentar um item e alterar/remover um item ainda pendente.
6. Iniciar preparo e provar que a remoção proibida é bloqueada.
7. Finalizar e mostrar que o pedido não pode ser modificado financeiramente.
8. Demonstrar cancelamento válido e inválido segundo a política escolhida.
9. Mostrar ocupação de mesa, rejeição de atendimento incompatível e liberação.
10. Consultar um pedido de retirada sem mesa.
11. Usar três filtros, combinar critérios e navegar entre páginas.
12. Executar as três consultas relacionadas, duas complexas e estatísticas.
13. Mostrar a evolução Alembic preservando registros existentes.
14. Reiniciar a API e comprovar persistência.
15. Demonstrar funcionamento em PostgreSQL e SQLite por mudança de configuração.

O roteiro contém o plano completo. Somente as etapas 1 a 3 foram realizadas neste
momento; as demais não devem ser apresentadas como funcionalidades já executadas.
