def getMessage(data, id):
  messages = dict()

  messages["cadastro"] = """
Vou completar seu atendimento, preciso fazer seu pré-cadastro:

NOME COMPLETO

DATA DE NASCIMENTO

CPF

RG

EMAIL

CEP

---

TELEFONE (só se contato da paciente for por email)
"""

  messages["prontuario"] = """
Combinado. Vou abrir o prontuário e já lhe passo as informações.
"""

  messages["online"] = f"""
*Guarde as orientações.*
Segue o link para atendimento da sua consulta online:

{data["meet-link"]}

*POR FAVOR, LEIA TODOS OS PONTOS:*

- Certifique-se da sua conexão de internet 10 minutos antes da consulta.

- Caso vá se consultar utilizando seu celular, acesse o link antes e instale o aplicativo solicitado (Google Meet).

- Algumas vezes pelo celular é preciso clicar duas vezes no link.

- APERTE o botão *Pedir p/ participar* e aguarde.

- Eventualmente Pode ser que a Dra. Geisa se atrase por estar finalizando outra consulta, pedimos que aguarde.

- Em caso de problemas com o Google Meet, a Dra. Geisa entrará em contato aqui pelo WhatsApp.
"""

  messages["agenda"] = f"""
Sua consulta está agendada para sexta-feira dia *{data["dia"]} às {data["hora"]}*.
"""

  messages["pagamento"] = f"""
CONFIRMAÇÃO FINAL

É feita mediante o *envio do comprovante* da confirmação financeira durante a marcação da consulta, *vencimento para amanhã*.. Se você precisar, poderá remarcar sua consulta.

As orientações de pagamento são enviadas *por email*, você poderá realizar o pagamento por boleto bancário, cartão de crédito ou débito.

Em caso de dificuldade para acessar o email, por favor me avise, posso enviar por aqui.
"""

  if id == "all":
    for key in messages:
      print(messages[key])
  else:
    options = ["all"] + list(messages.keys())
    default_message = f"É necessário incluir uma opção válida! Opções: {options}"

    message = messages.get(id, default_message)
    print(message)
