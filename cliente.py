

class cliente:
    def __init__(self, nome):
        self.nome = nome

    @property
    def get_nome(self):
        print("Chamando property nome")
        return self.__nome.title()

    def nome(self, nome):
        print("Chamando o setter nome")
        self.__nome = nome