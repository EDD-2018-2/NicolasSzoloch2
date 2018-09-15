# Lista elementos mas buscados
# Alumno: Nicolas Szoloch
"""Ejercicio 1
Se desea almacenar un conjunto de datos sobre una lista enlazada y se desea soportar búsquedas sobre dicho conjunto de datos. Se sabe que ciertos elementos del conjunto son buscados más frecuentemente que otros, y que la tendencia de búsqueda cambia con el tiempo, en el sentido que los elementos más frecuentemente consultados no necesariamente son los mismos en todo momento. Implemente una lista enlazada para permitir la búsqueda eficiente de los elementos más consultados. También debe soportar la inserción eficiente de nuevos elementos."""

class Elemento:
    def __init__(self, name, veces):
        self.nombre = name
        self.buscado = veces

    def __str__(self):
        return '{name} ha sido {buscado} veces buscado'.format(name=self.nombre, buscado = self.buscado)
    
class Lista:
    def __init__(self):
        self.contenedor = []
    
    def __str__(self):
        texto = '=== contenedor ===\n'
        for elm in self.contenedor:
            texto += elm.__str__() + '\n'
        return texto

    def agregar(self, ele):
        for it in self.contenedor:
            if it.nombre == ele.nombre:
                return False
        self.contenedor.append(ele)
        return True   

    def masBuscados(self):
        if not self.contenedor:
            return "NO Hay Datos"
        k=0
        text='=== Mas Buscados ===\n'
        for it in self.contenedor:
            if k < it.buscado:
                k=it.buscado
        for it in self.contenedor:
            if it.buscado==k:
                text += it.__str__() + '\n'
        return text

if __name__=="__main__":
    el_1 = Elemento('youtube.com', 5)
    el_2 = Elemento('facebook.com', 7)
    el_3 = Elemento('twitter.com', 9)
    el_4 = Elemento('sdafsd', 9)
    contenedor = Lista()
    contenedor.agregar(el_1)
    contenedor.agregar(el_2)
    print(contenedor)
    contenedor.agregar(el_3)
    contenedor.agregar(el_4)
    print(contenedor)
    print(contenedor.masBuscados())