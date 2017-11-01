from logica import usuario
from logica import filme

avaliacoes = []

def avaliar_filme(cpf,cod_filme,nota):
    user = usuario.buscar_usuario(cpf)
    movie = filme.buscar_filme(cod_filme)
    if user == None or movie == None:
        return False

    avaliacao = [cpf,user[1],cod_filme,movie[1],nota]
    avaliacoes.append(avaliacao)
    return True

def listar_avaliacoes():
    return avaliacoes

def listar_avaliacoes_por_filme(cod_filme):
    aux = []
    for a in avaliacoes:
        if cod_filme == a[2]:
            aux.append(a)
    return aux

def remover_todas_avaliacoes():
    global avaliacoes
    avaliacoes = []    
