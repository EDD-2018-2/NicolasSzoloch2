# Recibe en Notacion Polaca, retorna valor algebraico
# Alumno: Nicolas Szoloch
"""Ejercicio 2
 Ejemplo notación polaca

(5 - 6) * 7 <=> * (- 5 6) 7
((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) <=> - * / 15 - 7 + 1 1 3 + 2 + 1 1 
"""
import operator

class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None
    def valor(self):
        return self.value

class Cola:
    def __init__(self):
        self.head = None
        self.last = None
    
    def __str__(self):
        texto = '=== cola numeros ===\n'
        if not self.head:
          return texto
        a = self.head
        texto += a.valor() + ' '
        while(a.next):
          a = a.next
          texto += a.valor() + ' '
        return texto

    def encolar(self, n):
        if not self.head:
          self.head = n
          self.last = n
        else:
          c = self.last
          c.next = n
          self.last = n

class Cola2:#Contiene los simbolos
    def __init__(self):
        self.head = None
        self.last = None
    
    def __str__(self):
        texto = '=== cola simbolos ===\n'
        if not self.head:
          return texto
        a = self.head
        texto += a.valor() + ' '
        while(a.next):
          a = a.next
          texto += a.valor() + ' '
        return texto

    def encolar(self, n):
        if not self.head:
          self.head = n
          self.last = n
        else:
          c = self.last
          c.next = n
          self.last = n

while(True):
  container = Cola()
  container2 = Cola2()
  x = input ("Inserte la expresion en Notacion Polaca: ")#Es un string
  a = x.split()#Separa los terminos recibidos por espacios
  for it in a:
    if it.isdigit():
      b = Nodo(it)
      container.encolar(b)
    elif (it=="*" or it=="/" or it=="-" or it=="+"):#Solo simbolos basicos, no parentesis
      b = Nodo(it)
      container2.encolar(b)
  print(container)
  print(container2)