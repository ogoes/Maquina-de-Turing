class Estado:
    def __init__(self, nome): ## classe, atributos e metodos de estados
        self.nome = nome
        self.inicial = False
        self.final = False

    def get_nome(self):
        return self.nome

    def is_final(self):
        return self.final

    def is_inicial(self):
        return self.inicial

    def set_inicial(self):
        self.inicial = True

    def set_final(self):
        self.final = True
