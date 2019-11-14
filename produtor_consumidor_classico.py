import threading

# Prof. Gustavo Wagner, gugawag@gmail.com
# IFPB - Sistemas Operacionais
# Explicacao: solucao classica para o problema do produtor-consumidor, com espera ocupada.
#             Propensa a condicoes de disputa

TAMANHO_BUFFER = 10
contador = 0
buffer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
entrada = 0
saida = 0
item_produzido = 0


class Produtor:

    def __init__(self):
        pass

    def produzir(self):
        global contador
        global entrada
        global saida
        global buffer
        global TAMANHO_BUFFER
        global item_produzido

        while True:
            # produz um item em next_produced
            while contador == TAMANHO_BUFFER:
                continue  # não faz coisa alguma
            item_produzido += 1
            buffer[entrada] = item_produzido  # item produzido
            print('Produtor - Produzido item ', buffer[entrada])
            entrada = (entrada + 1) % TAMANHO_BUFFER
            contador += 1


class Consumidor:

    def __init__(self):
        pass

    def consumir(self):
        global contador
        global entrada
        global saida
        global buffer
        global TAMANHO_BUFFER

        print(contador, entrada, saida, len(buffer), TAMANHO_BUFFER)
        while True:
            while contador == 0:
                continue  # não faz coisa alguma
            item_consumido = buffer[saida]
            print('Consumidor - Consumido item ', item_consumido)
            saida = (saida + 1) % TAMANHO_BUFFER
            contador -= 1
            # consome o item item_consumido


produtor = Produtor()
consumidor = Consumidor()

t_produtor = threading.Thread(target=produtor.produzir)
t_consumidor = threading.Thread(target=consumidor.consumir)


t_produtor.start()
t_consumidor.start()
