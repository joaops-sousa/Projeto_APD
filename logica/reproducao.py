from logica import usuario
from logica import filme
from logica import historico


def reproduzir_filme(cpf,cod_filme):
    user = usuario.buscar_usuario(cpf)
    movie = filme.buscar_filme(cod_filme)
    if user == None or movie == None:
        return False
    else:
        historico.registrar_filme_assistido(cod_filme,cpf)
        return True
