class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Bruno Divino", "bruno.divino", "a")
usuario2 = Usuario("Camila Ferreira", "Mila", "a")
usuario3 = Usuario("Guilherme Louro", "Cake", "a")
usuario4 = Usuario("Jéssica França", "jessica.franca", "a")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2,
             usuario3.nickname : usuario3, 
             usuario4.nickname : usuario4}
