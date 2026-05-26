# Classe conta de banco 

class Conta():
    def __init__(self,nome,saldo,senha):
        self.nome =  nome
        self.saldo = saldo
        self.senha = senha 

    def deposito(self,qtdDepositar,senha):
        if senha != self.senha:
            print('Senha incorreta')
            return None

        if qtdDepositar < 0:
            print('Você não pode depositar um valor negativo')
            return None 

        self.saldo += qtdDepositar 
        return self.saldo

    def sacar(self,qtdSacar,senha):
        if senha != self.senha:
            print('Senha incorreta')
            return None 
        if qtdSacar < 0:
            print('Você não pode sacar um valor negativo')
            return None 
        if qtdSacar > self.saldo:
            print('Você não pode sacar mais do que há na sua conta')
            return None

        self.saldo -= qtdSacar 
        return self.saldo 
    
    def pegaSaldo(self,senha):
        if senha != self.senha:
            print('Desculpa, senha incorreta')
            return None
        return self.saldo

    def mostra(self):
        print('     Nome:',self.nome)
        print('     Saldo:',self.saldo)
        print('     Senha:',self.senha)
        print()

