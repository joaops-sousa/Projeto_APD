import unittest

from logica import usuario

class TestUsuario(unittest.TestCase):

    def setUp(self):
        usuario.remover_todos_usuarios()
        
    def test_sem_usuarios(self):
        usuarios = usuario.listar_usuarios()
        self.assertEqual(0,len(usuarios))

    def test_adicionar_um_usuario(self):
        usuario.adicionar_usuario(111111,"Bob","bob@gmail.com","senha1")

        usuarios = usuario.listar_usuarios()
        self.assertEqual(1,len(usuarios))

        u = usuarios[0]
        self.assertEqual(111111,u[0])
        self.assertEqual("Bob",u[1])
        self.assertEqual("bob@gmail.com",u[2])
        self.assertEqual("senha1",u[3])

    def test_adicionar_dois_usuarios(self):
        usuario.adicionar_usuario(111111,"Bob","bob@gmail.com","senha1")
        usuario.adicionar_usuario(222222,"Julia","julia@gmail.com","senha2")
        usuarios = usuario.listar_usuarios()
        self.assertEqual(2,len(usuarios))

    def test_buscar_usuario(self):
        usuario.adicionar_usuario(111111,"Bob","bob@gmail.com","senha1")
        usuario.adicionar_usuario(222222,"Julia","julia@gmail.com","senha2")
        u = usuario.buscar_usuario(222222)
        self.assertEqual(222222,u[0])
        self.assertEqual("Julia",u[1])

    def test_remover_usuario(self):
        usuario.adicionar_usuario(111111,"Bob","bob@gmail.com","senha1")
        usuario.adicionar_usuario(222222,"Julia","julia@gmail.com","senha2")

        usuario.remover_usuario(111111)
        u = usuario.buscar_usuario(111111)
        self.assertIsNone(u)

    def test_remover_todos_usuarios(self):
        usuario.adicionar_usuario(111111,"Bob","bob@gmail.com","senha1")
        usuario.adicionar_usuario(222222,"Julia","julia@gmail.com","senha2")
        usuario.remover_todos_usuarios()
        u = usuario.listar_usuarios()
        self.assertEqual([],u)

    def test_iniciar_usuarios(self):
        usuario.iniciar_usuarios()
        usuarios = usuario.listar_usuarios()
        self.assertEqual(3,len(usuarios))

if __name__ == "__main__":
    unittest.main(exit=False)
