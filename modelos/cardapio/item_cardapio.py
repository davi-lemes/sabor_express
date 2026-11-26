from abc import ABC, abstractmethod # importando um método nativo para criar uma classe abstrata

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass