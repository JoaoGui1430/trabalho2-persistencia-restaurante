# Acompanhamento de F1 a F18

Situação após as etapas 1 a 3. Base configurada/modelo desenhado não significa
funcionalidade persistida. Nenhuma F está integralmente concluída neste momento.

| Item | Funcionalidade | Situação atual | Etapas de implementação/conferência |
|---|---|---|---|
| F1 | Cadastro das entidades | Pendente. | 6–9. |
| F2 | Listagem de registros | Pendente. | 7–11. |
| F3 | Consulta por identificador | Pendente. | 7–9 e 15. |
| F4 | Atualização de dados | Campos e permissões planejados; operações pendentes. | 6–9. |
| F5 | Exclusão ou desativação | Política definida; operações pendentes. | 7–9. |
| F6 | Relacionamentos 1:1, 1:N e N:N | Modelo e diagrama definidos; ORM e uso real pendentes. | 5, 8, 9 e 11. |
| F7 | CRUD Routers | APIRouter da rota inicial funciona; routers dos recursos pendentes. | 7–12. |
| F8 | Paginação no banco | Pendente. | 10. |
| F9 | Pelo menos três critérios de filtro | Planejados status, mesa_id e produto_id; consultas pendentes. | 10. |
| F10 | Três consultas relacionadas | Planejadas; consultas pendentes. | 11. |
| F11 | Duas consultas complexas | Planejados ranking de produtos e faturamento por período. | 12. |
| F12 | Estatísticas/agregações | Planejadas; endpoint pendente. | 12. |
| F13 | Pelo menos três regras de negócio | Regras e estados definidos; aplicação nos serviços pendente. | 7–9 e 15. |
| F14 | Migração Alembic de evolução | Alteração futura definida; Alembic ainda não configurado. | 5 e 13. |
| F15 | PostgreSQL e SQLite por configuração | Portabilidade considerada no desenho; conexões pendentes. | 4, 5, 13 e 15. |
| F16 | Povoamento inicial | Pendente. | 14. |
| F17 | Funcionalidade específica do restaurante | Fluxo deduzido e documentado; pedidos/cálculo persistidos pendentes. | 8, 9, 15 e 16. |
| F18 | Tratamento de erros | Configuração e handlers HTTP iniciais implementados; erros de banco/domínio pendentes. | 4–9 e 15. |

## Exigências complementares

- Cinco entidades principais: definidas no desenho, ainda sem tabelas.
- PKs, FKs, restrições e relacionamento associativo: definidos no desenho.
- Persistência após reiniciar: pendente da conexão e operações no banco.
- Dados para apresentação: pendentes; ao menos dez produtos e dados em todas as
  entidades principais, com situações suficientes para consultas e paginação.
- README: iniciado; instruções dos dois bancos/migrações/povoamento serão incluídas
  junto das implementações.
- Logging: implementado como apoio ao desenvolvimento; não é um F adicional.
- Git/GitHub: registro de evolução solicitado pelo aluno; não substitui os logs
  nem a demonstração funcional exigida pelo professor.
