def getMessage(prices, n, name):
  messages = [
    f"""
Olá {name},

A Dra. Geisa atende com Ginecologia Integrativa com *foco em Equilíbrio Hormonal Feminino*, que utiliza as bases da Medicina e Ginecologia Tradicionais ampliadas com a visão da Medicina Funcional, Modulação Hormonal Bioidêntica e Terapias Integrativas.
""",
    f"""
Períodos de Atendimento Presencial em Florianópolis:
> Manhã: Quarta-feira e Quinta-feira
> Tarde: Quarta-feira, Quinta-feira e Sexta-feira

Períodos de Atendimento Online:
> Manhã e Tarde: Terça-feira, Quarta-feira e Quinta-feira
""",
    f"""
Seguem os valores das consultas, *Consultas e Seguimentos - Sem Retornos*.

*Consulta Presencial*

✨ Modalidade Beija-flor de *45 min*
> Indicada para 1ª consulta ou seguimento de tratamento com enfoque em Medicina Funcional. Para essa modalidade, veja também a opção de Consulta Online. Valor: R$ {prices["beija-flor"]["presencial"]}

🌻Modalidade Girassol de 90 min
> Indicada para pacientes em momentos sensíveis para um olhar mais aprofundado de exames e orientações médicas. Valor: de R$ {prices["girassol"]["presencial"]} por {prices["girassol"]["online"]}

*Consulta Online*

✨ Modalidade Beija-flor de *45 min*
> Indicada para 1ª consulta ou seguimento de tratamento com enfoque em Medicina Funcional. Valor: R$ {prices["beija-flor"]["online"]}

🌻Modalidade Girassol de *90 min*
> Indicada para pacientes em momentos sensíveis para um olhar mais aprofundado de exames e orientações médicas. Valor: R$ {prices["girassol"]["online"]}
""",
    """"
*De acordo com a modalidade que você escolher, passo as datas disponíveis.*

(Me desculpe se você já é paciente e conhece as informações. Agradeço à compreensão.)
    """,
    """
Períodos de Atendimento Presencial em Florianópolis:
> Manhã: Quarta-feira e Quinta-feira
> Tarde: Quarta-feira, Quinta-feira e Sexta-feira

Períodos de Atendimento Online:
> Manhã e Tarde: Terça-feira, Quarta-feira e Quinta-feira
"""
  ]

  try:
    required_message = int(n, 10)
    print(messages[required_message - 1])
  except:
    for index, message in enumerate(messages):
      print(f"### MENSAGEM DE WHATSAPP {index + 1}:")
      print(message)
