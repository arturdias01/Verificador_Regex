import re


class RegexValidation:
    def __init__(self, email, cpf):
        self.check = 0
        self.__email = email
        self.__cpf = cpf
        self.expr_cpf = re.compile(r'\d{3}\.\d{3}\.\d{3}\-\d{2}')
        self.expr_email = re.compile(r'^(?=.{1,256}$)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')

    def __email_validation(self):
        if self.expr_email.match(self.__email):
            self.check += 1

    def __cpf_validation(self):
        if self.expr_cpf.match(self.__cpf):
            self.check += 1

    def confirm(self):
        self.__email_validation()
        self.__cpf_validation()
        if self.check == 2:
            return True


