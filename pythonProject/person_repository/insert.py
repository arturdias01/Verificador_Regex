from configs.connection import session
from entities.person_table import Person


class InsertIntoPerson:
    def __init__(self, name, email, cpf):
        self.name = name
        self.email = email
        self.cpf = cpf

    def __insert(self):
        new_person = Person(name=self.name, email_address=self.email, cpf=self.cpf)
        session.add(new_person)
        session.commit()

    def __repr__(self):
        return f'Nome: {self.name} | email_address: {self.email} | cpf: {self.cpf}'

    def confirm(self):
        print(f'\n{self.__repr__()}')
        option = input('[1] - confirmar inserção | [2] - cancelar inserção\n>>> ')
        if option == '1':
            self.__insert()
            print('\nPessoa cadastrada com sucesso.')
        else:
            print('\nCadastro cancelado.')
