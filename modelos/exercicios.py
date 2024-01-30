# ## Mão na Massa 1:
# class Musica():
#     nome = ''
#     artista = ''
#     duracao = int

# musica1 = Musica()
# musica1.nome = 'Shadow Moses'
# musica1.artista = 'Bring Me The Horizon'
# musica1.duracao = 255

# musica2 = Musica()
# musica2.nome = 'Perfect Machine'
# musica2.artista = 'Starset'
# musica2.duracao = 323

# musica3 = Musica()
# musica3.nome = 'Snuff'
# musica3.artista = 'Slipknot'
# musica3.duracao = 276

# print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')

# ## Exercícios 01.Classes: 
# #1:
# class Restaurante():
#     nome = ''
#     categoria = ''
#     ativo = False

# restaurante_praca = Restaurante()
# restaurante_praca.nome = 'Praça'
# restaurante_praca.categoria = 'Italiana'

# #2:
# nome_do_restaurante = restaurante_praca.nome

# #3:
# if restaurante_praca.ativo == True:
#     print(f'O restaurante {restaurante_praca.nome} está ativo')
# else:
#     print(f'O restaurante {restaurante_praca.nome} não está ativo')

# #4:
# categoria = Restaurante.categoria

# #5:
# restaurante_praca.nome = 'Bistrô'

# #6:
# restaurante_pizza = Restaurante()
# restaurante_pizza.nome = 'Pizza Place'
# restaurante_pizza.categoria = 'Fast Food'

# #7:
# if restaurante_pizza.categoria == 'Fast Food':
#     print('A categoria é Fast Food.')
# else:
#     print('A categoria não é Fast Food.')

# #8:
# restaurante_pizza.ativo = True

# #9:
# print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')


# ## Mão na Massa 2:
# class Musica:
#     def __init__(self, nome='', artista='', duracao=0):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao

# musica1 = Musica(nome='Shadow Moses', artista='Bring Me The Horizon', duracao=255)
# musica2 = Musica(nome='Perfect Machine', artista='Starset', duracao=323)
# musica3 = Musica(nome='Snuff', artista='Slipknot', duracao=276)

# ## Exercícios 02.Construtor e instanciando objetos: 
# #1: 
# class Carro:
#     def __init__(self, modelo, cor, ano):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano

# carro1 = Carro(modelo='Corolla', cor='Preto', ano=2023)

# #2:
# class Restaurante:
#     def __init__(self, nome, categoria, bairro, faixa_preco, ativo=False):
#         self.nome = nome
#         self.categoria = categoria
#         self.bairro = bairro
#         self.faixa_preco = faixa_preco
#         self.ativo = ativo

# restaurante1 = Restaurante(nome='RestauranteTeste', categoria='Brasileiro', bairro='Tijuca', faixa_preco='Barato', ativo=True)

# #3: 
# class Restaurante2:
#     def __init__(self, nome, categoria, ativo, bairro, faixa_preco):
#         self.nome = nome
#         self.categoria = categoria
#         self.bairro = bairro
#         self.faixa_preco = faixa_preco
#         self.ativo = False

# #restaurante2 = Restaurante2(nome='RestauranteTeste2', categoria='Italiano')

# #4:
#     def __str__(self):
#         return f'{self.nome} | {self.categoria}'

# restaurante3 = Restaurante2(nome='RestauranteTeste2', categoria='Italiano', bairro='Bangu', faixa_preco='Caro', ativo=True)
# print(restaurante3)

# #5:
# class Cliente:
#     def __init__(self, nome='', idade=0, estado='', banco=''):
#         self.nome = nome
#         self.idade = idade
#         self.estado = estado
#         self.banco = banco

# cliente1 = Cliente(nome='Douglas', idade=30, estado='RJ', banco='Bradesco')
# cliente2 = Cliente(nome='Tamara', idade=32, estado='RJ', banco='Santander')
# cliente3 = Cliente(nome='Daniel', idade=21, estado='RJ', banco='Nubank')


# ## Mão na Massa 3:

# class Pessoa:
#     def __init__(self, nome='', idade=0, profissao=''):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao
    
#     def __str__(self):
#         return f'{self.nome}, {self.idade} anos, {self.profissao}'
 
#     @property
#     def saudacao(self):
#         if self.profissao:
#             return f'Olá, meu nome é {self.nome} e sou {self.profissao}'
#         else:
#             return f'Olá, sou {self.nome}!'
           
#     def aniversario(self):
#         self.idade += 1


# pessoa1 = Pessoa(nome='Douglas', idade=30, profissao='estudante')
# pessoa2 = Pessoa(nome='Daniel', idade=21, profissao='estudante')
# pessoa3 = Pessoa(nome='Tamara', idade=32)

# print()
# print('Informações iniciais:')
# print(pessoa1)
# print(pessoa2)
# print(pessoa3)
# print()

# pessoa1.aniversario()
# pessoa3.aniversario()

# print('Informações após aniversário:')
# print(pessoa1)
# print(pessoa3)
# print()

# print(pessoa1.saudacao)
# print()

# ## Exercícios 03.Property e métodos de classe: 
# #1:
# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
#         self._ativo = False
# #2:    
#     def __str__(self):
#         return f'Titular: {self.titular} - Saldo: {self.saldo}'
# #3:
#     @classmethod
#     def ativar_conta(cls, conta):
#         conta._ativo = True
    
# conta1 = ContaBancaria("Douglas", 500)
# conta2 = ContaBancaria("Daniel", 600)

# print(conta1)
# print(conta2)

# conta3 = ContaBancaria("Tamara", 700)
# print(f'Antes da ativação, conta ativa? {conta3._ativo}')

# ContaBancaria.ativar_conta(conta3)
# print(f'Após ativação, conta ativa? {conta3._ativo}')

# #4:
# class ContaBancariaPythonica:
#     def __init__(self, titular, saldo):
#         self._titular = titular
#         self._saldo = saldo
#         self._ativo = False

#     @property
#     def titular(self):
#         return self._titular

#     @property
#     def saldo(self):
#         return self._saldo

#     @property
#     def ativo(self):
#         return self._ativo
# #5:
# conta4 = ContaBancaria("Fernanda", 1500)
# print(f'Titular da conta 4: {conta4.titular}')

# #6:
# class ClienteBanco:
#     def __init__(self, nome, idade, tipo, numero, saldo):
#         self.nome = nome
#         self.idade = idade
#         self.tipo = tipo
#         self.numero = numero
#         self.saldo = saldo
# #7:
#     @classmethod
#     def criar_conta(cls, titular, saldo_inicial):
#         conta = ContaBancariaPythonica(titular, saldo_inicial)
#         return conta
    
# cliente1 = ClienteBanco("Douglas", 30, "Corrente", "123", 100)
# cliente2 = ClienteBanco("Daniel", 21, "Corrente", "456", 200)
# cliente3 = ClienteBanco("Tamara", 32, "Poupança", "789", 300)

# #7.2:
# cliente4 = ClienteBanco.criar_conta("Ana", 2000)
# print(f'Conta de {cliente4.titular} criada com saldo inicial de R$ {cliente4.saldo}')

# ## Exercícios 04.Importante classe e composição:
# #1:
# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         self.disponivel = True
# #2:
#     def __str__(self):
#         return f'Livro: {self.titulo} - Autor: {self.autor} - Ano de publicação: {self.ano_publicacao}'
# #3:
#     def emprestar(self):
#         self.disponivel = False
# #4:
#     @staticmethod
#     def verificar_disponibilidade(ano):
#         livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]

#         if livros_disponiveis:
#             livros_disponiveis_str = ", ".join(livro.__str__() for livro in livros_disponiveis)
#         else:
#             livros_disponiveis_str = "Nenhum livro disponível"

#         return livros_disponiveis_str

# livro1 = Livro("LivroTeste1", "Douglas", 2023)
# livro2 = Livro("LivroTeste2", "Tamara", 2022)
# print(livro1)
# print(livro2)

# print(f'Livro 1 está disponível? {livro1.disponivel}')
# livro1.emprestar()
# print(f'Livro 1 está disponível? {livro1.disponivel}')

# Livro.livros = [livro1, livro2]