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

    def telefone():
        if self.telefone is not None and (len(self.telefone)) < 10 or len(self.telefone) > 11:
            print("Telefone inválido.")

    def email():
        if self.email is not None and '@' not in self.email:
            print("E-mail inválido.")

    def getNome(self):
        return self.nome
   

Pedro = Cliente("Pedro", "12345678901", "1234567890", "pedro123@email.com")
Sarah = Cliente("Sarah", "11122233344", "9876543210", "sarah@email.com")

print(Sarah)
print(Pedro.getNome())




"""
Cliente(String nome, String cpf)

Cria um cliente contendo nome e CPF.

String getCpf()

Retorna o CPF do cliente.

String getTelefone()

Retorna o telefone do cliente.

String getEmail()

Retorna o e-mail do cliente.

void alterarTelefone(String telefone)

Atualiza o telefone do cliente.

void alterarEmail(String email)

Atualiza o e-mail do cliente.
"""


    