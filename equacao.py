from primeira_calculadora import solucionar


def solucionar_lado_oposto(equacao):
    for i,valor in enumerate(equacao):
        if valor=='y':
            posicao_y=i
        if valor=='=':
            posicao_igual=i
    if posicao_y<posicao_igual:
        lado_oposto=equacao[posicao_igual+1:]
        lado_y=equacao[:posicao_igual]
    else:
        lado_y=equacao[posicao_igual+1:]
        lado_oposto=equacao[:posicao_igual]

    lado_oposto=[solucionar(lado_oposto)]
    
    return lado_y, lado_oposto

def solucionar_parenteses(lado_y):
    while '(' in lado_y:
        for i,termo in enumerate(lado_y):
            if termo=='(':
                comeco=i
            if termo==')':
                final=i
                break
        if 'y' in lado_y[comeco:final+1]:
            lado_y[comeco]='['
            lado_y[final]=']' 
        else:
            sol_parenteses=[solucionar(lado_y[comeco+1:final])]
            lado_y[comeco:final+1]=sol_parenteses
    return lado_y

def achar_capsula(lado_y):
    if '[' not in lado_y:
        for i, termo in enumerate(lado_y):
            if termo=='y':
                lado_y[i]='capsula'
                capsula=['y']
                return lado_y,capsula
    else:
        for i,termo in enumerate(lado_y):
            if termo=='[':
                comeco=i
            if termo==']':
                final=i
        capsula=lado_y[comeco:final+1]
        lado_y[comeco:final+1]=['capsula']
        return lado_y,capsula
        

def fazer_divisao_sem_capsula(lado_y):
    for i, termo in enumerate(lado_y):
        if termo=='/' and lado_y[i-1]!='capsula' and lado_y[i+1]!='capsula':
            lado_y[i-1:i+2]=[float(lado_y[i-1])/float(lado_y[i+1])]
        if termo=='x' and lado_y[i-1]!='capsula' and lado_y[i+1]!='capsula':
                lado_y[i-1:i+2]=[float(lado_y[i-1])*float(lado_y[i+1])]
    
    return lado_y


def isolar_capsula(lado_y,lado_oposto):
    posicao_c=0
    for i, termo in enumerate(lado_y):
        if termo=='capsula':
            posicao_c=i
    print(f'posica0_c {posicao_c}')
    print(f'capsula {lado_y}')
    if posicao_c!=0:
        antes_da_capsula=lado_y[:posicao_c]
        depois_da_capsula=lado_y[posicao_c+1:]
    else:
        antes_da_capsula=[]
        depois_da_capsula=lado_y[posicao_c+1:]
    
    while '+' in depois_da_capsula or '-' in depois_da_capsula:
        for i, termo in enumerate(depois_da_capsula):
            if termo=='+':
                lado_oposto.append('-')
                lado_oposto.append(depois_da_capsula[i+1])
                depois_da_capsula[i:i+2]=[]
                break
            if termo=='-':
                lado_oposto.append('+')
                lado_oposto.append(depois_da_capsula[i+1])
                depois_da_capsula[i:i+2]=[]
                break
    
    while '+' in antes_da_capsula or '-' in antes_da_capsula:
        lado_oposto.append('-')
        lado_oposto.append(antes_da_capsula[0])
        antes_da_capsula[:1]=[]
        if antes_da_capsula[0]=='+':
            antes_da_capsula[:1]=[]
        else:
            antes_da_capsula[:1]=[]
            lado_oposto=['(']+lado_oposto+[')','x','-1']
    lado_oposto=[solucionar(lado_oposto)]
    print(f'antes {antes_da_capsula}')
    if 'x' in depois_da_capsula or '/' in depois_da_capsula:
        if depois_da_capsula[0]=='x':
            lado_oposto=[str(float(lado_oposto[0])/float(depois_da_capsula[1]))]
            depois_da_capsula=[]
        else:
            lado_oposto=[str(float(lado_oposto[0])*float(depois_da_capsula[1]))]
            depois_da_capsula=[]
    if '/' in antes_da_capsula or 'x' in antes_da_capsula:
        print(f'antes {antes_da_capsula}')
        if antes_da_capsula[1]=='x':
            lado_oposto=[str(float(lado_oposto[0])/float(antes_da_capsula[0]))]
        else:
            lado_oposto=[str(float(antes_da_capsula[0])/float(lado_oposto[0]))]
            antes_da_capsula=[]
    return ['capsula'],lado_oposto

def solucionar_capsula(capsula,lado_oposto):
    posicao_c=0
    if '[' not in capsula:
        return 'y',lado_oposto[0]
    else:
        print('a')
        for i, termo in enumerate(capsula):
            if termo=='y':
                capsula[i]='capsula'
        capsula[:1]=[]
        capsula[len(capsula)-1:]=[]
        for i, termo in enumerate(capsula):
            if termo=='capsula':
                posicao_c=i
        
        print(f'capsula {capsula}')
        print(f'lado oposto {lado_oposto}')

        
        capsula,lado_oposto=isolar_capsula(capsula,lado_oposto)
        return 'y',lado_oposto[0]


def equacionar():
    equacao=input().split()
    lado_y,lado_oposto=solucionar_lado_oposto(equacao)
    
    lado_y=solucionar_parenteses(lado_y)
    
    lado_y,capsula=achar_capsula(lado_y)
    
    lado_y=fazer_divisao_sem_capsula(lado_y)
    
    lado_y,lado_oposto=isolar_capsula(lado_y,lado_oposto)
    
    lado_y,lado_oposto=solucionar_capsula(capsula,lado_oposto)
    print(f'y = {lado_oposto}')
