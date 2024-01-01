class TableroAjedrez:
    def __init__(self):
        self.tablero = []

    def new_tablero(self):
        self.tablero = [[' ' for _ in range(8)] for _ in range(8)]

    def imprimir_tablero(self):
        for fila in self.tablero:
            print("|".join(fila))
            print("---------")

if __name__ == "__main__":
    tablero_ajedrez = TableroAjedrez()
    tablero_ajedrez.new_tablero()
    tablero_ajedrez.imprimir_tablero()