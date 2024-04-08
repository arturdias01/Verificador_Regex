from configs.base import Base
from configs.connection import engine
from person_repository.list import ListPerson
from person_repository.insert import InsertIntoPerson
from validation.regex_validation import RegexValidation


def delimit():
    print('\n', '-' * 50, '\n')


Base.metadata.create_all(engine)

menu = """
--Sistema de cadastro--

[1] - Listar pessoas;
[2] - Cadastrar pessoas;
[0] - Sair.
"""

while True:
    print(menu)
    option = input('>>> ')

    if option == '0':
        break
    elif option == '1':
        ListPerson.list()
        delimit()
    elif option == '2':
        nome = input('Nome: ')
        email = input('Email: ')
        cpf = input('CPF(XXX.XXX.XXX-XX): ')

        validate = RegexValidation(email, cpf)
        val = validate.confirm()

        if val == True:
            new_person = InsertIntoPerson(nome, email, cpf)
            new_person.confirm()
            delimit()
        else:
            print('\nERRO: Email ou CPF inválido.')
            delimit()
            continue
