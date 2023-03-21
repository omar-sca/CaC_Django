
#1
def numeroMenor(num1, num2):
    if num1<=num2: return num1
    else: return num2

def maximoComunDivisor(num1, num2):
    for i in range(1,numeroMenor(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            mcm=i
    return  mcm

#print("mcd",maximoComunDivisor(9,18))


#2
def numeroMayor(num1, num2):
    if num1>=num2: return num1
    else: return num2

def minimoComunMultiplo(num1,num2):
    mcm=numeroMayor(num1,num2)
    while mcm%num1!=0 or mcm%num2!=0:
        mcm +=1
    return mcm

#print("mcm",minimoComunMultiplo(5,12))


#3
def cadenaADiccionario(cadena):
    listaKeys=cadena.split(" ")
    diccionario={}
    for key in listaKeys:
        if key in diccionario:
            diccionario[key] += 1
        else:
            diccionario[key]=1
    return diccionario

#cadenaADiccionario("Hola como estas como estas")


#4
def diccionarioATupla(dic):
    maximo=max(dic.values())
    
    for k,v in dic.items():
        if v==maximo:
            tupla=(k,v)
    return tupla

#print(diccionarioATupla(cadenaADiccionario("Hola como estas como estas")))


#5
def get_int_iterativa():
    fError=True
    while fError:
        try:
            fError=False
            valor=input()
            numero= int(valor)
        except ValueError as err:
            fError=True
        
    return numero

#get_int_iterativa()
    
def get_int_recursiva():
    try:
        valor=input()
        return int(valor)
    except ValueError as err:
        get_int_recursiva()

#get_int_recursiva()


#6
class Persona():
    def __init__(self, nombre="",edad="",DNI=""):
        self.__nombre=nombre
        self.__edad=edad
        self.__DNI=DNI

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def DNI(self):
        return self.__DNI

    @nombre.setter
    def nombre(self,valor):
        self.__nombre=valor

    @edad.setter
    def edad(self,valor):
        if type(valor)== int:
            self.__edad=valor
        else:
            return "La edad ingresada no es valida"

    @DNI.setter
    def DNI(self,valor):
        if type(valor)== int:
            self.__DNI=valor

    def es_mayor_de_edad(self):
        return self.__edad>=18
    
    def mostrar(self):
        return f"La persona {self.nombre} con DNI Nº: {self.DNI} tiene {self.edad} años."

'''
p1=Persona(nombre="Juan Perez",edad=50,DNI=123456)
p1.DNI= "hola"
print(p1.es_mayor_de_edad())
print(p1.mostrar())
'''


#7
class Cuenta():
    def __init__(self,titular,cantidad=0.0):
        self.__titular=titular
        self.__cantidad=cantidad
    
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        self.__titular = valor

    @property
    def cantidad(self):
        return self.__cantidad
   
    def mostrar(self):
        return f"Cuenta cuyo titular es {self.titular.nombre} y posee $ {self.cantidad}"

    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad
'''
c1 = Cuenta(p1)
c1.ingresar(10)
print(c1.mostrar())
'''


#8
class CuentaJoven(Cuenta):
    def __init__(self, titular, bonificacion,cantidad=0.0):
        super().__init__(titular,cantidad)
        self.__bonificacion=bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self,valor):
        self.__bonificacion=valor

    def es_titular_valido(self):
        if self.titular.es_mayor_de_edad and self.titular.edad<=25 :
            return True
        else:
            return False

    def retirar(self, cant):
        if self.es_titular_valido:
            super().retirar(cant)

    def mostrar(self):
        return f"Cuenta Joven con {self.bonificacion} % de bonificación"
'''
cj1= CuentaJoven(p1,20,50)
p1.edad=20
cj1.retirar(10)
print(cj1.cantidad)
print(cj1.mostrar())
'''
