class FlightData:
    def __init__(self, preco, aeroporto_origem, aeroporto_destino, data_ida, data_volta, escala=0):
        self.preco = preco
        self.aeroporto_origem = aeroporto_origem
        self.aeroporto_destino = aeroporto_destino
        self.data_ida = data_ida
        self.data_volta = data_volta
        self.escala = escala

    def __repr__(self):
        return (f"Voo(Preço: ${self.preco}, Origem: {self.aeroporto_origem}, "
                f"Destino: {self.aeroporto_destino}, Ida: {self.data_ida}, "
                f"Volta: {self.data_volta})")
