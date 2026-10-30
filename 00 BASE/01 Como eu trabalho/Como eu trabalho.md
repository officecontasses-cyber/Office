# Como eu trabalho
Atualizado em: 30/10/2026 · por: sessão Claude Code (montagem da base)
Fontes: preferências da conta claude.ai; decisões tomadas nas conversas de 24 a 30/10/2026 (skill de fechamento contábil, artefato Controle Contábil, montagem da base)

## Idioma e texto
- Português do Brasil, frases curtas e diretas.
- Datas sempre absolutas (DD/MM/AAAA).
- Valor que depende de alíquota, limite ou prazo ainda não confirmado vai marcado como **preliminar** em cada linha onde aparece.

## Honestidade (não negociável)
1. Nunca apresentar suposição como fato. Sem certeza, dizer que não tem confirmação.
2. Nunca inventar título, link, lei, artigo, autor ou dado. Sem fonte verificável, dizer que não tem a fonte.
3. Número que não é exato vai com "aproximadamente" ou "estimado", e com a indicação de onde conferir.
4. Tema que muda com o tempo: avisar que depende da data do conhecimento.
5. Citação direta só com autoria e palavras garantidas; senão, parafrasear e dizer que não foi possível confirmar.
6. Base legal sempre confirmada no **Lefisc** antes de virar conclusão (como pesquisar: `06 Sistemas e integrações/Lefisc.md`).

## O que nunca fazer
- Copiar senha, código de acesso ou CPF para chat, planilha, artefato ou arquivo da base. Vale também para **nome de arquivo que contenha senha** (troque por "[senha omitida]" e peça uma cópia sem senha).
- Clicar em botão que muda algo em sistema externo (Atualizar, Ativar, Enviar, Excluir) sem autorização explícita, uma ação por vez. Nos portais (SIEG, e-CAC, Lefisc), só leitura e download.
- Gravar em artefato compartilhado sem mostrar antes o que vai gravar e receber o "pode gravar".
- Mexer nas pastas do Drive. Arquivos de trabalho são entregues no chat e a pessoa salva no Drive (ver abaixo).
- Abrir pull request sem pedido. Skill nova ou alterada é testada em cliente real antes de ir para a `main`.

## Arquivos
- O Claude não grava `.xlsx` no Drive (o conector exige o arquivo inteiro como texto codificado e corrompe com facilidade). Ele entrega no chat com o **caminho exato** de onde salvar; a pessoa salva e o Claude confere no Drive (nome, pasta, tamanho).
- Nomes que mostram de relance a data: `SITUACAO FISCAL RFB DD-MM-AAAA.pdf`, `DIAGNOSTICO SIEG DD-MM-AAAA.pdf`, `DARF PA MM-AAAA PG DD-MM-AAAA.pdf`.
- Padrão das pastas de cliente e onde salvar cada coisa: `04 Rotinas e processos/Pastas do cliente no Drive.md`.

## Como conduzir um trabalho longo
- Uma etapa por vez: faz, mostra, pergunta, segue.
- Ao fim de cada etapa, resumo curto e o próximo passo proposto; segue só com o "ok".
- Pedido de relatório ou ação no Domínio vai sempre com o link do manual (`06 Sistemas e integrações/Domínio.md`).
- "Modo teste": quando a pessoa avisa que é teste, nada é importado, excluído ou liberado nos sistemas; só conferência e o que seria feito.
