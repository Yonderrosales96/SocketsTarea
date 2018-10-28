class Vendible:
    def getDescripcion(self):
        return none
    def getPrecio(self):
        return none

class PizzaMargarita(Vendible):
    def getDescripcion(self):
        return "Pizza Margarita"
    def getPrecio(self):
        return 100

class Pasta (Vendible):
    def getDescripcion(self):
        return "Pasta con Salsa Napoli"
    def getPrecio(self):
        return 65

class Decorador(Vendible):
    def __init__ (self,vendible):
        self.vendible = vendible

class DecoradorTamano(Decorador):
    def __init__(self,vendible):
        Decorador.__init__(self,vendible)

class DecoradorIngrediente(Decorador):
    def __init__(self,vendible):
        Decorador.__init__(self,vendible)

class Jamon(DecoradorIngrediente):
    def __init__(self,vendible):
        DecoradorIngrediente.__init__(self,vendible)
    def getDescripcion(self):
        return self.vendible.getDescripcion() + " + Jamon"
    def getPrecio(self):
        return self.vendible.getPrecio() + 40

class Champinon(DecoradorIngrediente):
    def __init__(self,vendible):
        DecoradorIngrediente.__init__(self,vendible)
    def getDescripcion(self):
        return self.vendible.getDescripcion() + " + Champinon"
    def getPrecio(self):
        return self.vendible.getPrecio() + 35

class Pimenton(DecoradorIngrediente):
    def __init__(self,vendible):
        DecoradorIngrediente.__init__(self,vendible)
    def getDescripcion(self):
        return self.vendible.getDescripcion() + " + Pimenton"
    def getPrecio(self):
        return self.vendible.getPrecio() + 30

class DobleQueso(DecoradorIngrediente):
    def __init__(self,vendible):
        DecoradorIngrediente.__init__(self,vendible)
    def getDescripcion(self):
        return self.vendible.getDescripcion() + " + Doble queso"
    def getPrecio(self):
        return self.vendible.getPrecio() + 40

class Aceitunas(DecoradorIngrediente):
    def __init__(self,vendible):
        DecoradorIngrediente.__init__(self,vendible)
    def getDescripcion(self):
        return self.vendible.getDescripcion() + " + aceitunas"
    def getPrecio(self):
        return self.vendible.getPrecio() + 57.5

class Pepperoni(DecoradorIngrediente):
    def __init__(self,vendible):
        DecoradorIngrediente.__init__(self,vendible)
    def getDescripcion(self):
        return self.vendible.getDescripcion() + " + Pepperoni"
    def getPrecio(self):
        return self.vendible.getPrecio() + 38.5

class Salchichon(DecoradorIngrediente):
    def __init__(self,vendible):
        DecoradorIngrediente.__init__(self,vendible)
    def getDescripcion(self):
        return self.vendible.getDescripcion() + " + Salchichon"
    def getPrecio(self):
        return self.vendible.getPrecio() + 62.5


class Pequena(DecoradorTamano):
    def __init__ (self,vendible):
        DecoradorTamano.__init__(self,vendible)
    def getDescripcion(self):
        return self.vendible.getDescripcion() + " -- PEQUENA -- "
    def getPrecio(self):
        return self.vendible.getPrecio() + 50

class Mediana (DecoradorTamano):
    def __init__ (self,vendible):
        DecoradorTamano.__init__(self,vendible)
    def getDescripcion(self):
        return self.vendible.getDescripcion() + " -- MEDIANA -- "
    def getPrecio(self):
        return self.vendible.getPrecio() + 70

class Grande(DecoradorTamano):
    def __init__ (self,vendible):
        DecoradorTamano.__init__(self,vendible)
    def getDescripcion(self):
        return self.vendible.getDescripcion() + " -- GRANDE -- "
    def getPrecio(self):
        return self.vendible.getPrecio() + 100


class Pedido:
    def __init__(self,vendible):
        self.pedidos=[]
        self.pedidos.append(vendible)

    def total (self):
        total=0
        for pedido in self.pedidos:
           total += pedido.getPrecio()
        return total

    def add (self,vendible):
        self.pedidos.append(vendible)

    def getDescripcionPedidos(self):
        for pedido in self.pedidos:
            print( pedido.getDescripcion())

pedidos = Pedido(Pequena(Salchichon(Jamon(PizzaMargarita()))))


class AtencionUsuario:
    def __init__(self):
        self.pedidos = []
        self.pizza = PizzaMargarita()
        print("Bienvenido a la pizzeria")
        print("Por favor seleccione un tamano para su pizza")
        print("Opciones:")
        print("Tamanos: Grande (g) Mediana (m) Personal (p)")
        self.SeleccionarTamano()
        print("Es momento de seleccionar los toppings")
        self.SeleccionarToppings()


    def SeleccionarToppings(self):
        print("Ingredientes:")
        print("jamon (ja)")
        print("pimenton (pi)")
        print("champinon (ch)")
        print("Doble Queso (dq)")
        print("Aceitunas (ac)")
        print("Pepperoni (pe)")
        print("Salchichon (sa)")
        salir = False
        while not salir:
            print("Indique el ingrediente que desea (enter para terminar)")
            ingrediente = raw_input()
            if ingrediente == "ja":
                print("Ha seleccionado jamon")
                self.pizza = Jamon(self.pizza)
            elif ingrediente == "pi":
                print("Ha seleccionado Pimenton")
                self.pizza = Pimenton(self.pizza)
            elif ingrediente == "ch":
                print("Ha seleccionado champinon")
                self.pizza = Champinon(self.pizza)
            elif ingrediente == "dq":
                print("Ha seleccionado doble queso")
                self.pizza = DobleQueso(self.pizza)
            elif ingrediente == "ac":
                print("Ha seleccionado aceitunas")
                self.pizza = Aceitunas(self.pizza)
            elif ingrediente == "pe":
                print("Ha seleccionado Pepperoni")
                self.pizza = Pepperoni(self.pizza)
            elif ingrediente == "sa":
                print("Ha seleccionado salchichon")
                self.pizza = Salchichon(self.pizza)
            elif ingrediente == "":
                print(self.pizza.getDescripcion())
                print(self.pizza.getPrecio())
                salir = True
            else:
                print("Por favor seleccione un ingrediente de la lista")




    def SeleccionarTamano(self):
        invalido = False
        tamano = raw_input()
        while not invalido:
            if tamano != "g" and tamano != "m" and tamano != "p":
                print("Tamano incorrecto, vuelva a seleccionar ")
                tamano = raw_input()
            else:
                invalido = True
        if tamano =="g":
            print("Ha seleccionado pizza grande")
            self.pizza = Grande(PizzaMargarita())
        elif tamano == "m":
            print("Ha seleccionado pizza mediana")
            self.pizza = Mediana(PizzaMargarita())
        elif tamano == "p":
            print("Ha seleccionado pizza pequena")
            self.pizza = Pequena(PizzaMargarita())


AtencionUsuario()
