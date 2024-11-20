
class SuscriptorEmail:
    def __init__(self, email):
        self.email = email

    def actualizar(self, mensaje):
        print(f"Enviando notificacion a {self.email}")
        print(mensaje)

class SuscriptorSMS:
    def __init__(self, numero):
        self.numero = numero

    def actualizar(self, mensaje):
        print(f"Enviando notificacion a {self.numero}")
        print(mensaje)
        