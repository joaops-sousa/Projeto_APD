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

        usuario.iniciar_usuarios()
        filme.iniciar_filmes()
        
    def test_reproduzir_filme(self):
        r = reproducao.reproduzir_filme(111111,1)
        self.assertTrue(r)
    
if __name__ == "__main__":
    unittest.main(exit=False)
