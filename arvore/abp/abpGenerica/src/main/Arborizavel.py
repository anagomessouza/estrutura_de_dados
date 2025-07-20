from abc import ABC, abstractmethod

class Arborizavel(ABC):
    @abstractmethod
    def get_raiz(self):
        """Retorna o nó raiz da árvore."""
        pass

    @abstractmethod
    def inserir(self, dado):
        """Insere um elemento na árvore."""
        pass

    @abstractmethod
    def apagar(self, dado):
        """Remove um elemento da árvore e retorna o dado removido, ou None se não encontrado."""
        pass

    @abstractmethod
    def existe(self, dado):
        """Verifica se um elemento existe na árvore."""
        pass

    @abstractmethod
    def limpar(self):
        """Remove todos os elementos da árvore."""
        pass

    @abstractmethod
    def imprimir_pre_ordem(self):
        """Retorna uma string com os elementos em pré-ordem."""
        pass

    @abstractmethod
    def imprimir_em_ordem(self):
        """Retorna uma string com os elementos em ordem."""
        pass

    @abstractmethod
    def imprimir_pos_ordem(self):
        """Retorna uma string com os elementos em pós-ordem."""
        pass