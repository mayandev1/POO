import requests
from PIL import Image
from io import BytesIO
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


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
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        
    def mostrar_imagem(self):
        
        resposta = requests.get(self._imagem)
        img = Image.open(BytesIO(resposta.content))
        
        plt.imshow(img)
        plt.axis("off")
        plt.savefig(f"{self._nome}.png")
        
        print("Imagem salva!")
        
    def mostrar_dados(self):
        
        print(f"Nome do pokémon: {self._nome}")    
        print(f"ID: {self._id}")    
        print(f"Altura: {self._altura}")    
        print(f"Peso: {self._peso}")
        print(f"Tipos: {', '.join(self._tipos)}")
            
            
# main

p1 = Pokemon("pikachu")
p1.mostrar_dados()
p1.mostrar_imagem()

p2 = Pokemon("blastoise")
p2.mostrar_dados()
p2.mostrar_imagem()

print(f"Total:", Pokemon.quantidade_pokemons)