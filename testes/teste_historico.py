import unittest

from logica import historico
from logica import usuario
from logica import filme

class TestHistorico(unittest.TestCase):

    def setUp(self):
        historico.remover_todos_historicos()
        usuario.remover_todos_usuarios()
        filme.remover_todos_filmes()

        usuario.iniciar_usuarios()
        filme.iniciar_filmes()
    def test_sem_filmes_assistidos(self):
        filmes_assistidos = historico.listar_historico_geral()
        self.assertEqual(0,len(filmes_assistidos))

    def test_registrar_um_filme_assistido(self):
        historico.registrar_filme_assistido(1,111111)

        hist = historico.listar_historico_geral()
        user = hist[0][0]
        movie = hist[0][1]
        self.assertEqual(1,len(hist))
        self.assertEqual(111111,user[0])
        self.assertEqual(1,movie[0])

    def test_registrar_dois_filmes_assistidos(self):
        historico.registrar_filme_assistido(1,111111)
        historico.registrar_filme_assistido(2,111111)

        hist = historico.listar_historico_geral()
        self.assertEqual(2,len(hist))

    def test_listar_filmes_assistidos(self):
        historico.registrar_filme_assistido(1,111111)
        historico.registrar_filme_assistido(1,222222)
        historico.registrar_filme_assistido(2,111111)

        filmes_assistidos = historico.listar_filmes_assistidos(111111)
        f1 = filmes_assistidos[0]
        f2 = filmes_assistidos[1]
        self.assertEqual(1,f1[0])
        self.assertEqual(2,f2[0])

    def test_limpar_historico(self):
        historico.registrar_filme_assistido(1,111111)
        historico.registrar_filme_assistido(1,222222)
        historico.registrar_filme_assistido(2,111111)

        historico.limpar_historico(111111)
        filmes_assistidos = historico.listar_filmes_assistidos(111111)
        self.assertIsNone(filmes_assistidos)
        

    def test_remover_todos_historicos(self):
        historico.registrar_filme_assistido(1,111111)
        historico.registrar_filme_assistido(1,222222)
        historico.registrar_filme_assistido(2,111111)

        historico.remover_todos_historicos()

        hist = historico.listar_historico_geral()

        self.assertEqual([],hist)
        
if __name__ == "__main__":
    unittest.main(exit=False)
