usuarios = []

def adicionar_usuario(cpf,nome,email,senha):
    usuario = [cpf,nome,email,senha]
    usuarios.append(usuario)
    
def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for u in usuarios:
        if u[0] == cpf:
            return u
    return None

def remover_usuario(cpf):
    for u in usuarios:
        if u[0] == cpf:
            usuarios.remove(u)
            return True
    return False

def iniciar_usuarios():
    adicionar_usuario(111111,"Jorge","jorge@gmail.com","senha1")
    adicionar_usuario(222222,"Fabio","fabio@gmail.com","senha2")
    adicionar_usuario(333333,"Lara","lara@gmail.com","senha3")
