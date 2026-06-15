import requests
from PIL import Image
from io import BytesIO

class Pokemon:
    
    quantidade_pokemons = 0
    __slots__ = (
        "_nome",
        "_id",
        "_altura",
        "_peso",
        "_tipos",
        "_imagem",
    )
    
    def __init__(self, pokemon):
        self.buscar_pokemon(pokemon)
        Pokemon.quantidade_pokemons += 1
              
    def buscar_pokemon(self, pokemon):    
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

        resposta = requests.get(url)
        
        if resposta.status_code != 200:
            raise ValueError("Pokémon não encontrado!") 
    
        dados = resposta.json()
        self._nome = dados["name"]
        self._altura = dados["height"]
        self._id = dados["id"]
        self._peso = dados["weight"]
        self._tipos = [
            tipo["type"]["name"]
            for tipo in dados["types"]
        ]
        self._imagem = dados["sprites"]["front_default"]
    
    @staticmethod
    def quantidade():
        return Pokemon.quantidade_pokemons
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        
    def mostrar_imagem(self):
        
        resposta = requests.get(self._imagem)
        img = Image.open(BytesIO(resposta.content))
        
        img.show()
        
    def mostrar_dados(self):
        
        print("\n --------------- DADOS ---------------")
        print(f"Nome do pokémon: {self._nome}")    
        print(f"ID: {self._id}")    
        print(f"Altura: {self._altura}")    
        print(f"Peso: {self._peso}")
        print(f"Tipos: {', '.join(self._tipos)}")
            

pokedex = []

def menu():
    print("\n----- POKEDEX -----")
    print("1 - Consultar e cadastrar Pokémon")
    print("2 - Listar Pokémons cadastrados")
    print("3 - Exibir dados de um Pokémon")
    print("4 - Exibir imagem de um Pokémon")
    print("5 - Mostrar quantidade de Pokémons cadastrados")
    print("0 - Sair")
    
def cadastrar():
    
    nome = input("Digite o nome ou ID: ")
    
    try:
        pokemon = Pokemon(nome)
        pokedex.append(pokemon)
        print("Pokémon cadastrado!")
    except:
        print("Pokémon não cadastrado!")

def listar_pokemons():
    if not pokedex:
        print("Nenhum pokémon cadastrado.")
        return False
    
    for i, pokemon in enumerate(pokedex):
        print(f"{i} - {pokemon.nome}")
        
    return True

def mostrar_dados():
    
    if listar_pokemons():
        
        indice = int(input("Escolha o índice: "))
        pokedex[indice].mostrar_dados()
        
def mostrar_imagem():
    
    if listar_pokemons():
        indice = int(input("Escolha o índice: "))
        pokedex[indice].mostrar_imagem()


def mostrar_quantidade():
    total = Pokemon.quantidade()
    print(f"Total de pokémons cadastrados: {total}")
            
# MAIN POKEDEX

while True:
    
    menu()
    opcao = int(input("Escolha uma opção: "))
    
    match(opcao):
        case 1:
            cadastrar()
        case 2:
            listar_pokemons()
        case 3: 
            mostrar_dados()
        case 4:
            mostrar_imagem()
        case 5:
            mostrar_quantidade()
        case 0:
            print("Encerrando pokedex...")
            break
        case _:
            print("Opção inválida xará!")