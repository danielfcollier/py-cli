def getMessage(prices, id):
    messages = dict()

    messages["planos"] = """
A Dra. Geisa atende com hora marcada e com consultas mais longas de no mínimo 45 minutos, o que só é possível no formato de consultas particulares.

*Reembolso de Consultas Particulares*

A Dra. Geisa oferece o recibo da consulta, que pode ser entregue ao seu plano de saúde para solicitar o reembolso parcial ou integral do valor da consulta.

Por favor, verifique o seu contrato e as possibilidades de reembolso. Estamos à disposição para orientá-la e tirar dúvidas.
"""

    messages["calendario"] = """
No momento, a Dra. Geisa está atendendo no seguinte formato:

> Online: 3 semanas por mês 

> Presencial: 1 semana por mês

Agenda Presencial em Florianópolis:

> Março: dias 24, 25 e 26
> Abril: dias 28, 29 e 30
> Maio: dias 26, 27 e 28

Previsão Florianópolis:

> Junho: dias 23, 24 e 25
> Julho: dias 28, 29 e 30
"""

    messages["agenda"] = """
Períodos de Atendimento Presencial em Florianópolis:
> Manhã: Quarta-feira e Quinta-feira
> Tarde: Quarta-feira, Quinta-feira e Sexta-feira

Períodos de Atendimento Online:
> Manhã e Tarde: Terça-feira, Quarta-feira e Quinta-feira
"""

    messages["consultas"] = """
Informações sobre o Acompanhamento:

🍃 De acordo com suas necessidades, você receberá  a orientação para marcar uma nova consulta de 45 min dentro de um prazo de 10 a 90 dias.

🦋 Em geral, o tratamento inicia com consultas a cada 3 meses com novos exames e receitas, até que se chegue ao ponto em que será possível realizar manutenções a cada 6 meses e até 1 ano.

💫 Casos sensíveis ou graves podem precisar de consultas de 90 min ou de um acompanhamento inicial mais próximo com intervalos mensais.

🌻 A consulta de 90 min também pode ser solicitada quando você já vier com uma bateria extensa de exames em Medicina Funcional e deseje que a Dra. Geisa consiga avaliá-los desde a 1ª consulta

💌 O email é o canal de comunicação direto com a Dra Geisa para tirar dúvidas e quaisquer orientações que você precisar. Quando houver alguma alteração do preventivo, a Dra. lhe enviará orientações por email de como proceder.
"""

    messages["diu"] = f"""
Seguem as informações para colocação de DIU:

- você precisa fazer uma consulta prévia para a Dra. Geisa conhecê-la, conferir se você está bem informada dos prós e contras do método pretendido, com informações completas acerca das opções de acordo com seu momento de vida, tirar suas dúvidas e então, para você estar segura da indicação do procedimento. A consulta pode ser online ou presencial:

> 25 min: R$ {prices["pre-diu"]["presencial"]} Presencial ou R$ {prices["pre-diu"]["online"]} Online
> 45 min: R$ {prices["beija-flor"]["presencial"]} Presencial ou R$ {prices["beija-flor"]["online"]} Online

- Colocação do DIU: R$ {prices["diu"]}

> O valor da colocação pode ser parcelado em até 4x sem juros no cartão de crédito ou em até 12x com juros do sistema de pagamento.

- DIU: você irá adquirir à parte, direto com a farmácia por meio da receita que a Dra. fornecer.

> DIUs hormonais:  Mirena | Kyleena
> DIUs não-hormonais: Cobre | Cobre e Prata
"""

    messages["artemisia"] = f"""
Seguem os valores das consultas, *Consultas e Seguimentos - Sem Retornos*.

*Consulta Online ou Presencial*

🌿 Modalidade Artemísia de *25 min*
> Consulta Ginecológica focada no exame físico ou queixas pontuais de urgência. Valor: R$ {prices["urgencia"]}
"""

    if id == "all":
        for key in messages:
            print(messages[key])
    else:
        options = ["all"] + list(messages.keys())
        default_message = f"É necessário incluir uma opção válida! Opções: {options}"

        message = messages.get(id, default_message)
        print(message)
