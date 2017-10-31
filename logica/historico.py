import usuario
import filme

filmes_assistidos=[]

def registrar_filme_assistido(cod_filme,cpf):
    user = usuario.buscar_usuario(cpf)
    movie = filme.buscar_filme(cod_filme)
    aux = [user,movie]
    filmes_assistidos.append(aux)

def listar_filmes_assistidos(cpf):
    user = usuario.buscar_usuario(cpf)
    aux = []
    for f in filmes_assistidos:
        if f[0] == user:
            aux.append(f[1])
    if len(aux) < 1:
        return None
    
    return aux
