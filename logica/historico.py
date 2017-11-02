from logica import usuario
from logica import filme

historico_geral =[]

def registrar_filme_assistido(cod_filme,cpf):
    user = usuario.buscar_usuario(cpf)
    movie = filme.buscar_filme(cod_filme)
    if user == None or movie == None:
        return False
    else:
        aux = [user,movie]
        historico_geral.append(aux)
        return True

def listar_filmes_assistidos(cpf):
    user = usuario.buscar_usuario(cpf)
    filmes_assistidos = []
    for f in historico_geral:
        if f[0] == user:
            filmes_assistidos.append(f[1])
    if len(filmes_assistidos) < 1:
        return None
    
    return filmes_assistidos

def listar_historico_geral():
    return historico_geral

def remover_todos_historicos():
    global historico_geral
    historico_geral = []

def limpar_historico(cpf):
    user = usuario.buscar_usuario(cpf)
    if user == None:
        return False
    else:
        for i in range(len(historico_geral)):
            for h in historico_geral:
                if h[0] == user:
                    historico_geral.remove(h)            
    return True
    
