class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = ""

        if self.tipo.lower() == "mago":
            ataque = "magia"
        elif self.tipo.lower() == "guerreiro":
            ataque = "espada"
        elif self.tipo.lower() == "monge":
            ataque = "artes marciais"
        elif self.tipo.lower() == "ninja":
            ataque = "shuriken"
        else:
            ataque = "um ataque misterioso"

        print(f"o {self.tipo} atacou usando {ataque}")

heroi1 = Heroi("Arthur", 30, "guerreiro")
heroi2 = Heroi("Merlin", 150, "mago")
heroi3 = Heroi("Lee", 25, "monge")
heroi4 = Heroi("Hanzo", 28, "ninja")


lista_de_herois = [heroi1, heroi2, heroi3, heroi4]
print("--- Iniciando a Batalha ---")
for personagem in lista_de_herois:
    personagem.atacar()