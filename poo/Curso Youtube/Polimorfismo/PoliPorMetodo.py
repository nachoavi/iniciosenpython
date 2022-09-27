#Polimorfismo con metodo

class Chile:
    def capital(self):
        print("Capital de Chile: Santiago")
    def idioma(self):
        print("Idioma: Español")

class Francia:
    def capital(self):
        print("\nCapital de Francia: Paris")
    def idioma(self):
        print("Idioma: Frances")

chileno = Chile()
frances = Francia()

for pais in (chileno,frances):
    pais.capital()
    pais.idioma()