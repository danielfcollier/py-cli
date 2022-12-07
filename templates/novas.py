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
    """
Segue um vídeo que a Dra. Geisa preparou para as novas pacientes:
""",
    """
(o video!)
""",
    f"""
Seguem os valores das consultas, *Consultas e Seguimentos - Sem Retornos*.

*Consulta Presencial*

🌿 Modalidade Artemísia de *25 min*

> Consulta Ginecológica focada no exame físico ou queixas pontuais de urgência. Valor: R$ {prices["urgencia"]}

✨ Modalidade Beija-flor de *45 min*

> Indicada para 1ª consulta ou seguimento de tratamento com enfoque em Medicina Funcional. Para essa modalidade, veja também a opção de Consulta Online. Valor: R$ {prices["beija-flor"]["presencial"]}

*Consulta Online*

✨ Modalidade Beija-flor de *45 min*

> Indicada para 1ª consulta ou seguimento de tratamento com enfoque em Medicina Funcional. Valor: R$ {prices["beija-flor"]["online"]}

🌻Modalidade Girassol de *90 min*

> Indicada para pacientes em momentos sensíveis para um olhar mais aprofundado de exames e orientações médicas. Valor: de R$ {prices["girassol"]["presencial"]} por R$ {prices["girassol"]["online"]}
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
      print(f"### MENSAGEM DE WHATSAPP {index}:")
      print(message)
