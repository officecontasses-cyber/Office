# Prompt para o Claude in Chrome — levantamento da API SIEG

Copie tudo abaixo da linha e cole na extensão, com você já logado em https://hub.sieg.com/.

---

Você está no meu Chrome, já logado no HüB SIEG (https://hub.sieg.com/). Sua tarefa é SOMENTE LEITURA: levantar como acessar o HüB SIEG via API para controlar certidões, débitos e parcelamentos de clientes. Não confirme nada de memória; tudo precisa vir do que você ler nas páginas.

## Regras de segurança (obrigatórias)
- Não clique em "Gerar nova chave API": isso invalida a chave atual e pode quebrar integrações em uso.
- Não crie, edite, exclua nem envie nada (cadastros, consultas de certidão, e-mails, uploads).
- Se encontrar a chave de API, NÃO a escreva por extenso na resposta. Informe apenas que existe, onde fica e mostre mascarada (ex.: `abcd…wxyz`).
- Se alguma página pedir senha, 2FA ou ação que altere dados, pare e me pergunte.
- Abra cada página em nova aba e feche as que não precisar mais.

## Roteiro de pesquisa
1. **Portal (hub.sieg.com):** navegue pelo menu e liste todas as seções relacionadas a certidões, débitos/pendências fiscais, parcelamentos e DAS. Para cada uma, anote: nome da tela, o que mostra, filtros disponíveis, colunas, opções de exportação (Excel/CSV/PDF) e se há agrupamento por cliente, responsável ou carteira.
2. **Chave de API:** abra *Minha Conta → Integrações API SIEG*. Anote: se há chave ativa, onde ela fica (sem copiá-la), se existe limite de requisições ou restrição por plano e qualquer link para documentação.
3. **Base de conhecimento:** abra https://sieg.movidesk.com/kb/pt-br e busque pela série de artigos "(API)" (numerados, ex.: "17. Status certificado (API)", "22. Cadastrar integração estadual (API)", "25. Habilitar integração estadual (API)"). Liste TODOS os artigos de API com número, título e URL. Busque também por: certidão, débitos, parcelamento, DAS, pendências, situação fiscal, consulta em massa, webhook.
4. **Para cada artigo de API relevante** (principalmente Status certificado e qualquer um sobre certidões, débitos, parcelamentos, clientes/CNPJs), extraia literalmente, sem parafrasear:
   - URL do endpoint e método HTTP;
   - como a chave é enviada (query string, header ou body) e o nome exato do parâmetro;
   - todos os parâmetros, com tipo, obrigatoriedade e valores aceitos;
   - exemplo de requisição completo;
   - exemplo de resposta completo e a descrição de cada campo (inclusive códigos de status, datas de validade, indicadores de positiva/negativa);
   - paginação, limites de uso e códigos de erro.
5. **Lacunas a responder explicitamente:**
   - Existe API para débitos e parcelamentos, ou só tela/relatório no portal?
   - Dá para listar os clientes (CNPJs) cadastrados na conta pela API, ou só consultar CNPJ a CNPJ?
   - Existe campo de responsável, carteira, grupo ou tag por cliente que permita filtrar a "carteira da Fernanda"? Onde ele é configurado no portal?
   - Quais certidões a API cobre (federal, estadual, FGTS, trabalhista, municipal) e para quais UFs/municípios?
   - A API retorna o arquivo da certidão (PDF/base64) ou só o status?

## Formato da entrega
Responda em Markdown com estas seções:
1. **Mapa do portal** (tabela: seção, função, exportação).
2. **Autenticação** (como enviar a chave, sem revelá-la).
3. **Endpoints** (um bloco por endpoint, com os dados do item 4 transcritos literalmente).
4. **Lacunas respondidas** (as cinco perguntas acima, cada uma marcada como CONFIRMADO com URL do artigo, ou NÃO ENCONTRADO).
5. **Links** de todas as páginas consultadas.

Se algo não estiver documentado, escreva "NÃO ENCONTRADO". Não deduza nem complete por analogia. Ao terminar, me peça para colar o resultado no Claude Code.
