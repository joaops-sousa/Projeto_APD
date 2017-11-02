from logica import nota

def menu_listar_todas_notas():
    print("\nListar todas as notas \n")
    notas = nota.listar_avaliacoes()

    if len(notas) < 1:
        print("Não há notas disponíveis.")
    else:
        for n in notas:
            aux = ["CPF: " + str(n[0]),"Nome: "+str(n[1]),"Filme: "+n[3],"Nota:"+str(n[4])]
            for i in aux:
                print(i,end=" \t ")
            print()
def menu_listar_notas_por_filme():
    codigo = int(input("\nDigite o código do filme: "))
    notas = nota.listar_avaliacoes_por_filme(codigo)
    print()

    if notas == False:
        print("Filme não encontrado.")
    elif len(notas) < 1:
        print("Não há notas disponíveis para este filme.")
    else:
        for n in notas:
            aux = ["CPF: " + str(n[0]),"Nome: "+str(n[1]),"Filme: "+n[3],"Nota:"+str(n[4])]
            for i in aux:
                print(i,end=" \t ")

def exibir_menu_notas():
    run_notas = True
    menu = ("\n----------------\n"+
            "(1) Listar todas as Avaliações \n"+
            "(2) Listar Avaliações por Filme \n"+
            "(0) Voltar\n"+
            "----------------")

    while run_notas:
        print(menu)

        op = int(input("Digite sua escolha: "))

        if op == 1:
            menu_listar_todas_notas()
        elif op == 2:
            menu_listar_notas_por_filme()
        elif op == 0:
            run_notas = False
