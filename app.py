from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_mexicano.alternar_estado()

restaurante_praca.receber_avaliacao('Douglas', 10)
restaurante_praca.receber_avaliacao('Daniel', 8)
restaurante_praca.receber_avaliacao('Tamara', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()