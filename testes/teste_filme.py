import unittest

from logica import filme

class TestFilme(unittest.TestCase):

    def setUp(self):
        filme.remover_todos_filmes()
        
    def test_sem_filmes(self):
        filmes = filme.listar_filmes()
        self.assertEqual(0,len(filmes))

    def test_adicionar_um_filme(self):
        codigo = filme.adicionar_filme("It","terror",2017)

        filmes = filme.listar_filmes()
        self.assertEqual(1,len(filmes))
        self.assertEqual(1,codigo)

    def test_adicionar_dois_filmes(self):
        codigo1 = filme.adicionar_filme("It","terror",2017)
        codigo2 = filme.adicionar_filme("Mãe","terror",2017)

        filmes = filme.listar_filmes()
        self.assertEqual(2,len(filmes))
        self.assertEqual(1,codigo1)
        self.assertEqual(2,codigo2)

    def test_buscar_filme(self):
        codigo1 = filme.adicionar_filme("It","terror",2017)
        codigo2 = filme.adicionar_filme("Mãe","terror",2017)

        f = filme.buscar_filme(codigo2)
        self.assertEqual(codigo2,f[0])

    def test_buscar_filmes_por_genero(self):
        codigo1 = filme.adicionar_filme("It","terror",2017)
        codigo2 = filme.adicionar_filme("Mercenários","ação",2012)
        codigo3 = filme.adicionar_filme("Mãe","terror",2017)
        codigo4 = filme.adicionar_filme("Dora","aventura",2010)

        filmes = filme.buscar_filmes_por_genero("terror")
        f1 = filmes[0]
        f2 = filmes[1]
        self.assertEqual(codigo1,f1[0])
        self.assertEqual("It",f1[1])
        self.assertEqual(codigo3,f2[0])
        self.assertEqual("Mãe",f2[1])

    def test_remover_filme(self):
        codigo1 = filme.adicionar_filme("It","terror",2017)
        codigo2 = filme.adicionar_filme("Mercenários","ação",2012)
        codigo3 = filme.adicionar_filme("Mãe","terror",2017)

        filme.remover_filme(codigo2)

        f = filme.buscar_filme(codigo2)
        self.assertIsNone(f)

    def test_remover_todos_filmes(self):
        filme.adicionar_filme("It","terror",2017)
        filme.adicionar_filme("Mercenários","ação",2012)

        filme.remover_todos_filmes()
        filmes = filme.listar_filmes()
        self.assertEqual([],filmes)

    def test_iniciar_filmes(self):
        filme.iniciar_filmes()
        filmes = filme.listar_filmes()
        self.assertEqual(4,len(filmes))
        
if __name__ == "__main__":
    unittest.main(exit=False)
