# CREO UNA SUPER CLASSE
class Conto:
    def __init__(self, nome, conto):
        self.nome = nome
        self.conto = conto

# CREO LA CLASSE


class ContoCorrente(Conto):
    # DEFINISCO L'INIZIALIZZATORE RICHIAMANDO GLI ATTRIBUTI DALLA SUPER CLASSE
    def __init__(self, nome, conto, importo):
        super().__init__(nome, conto)
        # HO RESO PRIVATO L'ATTRIBUTO SALDO
        self.__saldo = importo
    # DEFINISCO UN METODO CHE HA LA FUNZIONE DI PRELEVARE I SOLDI DA IL SALDO

    def preleva(self, importo):
        self.__saldo -= importo
    # DEFINISCO UN METODO CHE HA LA FUNZIONE DI DEPOSITARE I SOLDI NEL SALDO

    def deposita(self, importo):
        self.__saldo += importo
    # DEFINISCO UN METODO CHE HA LA FUNZIONE DI DESCRIVERE NOME DELL INTESTATARIO , NUMERO DEL CONTO E IL SALDO TOTALE

    def descrizione(self):
        print("Conto numero:", self.conto, "\nUtente:",
              self.nome, "\nSaldo:", self.__saldo, "€")
        print(" ")

    # CREO UNA PROPERTY E GLI ATTRIBUISCO IL METODO GETTER
    @property
    def saldo(self):
        return self.__saldo

    # CREO UNA PROPERTY E GLI ATTRIBUISCO IL METODO SETTER
    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)
# CREO UNA NUOVA CLASSE , CHE ESEGUIRA UN METODO STATICO PER ESEGUIRE IN QUESTO CASO UN BONIFICO


class GestoreContiCorrenti:
    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)


# PROVO I VARI METODI CON I VARI ARGOMENTI
conto1 = ContoCorrente("Matt K Lawrence", "103748324", 67_000)
conto2 = ContoCorrente("Tommy K Lawrence", "245324045", 45_000)

# conto1.saldo = 10000000
# conto1.descrizione()
# print(" ")
# conto2.descrizione()
# print(" ")
# conto1.preleva(2000)
# conto1.deposita(10000)
# conto1.descrizione()
# conto2.preleva(1000)
# conto2.descrizione()

# print(conto1.saldo)

GestoreContiCorrenti.bonifico(conto1, conto2, 500)
conto1.descrizione()
conto2.descrizione()
