from reportlab.pdfgen import canvas
import time
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
    def __init__(self):
        self.pedidos=[]
        

    def total (self):
        total=0
        for pedido in self.pedidos:
           total += pedido.getPrecio()
        return total

    def add (self,vendible):
        self.pedidos.append(vendible)

    def getDescripcionPedidos(self):
        for pedido in self.pedidos:
            print(pedido.getDescripcion())

    def getPizza(self,indice):
        pedidos.get(indice)


class Cliente:
    def __init__(self):
        self.cedula =""
        self.nombre = ""
        self.direccion = ""

    def solicitarNombre(self):
        print("Por favor introduzca su nombre")
        self.nombre =input()

    def solicitarCedula(self):
        print("Por favor introduzca su cedula")
        self.cedula = input()

    def solicitarDireccion(self):
        print("Por favor introduzca su direccion")
        self.direccion = ""

    def imprimirFactura(self,pedido):
       
        c = canvas.Canvas("factura.pdf")
        c.setLineWidth(.3)
        c.setFont('Helvetica', 12)
 
        c.drawString(30,750,'FACTURA')
        c.drawString(30,735,'Tu Pizzeria Guatirence')
        c.drawString(485,750,time.strftime("%d:%m:%y -%I:%M:%S"))
        c.line(470,747,600,747)
 
        c.drawString(275,725,'ESTIMADO:')
        c.drawString(500,725,self.nombre)
        c.drawString(275,700,'CEDULA:')
        c.drawString(500,700,self.cedula)
        c.line(378,723,580,723)
        c.line(378,697,580,697)
 
        x = 30
        y = 653
        for pizza in pedido.pedidos:
            c.drawString(x,y,'Pizza:')
            c.line(x+90,y-3,x+550,y-3)
            c.drawString(x+90,y,pizza.getDescripcion())
            y = y - 20 
 
        c.save()

class AtencionUsuario:
    def __init__(self):
       
        self.pizza = PizzaMargarita()
        self.pedidos = Pedido()
        exit = False


       
        while not exit:
            print("Bienvenido a la pizzeria")
            print("Por favor seleccione un tamano para su pizza")
            print("Opciones:")
            print("Tamanos: Grande (g) Mediana (m) Personal (p)")
            self.SeleccionarTamano()
            print("Es momento de seleccionar los toppings")
            self.SeleccionarToppings()
            str = input("Desea Continuar [S/n]")
            if str == "s" or str == "S":
                self.pedidos.add(self.pizza)
            else:
                exit = True
                self.pedidos.add(self.pizza)
                self.pedidos.getDescripcionPedidos()
                print("PRECIO TOTAL : ",self.pedidos.total())
                cliente =Cliente()
                cliente.solicitarNombre()
                cliente.solicitarCedula()
                cliente.solicitarDireccion()
                cliente.imprimirFactura(self.pedidos)


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
            ingrediente = input()
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
        tamano = input()
        while not invalido:
            if tamano != "g" and tamano != "m" and tamano != "p":
                print("Tamano incorrecto, vuelva a seleccionar ")
                tamano = input()
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
