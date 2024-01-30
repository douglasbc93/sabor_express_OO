from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')
# restaurante_mexicano.alternar_estado()

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()