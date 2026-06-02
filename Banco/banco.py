Class Banco:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.contas = []

    def nome(self):
        if self.nome is None or self.nome == "" or len(self.nome) < 3:
            print("Nome do banco inválido.")

    def codigo(self):
        if self.codigo is None or self.codigo <= 0:
            print("Código do banco inválido.")

'''
Contas
Um banco pode possuir várias contas.

Não podem existir duas contas com o mesmo número dentro do mesmo banco.

Uma conta somente pode pertencer a um banco por vez.

O banco deve ser capaz de localizar contas a partir de seu número.
'''