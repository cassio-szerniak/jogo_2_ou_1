class Jogos:
    def __init__(self, titulo, codigo, limite=10):
        self.titulo = titulo
        self.codigo = codigo
        self.limite = limite

    def menu(self):
        print("o que voce quer jogar?")
        print('1 - JOGAR 2 OU 1')
        print('2 - JOGAR ADIVINHE DE 1 A 10')
        print('0 - SAIR DO JOGO')
        jogar = input('--------------------------> ')
        jogar = int(jogar)
        if jogar == 1 or jogar == 2 or jogar == 0:
            if jogar == self.codigo:
                self.play()
            else:
                print('Saindo do jogo...\n')
                print("ate a proxima...")
        else:
            print("\nOpcao invalida! Tente novamente!\n")

    def play(self):
        print("estamos jogando", self.titulo)

jogo_dois_ou_um = Jogos('dois_ou_um', 1)
jogo_adivinha = Jogos('adivinha', 2, 6)



jogo_dois_ou_um.menu()