import unittest

from logica import usuario
from logica import filme
from logica import historico
from logica import reproducao

class TestReproducao(unittest.TestCase):

    def setUp(self):
        usuario.remover_todos_usuarios()
        filme.remover_todos_filmes()
        historico.remover_todos_historicos()
        reproducao.remover_todas_avaliacoes()

        usuario.iniciar_usuarios()
        filme.iniciar_filmes()
        
    def test_reproduzir_filme(self):
        r = reproducao.reproduzir_filme(111111,1)
        self.assertTrue(r)

    def test_avaliar_um_filme(self):
        reproducao.avaliar_filme(111111,1,10)

        r = reproducao.listar_avaliacoes()
        self.assertEqual(1,len(r))
        self.assertEqual(111111,r[0][0])
        self.assertEqual(1,r[0][2])
        self.assertEqual(10,r[0][4])

    def test_avaliar_dois_filmes(self):
        reproducao.avaliar_filme(111111,1,10)
        reproducao.avaliar_filme(111111,3,6)

        r = reproducao.listar_avaliacoes()
        self.assertEqual(2,len(r))

    def test_listar_avaliacoes_por_cpf(self):
        reproducao.avaliar_filme(111111,1,10)
        reproducao.avaliar_filme(111111,3,6)
        reproducao.avaliar_filme(222222,3,10)

        r = reproducao.listar_avaliacoes_por_cpf(111111)
        a1 = r[0]
        a2 = r[1]
        self.assertEqual(2,len(r))
        self.assertEqual(a1[0],111111)
        self.assertEqual(a1[2],1)
        self.assertEqual(a1[4],10)
        self.assertEqual(a2[0],111111)
        self.assertEqual(a2[2],3)
        self.assertEqual(a2[4],6)

    def test_remover_todas_avaliacoes(self):
        reproducao.avaliar_filme(111111,1,10)
        reproducao.avaliar_filme(111111,3,6)
        reproducao.avaliar_filme(222222,3,10)

        reproducao.remover_todas_avaliacoes()

        r = reproducao.listar_avaliacoes()
        self.assertEqual([],r)
    
if __name__ == "__main__":
    unittest.main(exit=False)
