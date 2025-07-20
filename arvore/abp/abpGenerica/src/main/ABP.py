import re
from Arborizavel import Arborizavel
from NoTriplo import NoTriplo

class ABP(Arborizavel):
    def __init__(self):
        self.raiz = None

    def get_raiz(self):
        return self.raiz

    def limpar(self):
        self.raiz = None

    def inserir(self, dado):
        novo_no = NoTriplo(dado)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            atual = self.raiz
            while True:
                if dado <= atual.dado:
                    if atual.esquerda is None:
                        atual.esquerda = novo_no
                        novo_no.genitor = atual
                        break
                    atual = atual.esquerda
                else:
                    if atual.direita is None:
                        atual.direita = novo_no
                        novo_no.genitor = atual
                        break
                    atual = atual.direita

    def apagar(self, dado):
        nodo = self._buscar(dado)
        if nodo is None:
            return None

        if nodo.esquerda is None and nodo.direita is None:
            self._apagar_no_folha(nodo)
        elif nodo.esquerda is None or nodo.direita is None:
            self._apagar_com_um_filho(nodo)
        else:
            self._apagar_com_dois_filhos(nodo)

        return dado

    def _apagar_no_folha(self, nodo):
        pai = nodo.genitor
        if pai is None:
            self.raiz = None
        elif pai.esquerda == nodo:
            pai.esquerda = None
        else:
            pai.direita = None

    def _apagar_com_um_filho(self, nodo):
        avo = nodo.genitor
        neto = nodo.esquerda if nodo.esquerda else nodo.direita
        if avo is None:
            self.raiz = neto
            self.raiz.genitor = None
        elif avo.esquerda == nodo:
            avo.esquerda = neto
            neto.genitor = avo
        else:
            avo.direita = neto
            neto.genitor = avo

    def _apagar_com_dois_filhos(self, nodo):
        sucessor = self._encontra_menor_direita(nodo)
        nodo.dado = sucessor.dado
        if sucessor.esquerda is None and sucessor.direita is None:
            self._apagar_no_folha(sucessor)
        else:
            self._apagar_com_um_filho(sucessor)

    def _encontra_menor_direita(self, nodo):
        atual = nodo.direita
        while atual and atual.esquerda:
            atual = atual.esquerda
        return atual

    def _encontra_maior_esquerda(self, nodo):
        atual = nodo.esquerda
        while atual and atual.direita:
            atual = atual.direita
        return atual

    def existe(self, dado):
        return self._buscar(dado) is not None

    def _buscar(self, dado):
        atual = self.raiz
        while atual:
            if dado == atual.dado:
                return atual
            atual = atual.esquerda if dado <= atual.dado else atual.direita
        return None

    def imprimir_pre_ordem(self):
        return self._formata_saida(self._pre_ordem(self.raiz))

    def imprimir_em_ordem(self):
        return self._formata_saida(self._em_ordem(self.raiz))

    def imprimir_pos_ordem(self):
        return self._formata_saida(self._pos_ordem(self.raiz))

    def _pre_ordem(self, nodo):
        if nodo is None:
            return ""
        return f"{nodo.dado} {self._pre_ordem(nodo.esquerda)} {self._pre_ordem(nodo.direita)}"

    def _em_ordem(self, nodo):
        if nodo is None:
            return ""
        return f"{self._em_ordem(nodo.esquerda)} {nodo.dado} {self._em_ordem(nodo.direita)}"

    def _pos_ordem(self, nodo):
        if nodo is None:
            return ""
        return f"{self._pos_ordem(nodo.esquerda)} {self._pos_ordem(nodo.direita)} {nodo.dado}"

    def _formata_saida(self, msg):
        msg = re.sub(r"\s+", ",", msg.strip())
        return f"[{msg}]"