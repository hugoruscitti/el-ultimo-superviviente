import pilasengine
pilas=pilasengine.iniciar()


class Pasto (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="Floor.png"
        self.y=-200
        self.x=-0
        self.imagen.repetir_horizontal= True
        
        
    def actualizar(self):
        self.x -=+2
        if self.x < -960:
            self.x= -0        
            
class Soldado (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="corredor.png"
        self.y=-150
        self.x=-150
        
class Fondo (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="fondo.png"
        self.y=-20
        self.x=0
        self.escala=1.75
        self.imagen.repetir_horizontal= True
        
        
    def actualizar(self):
        self.x -=+0.2
        if self.x < -1400:
            self.x= -0
class Bloque (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="bloque.png"
        self.y=150
        self.x=-50 
        self.sonido=pilas.sonidos.cargar("pop.wav")

    def seleccionar(self):
        self.sonido.reproducir()
        self.imagen="bloque_naranja.png"
    def deshacer(self):
        self.imagen="bloque.png"
        

fondo=Fondo(pilas)        
pasto=Pasto(pilas)
bloque1=Bloque(pilas)
bloque2=Bloque(pilas)
bloque3=Bloque(pilas)
bloque4=Bloque(pilas)
bloque5=Bloque(pilas)
bloque6=Bloque(pilas)
bloque7=Bloque(pilas)
soldado=Soldado(pilas)
dist=90
bloque7.x=dist*3
bloque7.escala=0.5
bloque6.x=dist*2
bloque6.escala=0.7
bloque5.x=dist*1
bloque5.escala=0.84
bloque4.x=dist*0
bloque4.seleccionar()
bloque3.x=dist*-1
bloque3.escala=0.84
bloque2.x=dist*-2
bloque2.escala=0.7
bloque1.x=dist*-3
bloque1.escala=0.5
bloque_seleccionado=3

lista=[]
lista.append(bloque1)
lista.append(bloque2)
lista.append(bloque3)
lista.append(bloque4)
lista.append(bloque5)
lista.append(bloque6)
lista.append(bloque7)

def cuando_pulsa_tecla(e):
    global bloque_seleccionado
    global lista
    if e.codigo=="e":
        bloque_seleccionado+=1
        if bloque_seleccionado>6:
            bloque_seleccionado=6

        for x in lista:
            x.deshacer()
        lista[bloque_seleccionado].seleccionar()
    if e.codigo=="q":
        bloque_seleccionado-=1
        if bloque_seleccionado<0:
            bloque_seleccionado=0         

        for x in lista:
            x.deshacer()
        lista[bloque_seleccionado].seleccionar()
            
            
            
pilas.escena.pulsa_tecla.conectar(cuando_pulsa_tecla)
#1 cuchillo
#2 pistola
#3 metralleta
#4 sniper
#5 escopeta
#6 bazuca
#7 granada
pilas.ejecutar()
