from equacao import equacionar
from primeira_calculadora import solucionar,escrever_titulo,escrever_titulo_conta_normal
import bn
def main():
    while True:
        escrever_titulo()
        tipo_conta=input('digite aqui: ')
        if tipo_conta=='F':
            break
        if tipo_conta=='C':
            escrever_titulo_conta_normal()
            conta=input('conta: ').split()
            solucao=solucionar(conta)
            print('')
            print(f' resultado: {solucao}')
        if tipo_conta=='S':
            bn.calcular_segundo_grau()
        if tipo_conta=='E':
            equacionar()




main()