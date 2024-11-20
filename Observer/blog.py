

class Blog:
    def __init__(self):
        self.suscriptores = []

    def agregarSuscripor(self, suscriptor):
        self.suscriptores.append(suscriptor)

    def removerSuscripor(self, suscriptor):
        self.suscriptores.remove(suscriptor)

    def notificar_actualizacion(self, mensaje):

        for suscriptor in self.suscriptores:
            suscriptor.actualizar(mensaje)

    def publicar(self, titulo):
        print("Publicando nuevo articulo", titulo)
        self.notificar_actualizacion("Nuevo articulo publicado")