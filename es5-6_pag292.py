# consegna 11/03/21: elenca proprietà e metodi della classe prodotto e definisci il metodo assegna_prezzo
class prodotto():
    def __init__(self, nome, colore, categoria):
        self.nome = nome
        self.colore = colore
        self.categoria = categoria
    def assegna_prezzo(self, prezzo):
        self.prezzo = prezzo
        print("Prezzo:", self.prezzo)
    def info(self):
    	print("Il prodotto si chiama:", self.nome, "\nDi colore:", self.colore, 
        "\nAppartiene alla categoria:", self.categoria)

prodotto = prodotto("Q&P", "viola", "alimenti")
prodotto.info()
prodotto.assegna_prezzo("15€")