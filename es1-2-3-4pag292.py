'''
1. Crea una classe atleta per rappresentare le informazioni su un giocatore la classe deve contenere 
un attributo booleano chiamato visita_medica
2. Aggiungi alla classe atleta un metodo per assegnare l'atleta il nome della squadra dove gioca
3. Aggiungi alla classe atleta un metodo di chiamato effettua_visita che ponga l'attributo a True
4. Aggiungi alla classe atleta un metodo per visualizzare i dati del giocatore
'''
class atleta():
    def __init__(self, nome, cognome, visita, squadra):
        self.nome = nome
        self.cognome = cognome
        self.visita = visita
        self.squadra = squadra
    def effettua_visita(self) :
    	self.visita = True
    def info(self):
    	print("L'atleta si chiama", self.nome, self.cognome,"\nVisita medica:",
         self.visita, "\nGioca nella squadra:", self.squadra)
    	
atleta = atleta("Maria", "Gianfranca", False, "Fragola" )
atleta.info()
atleta.effettua_visita()
atleta.info()
