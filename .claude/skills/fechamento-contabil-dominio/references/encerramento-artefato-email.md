# Encerramento: alimentar o artefato Controle Contábil e e-mail ao revisor (Etapa 7)

## Artefato Controle Contábil

Artefato: https://claude.ai/artifact/JC1KXPzY6goap6Ci9PcEzN — coleção `fechamento`, um documento por
cliente e competência, id `{NNN}_{AAAA-MM}` (ex.: `238_2026-09`). Leia o documento antes de gravar e
grave com a versão lida (`if_version`), mudando **só** os campos abaixo — os demais (gatilho do fiscal,
leitura do Drive, lucros) são alimentados por outras rotinas.

| Campo | O que gravar |
|---|---|
| `docsSituacao` | Uma das opções da página: `Aguardando cliente`, `Cobrado do cliente`, `Recebido fora do Drive`, `Cliente sem movimento`, `Documentos completos` |
| `docsPendentes` | Lista curta do que falta do cliente (ex.: "extratos de aplicação jul/ago; contrato de mútuo") |
| `obsAnalista` | Resumo para o revisor, em até ~5 linhas: resultado do mês e acumulado, tributos (conferidos / liberados ao fiscal / avisados), achados principais, nº de pendências por responsável e o caminho do papel de trabalho |
| `liberadoRevisao` | `Sim` só quando as portas das etapas 1 a 6 passaram (ou o colaborador aceitou o que ficou aberto); senão `Não` |
| `dataLiberacao` | Data de hoje (`AAAA-MM-DD`) quando `liberadoRevisao` = `Sim` |
| `status` | `Liberado para revisão` com `liberadoRevisao` = `Sim`; senão `Em andamento`. Nunca grave `Aprovado` — é do revisor |
| `atualizadoEm` | Data de hoje (`AAAA-MM-DD`) em toda gravação — é o que ordena o bloco de avisos do topo |

**Bloco "Avisos do fechamento":** no topo do artefato, antes das abas, a página mostra duas listas, com
o botão **Abrir** em cada linha:
- **Liberados para revisão** — `liberadoRevisao` = `Sim` e ainda não aprovado (aviso ao revisor/contador);
- **Em andamento** — `status` = `Em andamento`, do mais recente para o mais antigo por `atualizadoEm`,
  com a marca "atualizado hoje".
Quando o revisor marca `Aprovado`, a linha sai do bloco e aparece em "Aprovados recentes".

**Quando gravar:** no fim da Etapa 1 (pacote conferido), ofereça marcar a competência como
`Em andamento`, com `docsSituacao`, `docsPendentes`, uma linha em `obsAnalista` e `atualizadoEm` — assim
o fechamento já aparece no topo do artefato. Na Etapa 7, grave o encerramento (campos acima). Sempre com
a autorização do colaborador.

Regras:
- **Mostre os campos ao colaborador e só grave depois que ele autorizar.** O artefato é compartilhado
  por link: o que você grava todo mundo vê.
- **Nunca grave** senha, CPF, código de acesso nem **nome de arquivo que contenha senha** (ex.: "Extrato
  inv senha …") — troque por "[senha omitida]". Isso vale para qualquer campo do artefato.
- Não apague nem reescreva `obsContador`, `dataRevisao` ou `status` = `Aprovado` gravados pelo revisor.
- Se a gravação falhar ou não for autorizada, passe ao colaborador o texto de cada campo para ele
  preencher na aba Fechamento.
- Modo teste: não grave `liberadoRevisao` = `Sim`; mostre o que seria gravado.

## E-mail ao revisor (modelo)

Para: {e-mail do Gian — o colaborador preenche; não invente}
Assunto: `Fechamento contábil {NNN} {NOME} — {MM/AAAA} — {liberado para revisão | em andamento}`

> Gian, o fechamento contábil do **{NNN} {NOME}** ({regime}) de **{MM/AAAA}** está {liberado para sua
> revisão | em andamento, com os pontos abaixo}.
>
> **Resultado:** {lucro/prejuízo} de R$ {mês} no mês e R$ {acumulado} no acumulado do ano.
> **Tributos:** {conferidos}; {liberados ao fiscal, com valor e vencimento}; {avisos ao fiscal}.
> **Achados principais:** {2 a 4 itens}.
> **Pendências:** cliente {n}, fiscal {n}, DP {n}, para você {n} — lista na aba `Pendências` do papel de
> trabalho.
> **Papel de trabalho:** `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}/CONCILIACAO {NNN} {MM-AAAA}.xlsx`
> **Artefato:** https://claude.ai/artifact/JC1KXPzY6goap6Ci9PcEzN (bloco "Liberados para revisão" no topo)

Valores que dependem de parâmetro legal ainda não confirmado no Lefisc vão marcados como preliminares
também no e-mail. Se o colaborador usa o Outlook web, a skill `resumo-rascunho-email-owa` cria o
rascunho; caso contrário, ele copia o texto.
