import subprocess
import random
class Amigo_secreto:

    #construtora
    def __init__(self):
        self.__lista_nomes = []
        self.__lista_sorteio = []
        self.__dicionario_de_nomes = {}
        
    #funcão para mensagem no inicio do jogo    
    def mensagem_inicial(self):
            print(r"""
    *******************************
    *                             *
    *      🎁 AMIGO SECRETO 🎁    *
    *                             *
    *******************************
          Feliz Sorteio! 🎄
    """)

    #funcão para pedir os nomes dos jogadores
    def pedir_nomes(self):
        i = 1
        print("Envie os nomes de quem irá participar, quando finalizar digite 0\n")
        while True:
            nomes = input(f"Digite o nome de {i} participante: ")
            if nomes == "0":
                print("Nomes enviados...")
                break
            self.__lista_nomes.append(nomes)
            self.__lista_sorteio.append(nomes)
            i+=1
        return self.__lista_nomes, self.__lista_sorteio
    
    #funcao de sorteio
    def sortear(self):
        while True:                                  # Loop até um sorteio válido acontecer
            lista_sorteio = self.__lista_nomes.copy()  # Faz uma cópia da lista de nomes
            random.shuffle(lista_sorteio)            # Embaralha a cópia

            self.__dicionario_de_nomes.clear()         # Limpa o sorteio anterior (se existir)
            for i in self.__lista_nomes:               # Para cada participante:
                if lista_sorteio[-1] == i:           # Evita que alguém tire a si mesmo
                    random.shuffle(lista_sorteio)    # Se for o caso, embaralha de novo
                self.__dicionario_de_nomes[i] = lista_sorteio.pop()  # Atribui o sorteio
            
            # Verifica se o sorteio foi válido (ninguém tirou a si mesmo)
            if all(k != v for k, v in self.__dicionario_de_nomes.items()):
                break                                # Se o sorteio for válido, sai do loop
        
        return self.__dicionario_de_nomes

    #funcão que irá mostrar quem o jogador tirou no sorteio
    def mostrar_sorteio(self):
        while True:
            resposta = input("Dgite seu nome para ver quem você sorteou ou 0 para sair: \n")
            if resposta == "0":
                print("JOGO FINALIZADO !!!!")
                break
            print(f" {resposta} você tirou o(a): {self.__dicionario_de_nomes[resposta]}")
            input("---------Pressione ENTER--------------")
            subprocess.run('cls', shell=True)
    

#instanciando e chamando os metodos
amigo = Amigo_secreto()
amigo.mensagem_inicial()
amigo.pedir_nomes()
amigo.sortear()
amigo.mostrar_sorteio()


