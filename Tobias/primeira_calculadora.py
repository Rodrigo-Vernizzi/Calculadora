def escrever_titulo():
    print('CALCULADORA DO TOBIAS ------------------------')
    print('')
    print('apenas use numeros, e as operacoes +,-,x,/,(,),!')
    print('')
    print('deixe um espaço entre todos os termos e operacoes')
    print('')

def multiplicar_e_dividir(conta):
    while 'x' in conta or '/' in conta:
        for j,termo in enumerate(conta):
            if termo=='x':
                existes=False
                multiplicacao=float(conta[j-1])*float(conta[j+1])
                m=[multiplicacao]
                if j<len(conta)-1:
                    segunda_parte=conta[j+2:]
                    existes=True
                conta[j-1:j+2]=[]
                primeira_parte=conta[0:j-1]
                if existes:
                    conta=primeira_parte+m+segunda_parte
                else:
                    conta=primeira_parte+m
                break
            for j,termo in enumerate(conta):
                if termo=='/':
                    existes=False
                    multiplicacao=float(conta[j-1])/float(conta[j+1])
                    m=[multiplicacao]
                    if j<len(conta)-1:
                        segunda_parte=conta[j+2:]
                        existes=True
                    conta[j-1:j+2]=[]
                    primeira_parte=conta[0:j-1]
                    print(conta)
                    if existes:
                        conta=primeira_parte+m+segunda_parte
                    else:
                        conta=primeira_parte+m
                    break
            for item in conta:
                print(item,end=' ')
            print(' = ')
    return conta

def somar_e_subtrair(conta):
    while len(conta)>1:
        for i, termo in enumerate(conta):

            if termo=='+':
                soma=[]
                termo=float(conta[i-1])+float(conta[i+1])
                soma.append(termo)
                conta[i-1:i+2]=[]
                conta= soma+conta
                break
            if termo=='-':
                soma=[]
                termo=float(conta[i-1])-float(conta[i+1])
                soma.append(termo)
                conta[i-1:i+2]=[]
                conta= soma+conta
                break
    return conta

def tirar_parenteses(conta):
    while '(' in conta:
        for i,termo in enumerate(conta):
            if termo=='(':
                comeco=i+1
            if termo==')':
                final=i
                break
        primeira_parte=conta[:comeco-1]
        segunda_parte=conta[final+1:]
        parenteses=conta[comeco:final]
        
        parenteses=multiplicar_e_dividir(parenteses)
        parenteses=somar_e_subtrair(parenteses)
        conta=primeira_parte+parenteses+segunda_parte
        
    return conta

def resolver_fatorial(conta):
    while '!' in conta:
        j=1
        for i, termo in enumerate(conta):
            if termo=='!':
                n=int(conta[i-1])
                while n >0:
                    j=j*n
                    n=n-1
                conta[i-1]=j
                conta[i:i+1]=[]

    return conta







def solucionar(conta):
    conta=resolver_fatorial(conta)
    print(conta)
    conta=tirar_parenteses(conta)
    conta=multiplicar_e_dividir(conta)
    print(conta)
    conta=somar_e_subtrair(conta)
    print(conta)        
    solucao=conta[0]
    return solucao















def main():
    escrever_titulo()
    conta=input('conta: ').split()
    solucao=solucionar(conta)
    print(f' resultado: {solucao}')




main()