from tkinter import *
import re



def menu():
    """
    representa o menu da calculadora
    :return:
    """
    print('Digite uma opção')

    conta = input('Digite os valores para cálculo.')

def processa(valores: str):
    """
    processa os valores e retorna o resultado
    :param valores: conjunto de números e operadores
    :return:
    """

    inicio = 0
    vet_op = []
    vet_num = re.split('[+-]', valores)

    for i in range(len(valores)):
        if valores[i] in ['+','-','*','/']:
            vet_op.append(valores[i])

    for op in vet_op:
        if len(vet_num) > 1:
            if op == '+':
                aux = int(vet_num[0]) + int(vet_num[1])
                vet_num.pop(0)
                vet_num.pop(0)
                vet_num.insert(0, aux)
            elif op == '-':
                aux = int(vet_num[0]) - int(vet_num[1])
                vet_num.pop(0)
                vet_num.pop(0)
                vet_num.insert(0, aux)

    print(aux)


valores = '11+22-10+44'
# aux = re.split('[+-]', valores)
# print(aux)

processa(valores=valores)



# janela = Tk()
# janela.title('Calculadora')
# if __name__ == "__main__":
#     menu()
#
# janela.mainloop()
