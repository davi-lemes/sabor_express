from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Davi Lemes', 6)
restaurante_praca.receber_avaliacao('Ana Dresch', 5)
restaurante_praca.receber_avaliacao('Pedro Lemes', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()