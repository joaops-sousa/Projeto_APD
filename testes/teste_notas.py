import unittest

from logica import usuario
from logica import filme
from logica import nota

class TestNotas(unittest.TestCase):

    def setUp(self):
        usuario.remover_todos_usuarios()
        filme.remover_todos_filmes()
        nota.remover_todas_avaliacoes()

        usuario.iniciar_usuarios()
        filme.iniciar_filmes()
        
    def test_sem_notas(self):
        avaliacoes = nota.listar_avaliacoes()
        self.assertEqual(0,len(avaliacoes))

    def test_adicionar_uma_avaliacao(self):
        nota.avaliar_filme(111111,1,10)

        a = nota.listar_avaliacoes()
        self.assertEqual(1,len(a))
        self.assertEqual(111111,a[0][0])
        self.assertEqual(1,a[0][2])
        self.assertEqual(10,a[0][4])

    def test_adicionar_duas_avaliacoes(self):
        nota.avaliar_filme(111111,1,10)
        nota.avaliar_filme(111111,3,6)

        a = nota.listar_avaliacoes()
        self.assertEqual(2,len(a))

    def test_listar_avaliacoes_por_filme(self):
        nota.avaliar_filme(111111,1,10)
        nota.avaliar_filme(111111,3,6)
        nota.avaliar_filme(222222,3,10)

        a = nota.listar_avaliacoes_por_filme(3)

        a1 = a[0]
        a2 = a[1]

        self.assertEqual(a1[0],111111)
        self.assertEqual(a1[2],3)
        self.assertEqual(a1[4],6)
        self.assertEqual(a2[0],222222)
        self.assertEqual(a2[2],3)
        self.assertEqual(a2[4],10)

    def test_remover_todas_avaliacoes(self):
        nota.avaliar_filme(111111,1,10)
        nota.avaliar_filme(111111,3,6)
        nota.avaliar_filme(222222,3,10)

        nota.remover_todas_avaliacoes()

        a = nota.listar_avaliacoes()
        self.assertEqual([],a)

if __name__ == "__main__":
    unittest.main(exit=False)

     
