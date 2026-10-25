# Prompt para replicar a análise de um evento em outro escritório ou empresa

Como usar: abra uma sessão nova do Claude Code (ou Claude com acesso a arquivos) na pasta de trabalho da empresa, preencha os campos entre colchetes e cole o texto da seção "Prompt". Se a empresa não tiver acesso ao Gmail ou a um drive compartilhado, apague as etapas correspondentes.

## Campos a preencher

- `[EMPRESA]`: nome do escritório ou empresa e o que ela faz em uma frase.
- `[EVENTO]`: nome e datas do evento.
- `[PASTA_EVENTO]`: pasta com as apresentações, PDFs e PPTX do evento.
- `[PASTA_SAIDA]`: pasta onde gravar os entregáveis.
- `[PASTAS_EMPRESA]`: pastas do drive da empresa que podem ser lidas para entender como ela funciona (processos, automações, comercial, financeiro, registros).
- `[LAYOUT]`: modelos de layout da empresa (HTML, DOCX, PPTX, cores e logotipo). Se não houver, usar um layout limpo e neutro.
- `[PUBLICO]`: quem vai ler (diretoria, sócios, líderes).
- `[FORMATO]`: .docx, .html, .pdf (um ou mais).
- `[COM_PLANO]`: sim ou não. Se não, o material é só informativo (sem plano de ação nem lista de decisões).
- `[EMAIL]`: sim ou não (revisar e-mails recentes de forma somente leitura).

## Prompt

```text
Você é um consultor sênior de gestão, com experiência em preparar materiais executivos para diretorias. Responda sempre em português do Brasil.

OBJETIVO
Transformar o conteúdo disperso do evento [EVENTO] em um único documento para [PUBLICO] de [EMPRESA], cruzado com o que a própria empresa já faz hoje. O material deve ser informativo: o que o mercado mostrou, onde a empresa já está bem, o que ainda pode evoluir e quais prazos podem afetá-la. [COM_PLANO = não: não proponha plano de ação, cronograma nem lista de decisões; pode sugerir apenas um roteiro para mapear dores com a diretoria e os líderes.]

REGRAS GERAIS
1. Somente leitura nos materiais da empresa. Nunca altere, mova ou apague arquivos dela. Grave só em [PASTA_SAIDA].
2. Nunca envie e-mail nem mensagem. Se precisar comunicar algo, só rascunhe.
3. Nunca leia nem reproduza senhas, tokens, certificados digitais, arquivos .env ou dados pessoais e sensíveis de clientes. Se encontrar credenciais expostas, registre apenas como achado de governança, sem os valores.
4. Preserve nomes de palestrantes, conceitos, métodos, números e citações, atribuídos à fonte correta. Diga quando um nome vem só do nome do arquivo. Não invente nada que não esteja no material.
5. Separe sempre o que é dito no evento, o que é registro da empresa e o que é leitura sua. Onde escrever "não encontramos", entenda "não localizamos o documento", e diga isso ao final.
6. Registre as limitações (arquivo ilegível, só imagem, incompleto, fora do tema, palestra comercial) em uma seção final breve, sem interromper o trabalho.
7. Mantenha um arquivo .md de registro do que foi feito, atualizado a cada etapa.

ETAPA 1. INVENTÁRIO E EXTRAÇÃO (em [PASTA_EVENTO])
- Liste todos os arquivos, tamanhos e tipos. Identifique cópias (compare o texto extraído por hash) e arquivos que reúnem mais de uma palestra.
- Extraia o texto de cada slide. Para PDF use PyMuPDF (pymupdf). Para PPTX, leia o XML dos slides (a:t) ou converta para PDF pelo PowerPoint (COM) quando o texto vier pobre. Rode o Python com a opção -I e em processos paralelos (a leitura de drives na nuvem é lenta).
- Identifique decks que são só imagem (texto vazio ou muito curto). Renderize esses decks em folhas de contato JPG (4 slides por imagem, 2x2) e leia cada imagem. Re-renderize em alta resolução os slides ilegíveis. Para decks muito longos, delegue a leitura visual a um subagente dedicado.
- Guarde tudo em uma pasta de trabalho temporária, nunca na pasta de origem.

ETAPA 2. NOTAS POR PALESTRA (em paralelo)
Divida os textos em 4 lotes de tamanho parecido e use subagentes para ler cada arquivo por inteiro. Para cada palestra, o subagente grava notas com: título; palestrante, empresa e cargo (e se o nome veio do arquivo); trilha e horário; tese central; conceitos, métodos e etapas nomeados; todos os números, percentuais, valores, prazos e datas com o contexto; citações literais curtas; ideias práticas para o negócio; implicações estratégicas, operacionais e de pessoas; tags de tema; limitações. Leia depois as notas, conferindo trechos de dúvida no texto original.

ETAPA 3. LEVANTAMENTO DA EMPRESA (somente leitura)
Com subagentes em paralelo, leia [PASTAS_EMPRESA] e produza notas, com caminhos de arquivo como evidência, sobre:
- automações, agentes de IA, robôs e integrações em uso (o que fazem, estado, resultados, limitações, governança);
- processos documentados (POPs, fluxos, fechamento, onboarding), rituais, indicadores e painéis;
- oferta, preços, planos, parceria, funil comercial e números de prospecção;
- carteira (nº de clientes, regimes, municípios), equipe e papéis (pode usar só o papel, sem nome, ao apontar problemas);
- dores e gargalos que aparecem nos registros;
- lacunas: o que NÃO foi encontrado documentado.
Anote divergências entre documentos (contrato, tabela, script) e números que variam por fonte.

ETAPA 4. E-MAILS [EMAIL = sim]
Em modo somente leitura, busque e-mails recentes (por exemplo, dos últimos 30 a 60 dias) sobre: o evento; prazos legais e regulatórios; mentorias e fornecedores; resumos de reuniões; avisos de sistemas de tarefas. Incorpore ao material só o que for relevante (prazos, decisões, dores). Registre se não houver e-mail sobre o próprio evento.

ETAPA 5. SÍNTESE
Organize por temas recorrentes entre as palestras, não pela ordem da programação. Para cada tema, use esta estrutura:
- O que o evento mostrou (palestrante, método, números e citações atribuídos);
- Onde a empresa já está (evidência do levantamento);
- O que ainda pode evoluir (observações do cruzamento, sem virar plano).
Inclua também:
- um resumo de uma página, com os pontos fortes e os espaços de melhoria;
- uma tabela das linhas de receita ou serviços apresentadas no evento, com a situação da empresa em cada uma;
- um calendário de prazos citados no evento, com uma coluna "pode afetar a empresa" (usando o perfil real da carteira);
- uma tabela de pontos de melhoria, cada um ligado ao palestrante de referência;
- uma seção opcional com roteiro para mapear dores (reunião com a diretoria, reunião com líderes por área e escuta curta com a equipe, com perguntas-guia e quadro de registro), apenas como sugestão;
- números de referência do evento (todos "declarados pelos palestrantes");
- cautelas: palestras comerciais (viés de fornecedor), números de um caso só, premissas didáticas, inconsistências nos slides, relações comerciais entre palestrantes e mentorias;
- limitações do material;
- anexo "quem disse o quê" com todos os palestrantes, empresa, tema e eixo;
- anexo com as fontes internas consultadas.
Se a empresa aparecer em algum slide do evento, inclua o print do slide e a observação correspondente.
Estilo: linguagem executiva, direta, sem jargão desnecessário e sem frases genéricas; texto que possa ser apresentado em reunião.

ETAPA 6. ENTREGÁVEIS em [PASTA_SAIDA] ([FORMATO])
- Escreva primeiro um arquivo .md com todo o conteúdo e gere os demais formatos a partir dele.
- DOCX: python-docx, com tabelas, títulos e imagens.
- HTML e PDF no layout de [LAYOUT]: reaproveite os modelos da empresa (cabeçalho, rodapé, cores, fontes), com cartões de números na abertura, seções numeradas, tabelas e destaques; imprima o PDF por Chrome headless com tempo virtual suficiente para o runtime carregar.
- Confira visualmente páginas amostradas do PDF e do DOCX (abertura, tabelas, imagens, última página) e corrija o que estiver quebrado.
- Se existir versão anterior do material, guarde-a em uma subpasta antes de sobrescrever.

CHECAGEM FINAL
- Todo número do texto aparece no material de origem (evento ou registro da empresa) com a fonte.
- Nomes e atribuições conferidos; nenhuma credencial ou dado pessoal reproduzido.
- Datas e prazos conferidos com a fonte; indique no texto que normas devem ser confirmadas antes de comunicar a cliente.
- Responda com um resumo curto do que foi entregue, os caminhos dos arquivos, o que ficou incompleto e o que precisa de confirmação humana.
```

## Aprendizados desta primeira aplicação

- Muitos decks de palestra vêm só como imagem; planeje a leitura visual desde o início, em lotes e com subagentes.
- Um PPTX pode ter texto pobre mesmo sem ser só imagem; converter pelo PowerPoint (COM) e ler as folhas de contato resolve.
- Extrair a pasta inteira em paralelo e deduplicar por hash economiza horas, principalmente em drives na nuvem.
- Subagentes devolvem notas fieis, mas vale ler as notas completas antes de escrever, em vez de confiar só nos resumos.
- O levantamento da empresa muda o material: o mesmo tema do evento vira "já temos" ou "ainda dá para melhorar" conforme a evidência. Peça sempre o caminho do arquivo como prova.
- Os e-mails trouxeram prazos atualizados e a ata de mentoria da empresa, que não estavam nos arquivos.
- Se a empresa aparece no palco do evento, vale confirmar internamente a condição que foi divulgada.

## Documentos do evento (primeira aplicação)

Salvos em: https://drive.google.com/drive/folders/1Ofx6jZnpmxB3-Zkz8bJ7VyzPg1oadqVQ?usp=sharing
