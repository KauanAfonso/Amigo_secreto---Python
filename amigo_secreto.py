import subprocess

import random
class Amigo_secreto:

    def __init__(self):
        self.lista_nomes = []
        self.lista_sorteio = []
        self.dicionario_de_nomes = {}

    def pedir_nomes(self):
        i = 1
        print("Envie os nomes de quem irá participar, quando finalizar digite 0\n")
        while True:
            nomes = input(f"Digite o nome de {i} participante: ")
            if nomes == "0":
                print("Nomes enviados...")
                break
            self.lista_nomes.append(nomes)
            self.lista_sorteio.append(nomes)
            i+=1
        return self.lista_nomes, self.lista_sorteio
    
    def sortear(self):
        random.shuffle(self.lista_sorteio) 
        
        for i in self.lista_nomes:
            nome_aleatorio = random.choice(self.lista_sorteio)
            if nome_aleatorio != i:
                self.dicionario_de_nomes[i] = nome_aleatorio
                self.lista_sorteio.remove(nome_aleatorio)
            else:
                continue
        print(self.dicionario_de_nomes)
        return self.dicionario_de_nomes
    
    def mostrar_sorteio(self):
        while True:
            resposta = input("Dgite seu nome para ver quem você sorteou ou 0 para sair: \n")
            if resposta == "0":
                break
            print(f" {resposta} você tirou o(a): {self.dicionario_de_nomes[resposta]}")
            input("---------Pressione ENTER--------------")
            subprocess.run('cls', shell=True)
    

amigo = Amigo_secreto()

amigo.pedir_nomes()
amigo.sortear()
amigo.mostrar_sorteio()


#a cada sorteio retirar o nome da lista_nomes para não sortear de novo