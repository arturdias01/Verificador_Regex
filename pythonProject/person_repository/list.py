from configs.connection import session
from entities.person_table import Person


class ListPerson:
    @classmethod
    def list(cls):
        all_person = session.query(Person).all()
        print('\n')
        for person in all_person:
            print(f'ID: {person.id} | NOME: {person.name}, | EMAIL: {person.email_address} | CPF: {person.cpf}')


ListPerson.list()
