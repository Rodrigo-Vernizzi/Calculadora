import argparse
import sys

def pontuar_frase(frase):
    for i,palavra in enumerate(frase):
        if i==0:
            nome=palavra
        else:
         nome=nome+"_"+palavra
    
    return nome

def abrir_arquivo(argumentos):
    informacoes=[]
    with open (argumentos.a,'r') as arquivo:
        for i,linha in enumerate(arquivo):
            if i!=0:
                informacoes.append(linha.strip().split())
    for i,categorias in enumerate(informacoes):
        for i in range(len(categorias)):
            palavra=categorias[i].strip(',')
            categorias[i]=palavra
    return informacoes


def escrever_arquivo(argumentos, informacoes):
    with open (argumentos.a,'w') as arquivo:
        arquivo.write('sep=,'+'\n')
        for categoria in informacoes:
            for i in categoria:
                arquivo.write(str(i) + ',' + ' ')
            arquivo.write('\n')

def criar_evento(argumentos):
    informacoes=abrir_arquivo(argumentos)

    lista_nome = argumentos.nome.split()
    nome=pontuar_frase(lista_nome)
    lista_descricao=argumentos.descricao.split()
    descricao=pontuar_frase(lista_descricao)
    if len(informacoes)==0:
        informacoes.append([1])
        print(f'evento 1 criado')
        informacoes.append([nome])
        informacoes.append([descricao])
        informacoes.append([argumentos.data])
        informacoes.append([argumentos.hora])
    else:
        numero=str(informacoes[0][len(informacoes[0])-1]).strip(',')
        proximo_numero=int(numero)+1
        print(f'evento {proximo_numero} criado')
        informacoes[0].append(proximo_numero)
        informacoes[1].append(nome)
        informacoes[2].append(descricao)
        informacoes[3].append(argumentos.data)
        informacoes[4].append(argumentos.hora)
    
    escrever_arquivo(argumentos,informacoes)
            
def alterar_evento(argumentos):
    numero=argumentos.evento-1
    lista_argumentos=[argumentos.nome,argumentos.descricao,argumentos.data,argumentos.hora]
    for i, informacao in enumerate(lista_argumentos):
        if informacao != 'None':
            categoria=i+1
            if categoria == 1 or categoria==2:
                frase=informacao.split()
                frase=pontuar_frase(frase)
                informacao=frase
            mudanca=informacao

    informacoes=abrir_arquivo(argumentos)

    informacoes[categoria][numero]=mudanca

    escrever_arquivo(argumentos,informacoes)

    print ('alteracao completa')


def remover_evento(argumentos):
    numero=int(argumentos.evento)
    informacoes=abrir_arquivo(argumentos)
    
    for i, categoria in enumerate(informacoes):
       categoria[numero-1:numero]=[]
           
                
    informacoes0=[]
    for i in informacoes[0]:
        if int(i)> numero:
            j=int(i)-1
            i=j
        informacoes0.append(i)
    informacoes[0]=informacoes0
      
    escrever_arquivo(argumentos, informacoes)
    print(f'evento {numero} removido')


def listar_eventos(argumentos):
    data_interessado=argumentos.data
    informacoes=abrir_arquivo(argumentos)
    lista_de_eventos=[]
    for i,data_evento in enumerate(informacoes[3]):
        if data_evento==data_interessado:
            lista_de_eventos.append(i)
    
    print(f'eventos do dia {data_interessado}')
    print('-'*30)
    for evento in lista_de_eventos:
        nome=informacoes[1][evento]
        descricao=informacoes[2][evento]
        hora=informacoes[4][evento]
        print(f'Evento {evento+1} - {nome}')
        print(f'descricao: {descricao}')
        print(f'data: {data_interessado}')
        print(f'hora: {hora}')
        print(f'-'*30)






def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", help="nome do arquivo", type=str)
    parser.add_argument("acao", help="cria um arquivo ", default='None', type=str)
    parser.add_argument("--evento", help=" identificador ", default=0 , type=int)
    parser.add_argument("--nome", help=" nome do evento", default='None', type=str)
    parser.add_argument("--descricao", help="descricao do evento",default='None', type=str)
    parser.add_argument("--data", help="data do evento", default='None', type=str)
    parser.add_argument("--hora", help="hora do evento", default='None', type=str)

    args=parser.parse_args()

    
    if 'inicializar' == args.acao:
        with open (args.a, 'w'):
            pass
        print(f'arquivo {args.a} criado')

    elif args.acao=='criar':
        criar_evento(args)
    
    elif args.acao=='alterar':
        alterar_evento(args)

    elif args.acao=='remover':
        remover_evento(args) 
    elif args.acao=='listar':
        listar_eventos(args)




main()