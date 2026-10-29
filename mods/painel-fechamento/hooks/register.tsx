import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

const PANE = 'fechamento'

const pulados = atom({ plugin: 'painel-fechamento', key: 'pulados' } as const, [] as string[], {
  shape: 'pulados-1',
})
const rascunho = atom({ plugin: 'painel-fechamento', key: 'rascunho' } as const, '', {
  shape: 'rascunho-1',
})

type Acao = { rotulo: string; texto: string }
type Item = {
  id: string
  cabecalho: string
  obrigacao: string
  contexto: string
  escrever: string
  acoes: Acao[]
}
type Grupo = { titulo: string; nota?: string; cor?: string; itens: Item[] }

// Lido da aba Set2026 da Controle_Fiscal em 29/10/2026.
const GRUPOS: Grupo[] = [
  {
    titulo: 'Vencido',
    nota: 'pós-fechamento',
    cor: 'red',
    itens: [
      {
        id: '197-pis-cofins',
        cabecalho: '#197 · ASBBM',
        obrigacao: 'DARF PIS e COFINS 09/2026',
        contexto: 'Venceu 23/10, em andamento. Se for isenta, as duas linhas viram Não se aplica.',
        escrever: '#197 DARF PIS e COFINS de 09/2026: ',
        acoes: [{ rotulo: 'Resolver agora', texto: '#197 vamos resolver as DARFs de PIS e COFINS de 09/2026' }],
      },
    ],
  },
  {
    titulo: 'Depende de decisão sua',
    cor: 'yellow',
    itens: [
      {
        id: '197-csll',
        cabecalho: '#197 · ASBBM',
        obrigacao: 'CSLL 3º trimestre · R$ 95,64 · vence 30/10',
        contexto: 'Só se ficar em Lucro Presumido. A resposta do Gian era para hoje.',
        escrever: '#197 enquadramento: ',
        acoes: [
          { rotulo: 'Seguir com Lucro Presumido', texto: '#197 vamos seguir com o Lucro Presumido e gerar a CSLL de 95,64' },
          { rotulo: 'Cobrar o Gian', texto: '#197 rascunha a cobrança ao Gian sobre o enquadramento, resposta hoje' },
        ],
      },
    ],
  },
  {
    titulo: 'Amanhã, 30/10',
    nota: 'IRPJ e CSLL do 3º trimestre',
    cor: 'yellow',
    itens: [
      {
        id: '247',
        cabecalho: '#247 · Porto Mais Alegre',
        obrigacao: 'IRPJ R$ 807,13 e CSLL R$ 3.502,24',
        contexto: 'Só falta trabalho nosso: lançar o rendimento 513,80 e o IRRF 115,61 no Domínio e gerar as guias.',
        escrever: '#247 IRPJ/CSLL do 3º trimestre: ',
        acoes: [{ rotulo: 'Fechar as guias', texto: '#247 vamos fechar as guias de IRPJ 807,13 e CSLL 3.502,24 do 3º trimestre' }],
      },
      {
        id: '71',
        cabecalho: '#71 · Conte Arquitetura',
        obrigacao: 'IRPJ R$ 104.929,65 e CSLL R$ 69.457,20',
        contexto: 'Falta o informe de rendimentos do Bradesco.',
        escrever: '#71 IRPJ/CSLL do 3º trimestre: ',
        acoes: [
          { rotulo: 'Fechar as guias', texto: '#71 vamos fechar o IRPJ e a CSLL do 3º trimestre' },
          { rotulo: 'Cobrar o informe', texto: '#71 rascunha a cobrança do informe de rendimentos do Bradesco, prazo amanhã' },
        ],
      },
      {
        id: '186',
        cabecalho: '#186 · Lopes & Nadal',
        obrigacao: 'IRPJ e CSLL, sem valor',
        contexto: 'Falta o comprovante do resgate do fundo de 31/07, cerca de 650,00.',
        escrever: '#186 IRPJ/CSLL do 3º trimestre: ',
        acoes: [
          { rotulo: 'Fechar as guias', texto: '#186 vamos fechar o IRPJ e a CSLL do 3º trimestre' },
          { rotulo: 'Cobrar o resgate', texto: '#186 rascunha a cobrança do comprovante do resgate do fundo de 31/07' },
        ],
      },
      {
        id: '133',
        cabecalho: '#133 · RFL',
        obrigacao: 'IRPJ e CSLL de setembro, sem valor',
        contexto: 'Lucro Real: depende do balancete da contabilidade.',
        escrever: '#133 IRPJ/CSLL de setembro: ',
        acoes: [{ rotulo: 'Fechar as guias', texto: '#133 vamos fechar o IRPJ e a CSLL de setembro (Lucro Real)' }],
      },
      {
        id: '238-darfs',
        cabecalho: '#238 · REAT Holding',
        obrigacao: 'DARFs de abril, maio e junho · R$ 9.405,48',
        contexto: 'Com multa e juros; pagamento não confirmado.',
        escrever: '#238 DARFs de abril, maio e junho: ',
        acoes: [{ rotulo: 'Resolver as DARFs', texto: '#238 vamos resolver as DARFs de abril, maio e junho (9.405,48)' }],
      },
      {
        id: '238-diario',
        cabecalho: '#238 · REAT Holding',
        obrigacao: 'Balancete de setembro no Livro Diário',
        contexto: 'É o que sustenta o balanço de redução.',
        escrever: '#238 transcrição do balancete no Diário: ',
        acoes: [{ rotulo: 'Tratar a transcrição', texto: '#238 vamos tratar da transcrição do balancete de setembro no Diário' }],
      },
      {
        id: '238-relatorio',
        cabecalho: '#238 · REAT Holding',
        obrigacao: 'Relatório de débitos à cliente',
        contexto: 'Relatório de 06/2026 mais o IRPJ e a CSLL vencidos. Era para a 2ª quinzena de outubro.',
        escrever: '#238 relatório de débitos: ',
        acoes: [{ rotulo: 'Montar o relatório', texto: '#238 vamos montar o relatório de débitos de 06/2026 para enviar à cliente' }],
      },
    ],
  },
  {
    titulo: 'Novembro',
    itens: [
      {
        id: '261-nf',
        cabecalho: '#261 · Giatech',
        obrigacao: 'NFS-e de outubro para a Betha · vence 09/11',
        contexto: 'Falta a Jani passar o valor. Valor cheio, com CSLL 1% retida e abatimento de 340,00 nas informações complementares.',
        escrever: '#261 nota de outubro, valor do serviço: ',
        acoes: [
          { rotulo: 'Calcular as retenções', texto: '#261 chegou o valor da nota de outubro: vamos calcular as retenções e o líquido' },
          { rotulo: 'Cobrar a Jani', texto: '#261 rascunha a cobrança do valor da nota de outubro para a Jani' },
        ],
      },
      {
        id: 'sped',
        cabecalho: 'Todos os clientes',
        obrigacao: 'SPED Contribuições 09/2026 · 16/11',
        contexto: 'Pendente em 25 linhas. É o maior bloco que resta do fechamento.',
        escrever: 'SPED Contribuições de 09/2026: ',
        acoes: [{ rotulo: 'Organizar a rodada', texto: 'Vamos organizar o SPED Contribuições de 09/2026: ordem e o que falta em cada cliente' }],
      },
    ],
  },
  {
    titulo: 'Sem prazo legal',
    nota: 'conciliação do Domínio',
    itens: [
      {
        id: '261-tomados',
        cabecalho: '#261 · Giatech',
        obrigacao: 'Serviços tomados · R$ 1.058,95',
        contexto: 'Em andamento: o protocolo de Novo Hamburgo precisa ser refeito. Nada muda em guia.',
        escrever: '#261 serviços tomados: ',
        acoes: [{ rotulo: 'Refazer o protocolo', texto: '#261 vamos refazer o protocolo de serviços tomados de Novo Hamburgo (1.058,95)' }],
      },
      {
        id: '238-dominio',
        cabecalho: '#238 · REAT Holding',
        obrigacao: 'Entradas e Serviços prestados',
        contexto: 'As duas linhas pendentes, sem valor.',
        escrever: '#238 conciliação do Domínio: ',
        acoes: [{ rotulo: 'Conciliar', texto: '#238 vamos conciliar Entradas e Serviços prestados de setembro no Domínio' }],
      },
      {
        id: '126',
        cabecalho: '#126 · Tatsch & Leite',
        obrigacao: 'Serviços tomados · R$ 13.539,36',
        contexto: 'Guia e declaração de São Leopoldo já enviadas.',
        escrever: '#126 serviços tomados: ',
        acoes: [{ rotulo: 'Conciliar', texto: '#126 vamos conciliar os serviços tomados de setembro' }],
      },
      {
        id: '264',
        cabecalho: '#264 · Zenith Paracuru',
        obrigacao: 'Serviços tomados · R$ 9.074,70',
        contexto: 'O resto do cliente está sem movimento.',
        escrever: '#264 serviços tomados: ',
        acoes: [{ rotulo: 'Conciliar', texto: '#264 vamos conciliar os serviços tomados de setembro' }],
      },
      {
        id: '152',
        cabecalho: '#152 · CRBM5',
        obrigacao: 'Entradas · R$ 39.205,71',
        contexto: 'As guias de ISSQN, inclusive a de fora do município, já foram enviadas.',
        escrever: '#152 Entradas: ',
        acoes: [{ rotulo: 'Conciliar', texto: '#152 vamos conciliar as Entradas de setembro (39.205,71)' }],
      },
      {
        id: '248',
        cabecalho: '#248 · Tacom Projetos SC',
        obrigacao: 'Entradas R$ 15,00 e guia de ICMS',
        contexto: 'O SPED ICMS já foi enviado.',
        escrever: '#248 Entradas e guia de ICMS: ',
        acoes: [{ rotulo: 'Resolver', texto: '#248 vamos resolver as Entradas e a guia de ICMS de setembro' }],
      },
      {
        id: '258',
        cabecalho: '#258 · Nadal Participações',
        obrigacao: 'Serviços tomados e prestados',
        contexto: 'As duas linhas pendentes. As DARFs estão sem movimento.',
        escrever: '#258 serviços tomados e prestados: ',
        acoes: [{ rotulo: 'Conciliar', texto: '#258 vamos conciliar os serviços tomados e prestados de setembro' }],
      },
      {
        id: '263',
        cabecalho: '#263 · Tacom Projetos RS',
        obrigacao: 'Serviços tomados e prestados',
        contexto: 'A guia de ISSQN de 4.089,69 já foi enviada.',
        escrever: '#263 serviços tomados e prestados: ',
        acoes: [{ rotulo: 'Conciliar', texto: '#263 vamos conciliar os serviços tomados e prestados de setembro' }],
      },
      {
        id: '177',
        cabecalho: '#177 · ILS Consultoria',
        obrigacao: 'Serviços tomados',
        contexto: 'Em andamento, sem valor. O resto do cliente está fechado.',
        escrever: '#177 serviços tomados: ',
        acoes: [{ rotulo: 'Conciliar', texto: '#177 vamos conciliar os serviços tomados de setembro' }],
      },
    ],
  },
]

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({
      name: 'fechamento',
      description: 'Abrir o painel das pendências do fechamento',
    })
    void $.ui.open({ id: PANE, title: 'Fechamento 09/2026' })

    return next(e)
  })

  on('command.run', { command: 'fechamento' }, async $ => {
    await $.ui.open({ id: PANE, title: 'Fechamento 09/2026' })

    return { text: 'Painel do fechamento aberto.' }
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const elementos = $.ui.resolve(e) as Record<string, any>
    const { Box, Text, Button } = elementos
    const Input = elementos.Input
    const escondidos = await read($, pulados)
    const texto = await read($, rascunho)

    const visiveis = (grupo: Grupo) => grupo.itens.filter(item => !escondidos.includes(item.id))
    const grupos = GRUPOS.filter(grupo => visiveis(grupo).length > 0)
    const total = grupos.reduce((soma, grupo) => soma + visiveis(grupo).length, 0)

    const enviar = (valor: string) => {
      const limpo = valor.trim()
      if (!limpo) return
      void update($, rascunho, () => '')
      void $.prompt.submit({ text: limpo })
    }

    return (
      <Box flexDirection="column" rowGap={1}>
        {Input ? (
          <Box flexDirection="column" borderStyle="round" paddingX={1}>
            <Input
              key="comando"
              label="Comando livre"
              placeholder="#247: gera a guia e me manda o rascunho"
              value={texto}
              rows={2}
              submitLabel="enviar"
              onInput={(valor: string) => {
                void update($, rascunho, () => valor)
              }}
              onSubmit={(valor: string) => {
                enviar(valor)
              }}
            />
            <Box columnGap={1}>
              <Button key="enviar" onPress={() => enviar(texto)}>
                Enviar
              </Button>
              <Button
                key="limpar"
                onPress={() => {
                  void update($, rascunho, () => '')
                }}
              >
                Limpar
              </Button>
            </Box>
          </Box>
        ) : null}

        <Text dimColor>
          {total} pendências · lido da Set2026 em 29/10
        </Text>

        {grupos.map(grupo => (
          <Box flexDirection="column" rowGap={1}>
            <Text color={grupo.cor} weight="bold">
              {grupo.titulo}
              {grupo.nota ? ` · ${grupo.nota}` : ''}
            </Text>
            {visiveis(grupo).map(item => (
              <Box flexDirection="column" borderStyle="round" paddingX={1}>
                <Text weight="bold">{item.cabecalho}</Text>
                <Text>{item.obrigacao}</Text>
                <Text dimColor>{item.contexto}</Text>
                <Box columnGap={1}>
                  {item.acoes.map(acao => (
                    <Button key={`${item.id}-${acao.rotulo}`} onPress={() => enviar(acao.texto)}>
                      {acao.rotulo}
                    </Button>
                  ))}
                  <Button
                    key={`${item.id}-escrever`}
                    onPress={() => {
                      void update($, rascunho, () => item.escrever)
                      void $.prompt.fill({ text: item.escrever, mode: 'replace' })
                    }}
                  >
                    Escrever
                  </Button>
                  <Button
                    key={`${item.id}-pular`}
                    onPress={() => {
                      void update($, pulados, lista => [...lista, item.id])
                    }}
                  >
                    Pular
                  </Button>
                </Box>
              </Box>
            ))}
          </Box>
        ))}

        {escondidos.length > 0 ? (
          <Button
            key="restaurar"
            onPress={() => {
              void update($, pulados, () => [])
            }}
          >
            Mostrar os {escondidos.length} pulados
          </Button>
        ) : null}
      </Box>
    )
  })
}
