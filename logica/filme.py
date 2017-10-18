filmes = []
codigo_filmes = 0

def __gerar_cod_filme():
    global codigo_filmes
    codigo_filmes += 1
    return codigo_filmes

def adicionar_filme(titulo,genero,ano):
    cod_filme = __gerar_cod_filme()

    filme = [cod_filme,titulo,genero,ano]
    filmes.append(filme)

def listar_filmes():
    return filmes

def buscar_filme(cod_filme):
    for f in filmes:
        if f[0] == cod_filme:
            return f
    return None

def buscar_filmes_por_genero(genero):
    aux = []
    for f in filmes:
       if f[2] == genero.lower():
            aux.append(f)
    if len(aux) < 1:
        return None

    return aux
           
def remover_filme(cod_filme):
    for f in filmes:
        if f[0] == cod_filme:
            filmes.remove(f)
            return True
    return False

def iniciar_filmes():
    adicionar_filme("Mercenários","ação",2010)
    adicionar_filme("It","terror",2017)
    adicionar_filme("Mãe","terror",2017)
    adicionar_filme("Vingadores","ação",2013)
