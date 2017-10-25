import usuario
import filme

filmes_assistidos=[]

def registrar_filme_assistido(cod_filme,cpf):
    filme_assistido=[cpf,cod_filme]
    filmes_assistidos.append(filme_assistido)

def listar_filmes_assistidos(cpf):
    usuario=usuario.buscar_usuario(cpf)
    cpf= usuario[0]
    nome=usuario[1]
    
