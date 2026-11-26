from modelos.avaliacao import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características"""

    restaurantes = []

    def __init__(self, nome, categoria):  # uma funcão definida para ser o método construtor da classe, utilizando o __init__. O self como parametro serve para dizer que os atributos irão para a instância que estamos na tratando no momento.
        """Inicializa uma instância de Restaurante
        
        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante
        """

        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False  # o _ mantém o atributo "ativo" privado, para sinalizar que é um atributo que não deve ser alterado
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):  # método que nos retorna o valor dos atributos em string para facilitar a visão do que foi atribuído no terminal.
        """Retorna uma representação em string do restaurante"""
        return f"{self._nome} | {self.categoria}"

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes"""
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}"
            )

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante"""
        return "✅" if self._ativo else "❌"

    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante"""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """Registra uma avaliação para o restaurante.
        
        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if nota >= 0 and nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante"""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media


# print(dir(restaurante_praca)) o dir mostra todos atributos e métodos de uma determinada instância
# print(vars(restaurante_praca)) o vars mostra apenas o estado atual da instância, não mostra os métodos e nem o que está sendo herdado da classe ou de heranças
