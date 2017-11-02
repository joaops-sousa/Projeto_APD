from logica import usuario
from logica import historico

def menu_adicionar():
    print("\nAdicionar Usuário \n")
    cpf = int(input("CPF: "))
    nome = str(input("Nome: "))
    email = str(input("Email: "))
    senha = str(input("Senha: "))

    usuario.adicionar_usuario(cpf,nome,email,senha)

def imprimir_usuario(usuario):
    print("CPF: ",usuario[0])
    print("Nome: ",usuario[1])
    print("Email: ",usuario[2])
    print()
    
def menu_listar():
    print("\nListar Usuários \n")
    usuarios = usuario.listar_usuarios()
    for u in usuarios:
        imprimir_usuario(u)

def menu_buscar():
    print("\nBuscar Usuário por CPF \n")
    cpf = int(input("CPF: "))
    u = usuario.buscar_usuario(cpf)
    if u == None:
        print("Usuário não encontrado.")
    else:
        imprimir_usuario(u)

def menu_remover():
    print("\nRemover Usuário \n")
    cpf = int(input("CPF: "))
    u = usuario.remover_usuario(cpf)
    if u == False:
        print("\nUsuário não encontrado.")
    else:
        print("\nUsuário Removido.")

def menu_exibir_historico():
    print("\nExibir Histórico do Usuário por CPF \n")
    cpf = int(input("CPF: "))
    u = usuario.buscar_usuario(cpf)
    hist = historico.listar_filmes_assistidos(cpf)

    if u == None:
        print("\nUsuário não encontrado.")
    elif hist == None:
        print("\nSeu histórico está vazio.")
    else:
        imprimir_usuario(u)
        print("\nHistórico: \n")
        for h in hist:
            print(h)

def menu_limpar_historico():
    print("\nLimpar Histórico do Usuário por CPF \n")
    cpf = int(input("CPF: "))
    h = historico.limpar_historico(cpf)

    if h == False:
        print("Usuário não encontrado.")
    else:
        print("Histórico removido.")
            
    
def exibir_menu_usuario():
    run_usuario = True
    menu = ("\n----------------\n"+
             "(1) Adicionar Usuário \n" +
             "(2) Listar Usuários \n" +
             "(3) Buscar Usuário por CPF \n" +
             "(4) Remover Usuário \n" +
             "(5) Exibir Histórico do Usuário por CPF \n"+
             "(6) Limpar Histórico do Usuário por CPF \n"+
             "(0) Voltar\n"+
            "----------------")

    while run_usuario:
        print(menu)
        op = int(input("Digite sua escolha: "))

        if op == 1:
            menu_adicionar()
        elif op==2:
            menu_listar()
        elif op ==3:
            menu_buscar()
        elif op==4:
            menu_remover()
        elif op == 5:
            menu_exibir_historico()
        elif op == 6:
            menu_limpar_historico()
        elif op==0:
            run_usuario = False
