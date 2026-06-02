class Cliente:
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email 
    
    def nome():
         if self.nome is None or self.nome == "" or len(self.nome) < 5:
            print("Nome inválido.")

    def cpf():
        if self.cpf is None or self.cpf == "" or len(self.cpf) != 11:
            print("CPF inválido.")

    




"""
O telefone é opcional.

Quando informado, deve possuir entre 10 e 11 dígitos numéricos.

Caso um telefone inválido seja informado, o sistema não deve armazená-lo.

E-mail
O e-mail é opcional.

Quando informado, deve conter o caractere '@'.

Caso um e-mail inválido seja informado, o sistema não deve armazená-lo.

"""


    