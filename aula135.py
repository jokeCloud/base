# mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando...')
            return

        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return

        print(f'{self.nome} está fotografando...')


canon = Camera('Canon')
sony = Camera('Sony')

canon.filmar()
canon.filmar()
canon.fotografar()
canon.parar_filmar()
canon.fotografar()

print()

sony.filmar()
sony.filmar()
sony.fotografar()
sony.parar_filmar()
sony.fotografar()

print(canon.filmando)
print(sony.filmando)
