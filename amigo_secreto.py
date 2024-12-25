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
        while True:                                  # Loop até um sorteio válido acontecer
            lista_sorteio = self.lista_nomes.copy()  # Faz uma cópia da lista de nomes
            random.shuffle(lista_sorteio)            # Embaralha a cópia

            self.dicionario_de_nomes.clear()         # Limpa o sorteio anterior (se existir)
            for i in self.lista_nomes:               # Para cada participante:
                if lista_sorteio[-1] == i:           # Evita que alguém tire a si mesmo
                    random.shuffle(lista_sorteio)    # Se for o caso, embaralha de novo
                self.dicionario_de_nomes[i] = lista_sorteio.pop()  # Atribui o sorteio
            
            # Verifica se o sorteio foi válido (ninguém tirou a si mesmo)
            if all(k != v for k, v in self.dicionario_de_nomes.items()):
                break                                # Se o sorteio for válido, sai do loop
        
        print("Resultado do sorteio:\n", self.dicionario_de_nomes)

    
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