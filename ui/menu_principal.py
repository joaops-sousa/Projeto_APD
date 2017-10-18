from ui import menu_usuario
from logica import usuario

from ui import menu_filme
from logica import filme

def inicializar_dados():
    usuario.iniciar_usuarios()
    filme.iniciar_filmes()

def exibir_menu_principal():
    run_menu=True

    inicializar_dados()

    menu = ("\n----------------\n"+
             "(1) Menu Usuário \n" +
             "(2) Menu Filme \n" +
             "(0) Sair\n"
            "----------------")

    while run_menu:
        print(menu)

        op = int(input("Digite sua escolha: "))
        
        if op == 1:
            menu_usuario.exibir_menu_usuario()
        elif op == 2:
            menu_filme.exibir_menu_filme()
        elif op == 0:
            print("Saindo do Programa...")
            run_menu=False
        else:
            print("Valor Inválido.")
