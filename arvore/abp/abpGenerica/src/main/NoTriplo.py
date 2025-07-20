class NoTriplo:
    def __init__(self, dado=None):
        self._dado = dado
        self._genitor = None
        self._esquerda = None
        self._direita = None

    @property
    def dado(self):
        return self._dado

    @dado.setter
    def dado(self, valor):
        self._dado = valor

    @property
    def genitor(self):
        return self._genitor

    @genitor.setter
    def genitor(self, no):
        self._genitor = no

    @property
    def esquerda(self):
        return self._esquerda

    @esquerda.setter
    def esquerda(self, no):
        self._esquerda = no

    @property
    def direita(self):
        return self._direita

    @direita.setter
    def direita(self, no):
        self._direita = no