from logica import filme
from logica import reproducao
from logica import nota

def menu_adicionar():
    print("\nAdicionar Filme \n")
    titulo = str(input("Título: "))
    genero = str(input("Genero: ")).lower()
    ano = int(input("Ano: "))

    filme.adicionar_filme(titulo,genero,ano)

def imprimir_filme(filme):
    print("Código: ",filme[0])
    print("Título: ",filme[1])
    print("Genero: ",filme[2])
    print("Ano: ",filme[3])
    print()
 
def menu_listar():
    print("\nListar Filmes \n")
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)

def menu_buscar():
    print("\nBuscar Filme por Código \n")
    cod = int(input("Código: "))
    f = filme.buscar_filme(cod)
    if f == None:
        print("Filme não encontrado.")
    else:
        imprimir_filme(f)

def menu_buscar_filmes_por_genero():
    print("\nBuscar Filmes por Gênero \n")
    genero = str(input("Gênero: ")).lower()
    f = filme.buscar_filmes_por_genero(genero)
    if f == None:
        print("Não há filmes com esse gênero.")
    else:
        for i in f:
            imprimir_filme(i)

def menu_remover():
    print("\nRemover Filme \n")
    cod = int(input("Código: "))
    f = filme.remover_filme(cod)
    if f == False:
        print("Filme não encontrado.")
    else:
        print("Filme Removido.")

def menu_player():
    run_movie = True
    m = ("\n----------------\n"+
         "(0) Encerrar Filme \n"+
         "(1) Pausar Filme\n"+
         "----------------")

    while run_movie:
        print()
        print("Reproduzindo Filme...")
        print(m)
        comando = int(input("Digite o comando: "))

        if comando == 0:
            run_movie = False
            print("Filme encerrado.")
        elif comando == 1:
            print()
            print("Filme pausado.")
            c = input("Aperte enter para despausar.")
        else:
            print("Comando inválido")

def menu_reproduzir_filme():
    print("\nReproduzir Filme escolhido\n")
    cpf = int(input("CPF: "))
    codigo = int(input("Código Filme: "))

    ok = reproducao.reproduzir_filme(cpf,codigo)
    if ok == False:
        print("Dados não encontrados.")
    else:
        menu_player()
        print("\nAvalie o filme assistido \n")
        avaliacao = int(input("Nota (0 - 10): "))
        while avaliacao < 0 or avaliacao > 10:
            avaliacao = int(input("Nota inválida. Digite novamente: "))
        nota.avaliar_filme(cpf,codigo,avaliacao)
        print("\nObrigado pela avaliação.")

def exibir_menu_filme():
    run_filme = True
    menu = ("\n----------------\n"+
             "(1) Adicionar Filme \n" +
             "(2) Listar Filmes \n" +
             "(3) Buscar Filme por Código \n" +
             "(4) Buscar Filmes por Gênero \n" +
             "(5) Remover Filme \n"+
             "(6) Reproduzir Filme Escolhido \n"+
             "(0) Voltar\n"+
            "----------------")

    while run_filme:
        print(menu)

        op = int(input("Digite sua escolha: "))

        if op == 1:
            menu_adicionar()
        elif op == 2:
            menu_listar()
        elif op == 3:
            menu_buscar()
        elif op == 4:
            menu_buscar_filmes_por_genero()
        elif op == 5:
            menu_remover()
        elif op == 6:
            menu_reproduzir_filme()
        elif op == 0:
            run_filme = False
