from observer import Observador
from blog import Blog
from suscriptor import SuscriptorEmail, SuscriptorSMS

## Enunciado

# Implementa un sistema de notificaciones de un blog.  Define un ainterfaz observador con un metodo "actualizar(String mensaje)". 
# Luego crea una clase Blog que mantenga una lista de observadores y notifique a todos lo observadores cuando se publique un nevo articulo
# FInalmente, crea las clases concretas que implementan la interfaz Observador para diferentes tipos de suscriptores, como "SuscriptorEmail" y "SuscriptorSMS"

# Crear un blog
mi_blog = Blog()

# Crear observadores
suscriptor1 = SuscriptorEmail("sofi@sofisoler.com.ar")
suscriptor2 = SuscriptorSMS("+123456789")

    # Suscribir observadores al blog
mi_blog.agregarSuscripor(suscriptor1)
mi_blog.agregarSuscripor(suscriptor2)


# Publicar un artículo
mi_blog.publicar("Como programar?")


mi_blog.removerSuscripor(suscriptor2)

# Publicar otro artículo
mi_blog.publicar("Consejos de jardinería")

