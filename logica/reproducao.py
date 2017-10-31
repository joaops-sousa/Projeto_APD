from logica import usuario
from logica import filme
from logica import historico

avaliacoes = []

def reproduzir_filme(cpf,cod_filme):
    user = usuario.buscar_usuario(cpf)
    movie = filme.buscar_filme(cod_filme)
    if user == None or movie == None:
        return False
    else:
        historico.registrar_filme_assistido(cod_filme,cpf)
        return True

def avaliar_filme(cpf,cod_filme,nota):
    user = usuario.buscar_usuario(cpf)
    movie = filme.buscar_filme(cod_filme)
    if user == None or movie == None:
        return False
    else:
        avaliacao = [cpf,user[1],cod_filme,movie[1],nota]
        avaliacoes.append(avaliacao)
        return True

def listar_avaliacoes():
    return avaliacoes

def listar_avaliacoes_por_cpf(cpf):
    aux = []
    for a in avaliacoes:
        if cpf == a[0]:
            aux.append(a)
    return aux

def remover_todas_avaliacoes():
    global avaliacoes
    avaliacoes = []
