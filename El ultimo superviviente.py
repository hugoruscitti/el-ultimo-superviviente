# -*- encoding: utf-8 -*-
import pilasengine
pilas=pilasengine.iniciar()


class Pasto (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="Floor.png"
        self.y=-200
        self.x=-0
        self.imagen.repetir_horizontal= True


    def actualizar(self):
        self.x -=+0
        if self.x < -960:
            self.x= -0
    def mover(self):
        self.x -=+7
        if self.x < -960:
            self.x= -0
    def mover_i(self):
        self.x -=-7
        if self.x > 960:
            self.x= -0

class Soldado (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen=pilas.imagenes.cargar_grilla("correr.png",6)
        
        self.y=-150
        self.x=-150
        self.ir_izquierda=False
        self.ir_derecha=False
        self.saltando=False
        self.agachado=False
    def actualizar(self):
        self.imagen.avanzar(5)
        self.x -=+0
        if self.ir_izquierda:
            self.mover_fondo_i()
        if self.ir_derecha:
            self.mover_fondo()
    def mover_fondo(self):
        self.pasto.mover()
        self.fondo.mover()
    def mover_fondo_i(self):
        self.pasto.mover_i()
        self.fondo.mover_i()
    def agachar(self):
        self.imagen="agachado.png"
    def parar(self):
        self.imagen="corredor.png"
    def saltar(self):
        if not self.saltando:
            self.imagen="salto.png"
            self.hacer(Saltar)
class Saltar(pilasengine.comportamientos.Comportamiento):
    """Realiza un salto, cambiando los atributos 'y'."""

    def iniciar(self, receptor, velocidad_inicial=13, cuando_termina=None):
        """Se invoca cuando se anexa el comportamiento a un actor.

        :param receptor: El actor que comenzará a ejecutar este comportamiento.
        """
        super(Saltar, self).iniciar(receptor)
        self.velocidad_inicial = velocidad_inicial
        self.suelo = int(self.receptor.y)
        self.velocidad = self.velocidad_inicial
        receptor.saltando=True
    def actualizar(self):
        self.receptor.y += self.velocidad
        self.velocidad -= 1
        

        if self.receptor.y <= self.suelo:
            self.velocidad=0
            self.receptor.y =-150
            self.receptor.saltando=False
            self.receptor.parar()


class Zombie(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="zombies2.png"
        self.escala=0.7
        self.imagen=pilas.imagenes.cargar_grilla("zombies2.png",6)
    def actualizar(self):
        self.imagen.avanzar(5)
class Fondo (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="fondo.png"
        self.y=-20
        self.x=0
        self.escala=1.75
        self.imagen.repetir_horizontal= True


    def actualizar(self):
        self.x -=+0
        if self.x < -1400:
            self.x= -0
    def mover(self):
        self.x -=+2.50
        if self.x < -1400:
            self.x= -0
    def mover_i(self):
        self.x -=-2.50
        if self.x > 1400:
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
soldado.pasto=pasto
soldado.fondo=fondo


zombie=Zombie(pilas)

zombie.x=100
zombie.y=-130

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


actor=pilas.actores.Actor()
actor.imagen="escopeta.png"
actor.escala=2
actor.x=89
actor.y=143


actor2=pilas.actores.Actor()
actor2.imagen="minigun.png"
actor2.escala=1.6
actor2.x=184
actor2.y=145



actor3=pilas.actores.Actor()
actor3.imagen="granato.png"
actor3.escala=1.5
actor3.x=267
actor3.y=145



actor4=pilas.actores.Actor()
actor4.imagen="metra.png"
actor4.escala=1.5
actor4.x=-90
actor4.y=145


actor5=pilas.actores.Actor()
actor5.imagen="cuchillito.png"
actor5.escala=1.8
actor5.x=-270
actor5.y=145



actor6=pilas.actores.Actor()
actor6.imagen="pistol.png"
actor6.escala=1.3
actor6.x=-180
actor6.y=145



actor6=pilas.actores.Actor()
actor6.imagen="sniper.png"
actor6.escala=1.5
actor6.x=1
actor6.y=150






lista=[]
lista.append(bloque1)
lista.append(bloque2)
lista.append(bloque3)
lista.append(bloque4)
lista.append(bloque5)
lista.append(bloque6)
lista.append(bloque7)

def cuando_suelta_tecla(e):
    if e.codigo=="s":
        soldado.parar()
    if e.codigo=="a":
        soldado.ir_izquierda=False
    if e.codigo=="d":
        soldado.ir_derecha=False
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
    if e.codigo=="w":
        soldado.saltar()
    if e.codigo=="s":
        soldado.agachar()
        return
    if e.codigo=="d":
        soldado.ir_derecha=True
        soldado.ir_izquierda=False
        soldado.espejado=False
    if e.codigo=="a":
        soldado.ir_derecha=False
        soldado.ir_izquierda=True
        soldado.espejado=True

pilas.escena.suelta_tecla.conectar(cuando_suelta_tecla)
pilas.escena.pulsa_tecla.conectar(cuando_pulsa_tecla)
#1 cuchillo
#2 pistola
#3 metralleta
#4 sniper
#5 escopeta
#6 minigun
#7 granada
pilas.ejecutar()
