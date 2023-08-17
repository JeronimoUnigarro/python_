class BilleteTren:
    def __init__(self, destino, precio):
        self.destino = destino
        self.precio = precio

class SistemaExpedicionBilletes:
    def __init__(self):
        self.destinos = {
            'A': BilleteTren('Destino A', 100),
            'B': BilleteTren('Destino B', 150),
            'C': BilleteTren('Destino C', 200),
        }
    
    def mostrar_menu(self):
        print("Bienvenido al sistema de expedición de billetes de tren")
        print("Destinos disponibles:")
        for clave, destino in self.destinos.items():
            print(f"{clave}: {destino.destino} - Precio: ${destino.precio}")
    
    def expedir_billete(self, destino, tarjeta_credito, pin):
        if destino in self.destinos:
            billete = self.destinos[destino]
            if self.validar_tarjeta_credito(tarjeta_credito, pin):
                print("Billete expedido:")
                print(f"Destino: {billete.destino}")
                print(f"Precio: ${billete.precio}")
                return True
            else:
                print("Tarjeta de crédito no válida. Transacción rechazada.")
        else:
            print("Destino no válido.")
        return False
    
    def validar_tarjeta_credito(self, tarjeta_credito, pin):
        # Implementación simplificada para fines de demostración.
        return tarjeta_credito.isdigit() and pin.isdigit()

def main():
    sistema = SistemaExpedicionBilletes()

    print("Presione el botón de inicio para comenzar.")
    input("Presione Enter para continuar...")

    while True:
        sistema.mostrar_menu()
        destino = input("Seleccione un destino (A/B/C): ")
        tarjeta_credito = input("Introduzca el número de tarjeta de crédito: ")
        pin = input("Introduzca su número de identificación personal (PIN): ")

        if sistema.expedir_billete(destino, tarjeta_credito, pin):
            break

if __name__ == "__main__":
    main()

