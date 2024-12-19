import random
class Amigo_secreto:

    def __init__(self, lista_nomes):
        self.lista_nomes = []

    def pedir_nomes(self):

        print("Envie os nomes de quem irá participar, quando finalizar digite 0\n")
        while True:
            nomes = input("Digite o nome de 1 participante: ")
            self.lista_nomes.append(nomes)
            if nomes == "0":
                print("Nomes enviados...")
                break
        return self.lista_nomes
    
    def sortear(self):
        dicionario_de_nomes = {}
        for i in self.lista_nomes:
            nome_aleatorio = random.choice(self.lista_nomes)
            if nome_aleatorio != i:
                dicionario_de_nomes[i] = nome_aleatorio
            else:
                continue
        return dicionario_de_nomes
