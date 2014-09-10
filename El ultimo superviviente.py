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
        self.imagen="corredor.png"
        self.y=-150
        self.x=-150
    def actualizar(self):
        self.x -=+0
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
        self.imagen="salto.png"

class Saltar(pilasengine.comportamientos.Comportamiento):
    """Realiza un salto, cambiando los atributos 'y'."""

    def iniciar(self, receptor, velocidad_inicial=10, cuando_termina=None):
        """Se invoca cuando se anexa el comportamiento a un actor.

        :param receptor: El actor que comenzará a ejecutar este comportamiento.
        """
        super(Saltar, self).iniciar(receptor)
        self.velocidad_inicial = velocidad_inicial
        self.cuando_termina = cuando_termina
        self.sonido_saltar = self.pilas.sonidos.cargar("audio/saltar.wav")
        self.suelo = int(self.receptor.y)
        self.velocidad = self.velocidad_inicial
        self.sonido_saltar.reproducir()
        self.velocidad_aux = self.velocidad_inicial

    def actualizar(self):
        self.receptor.y += self.velocidad
        self.velocidad -= 0.3

        if self.receptor.y <= self.suelo:
            self.velocidad_aux /= 2.0
            self.velocidad = self.velocidad_aux

            if self.velocidad_aux <= 1:
                # Si toca el suelo
                self.receptor.y = self.suelo
                if self.cuando_termina:
                    self.cuando_termina()


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
def cuando_suelta_tecla(e):
    if e.codigo=="s":
        soldado.parar()

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
        soldado.mover_fondo()
        soldado.espejado=False
    if e.codigo=="a":
        soldado.mover_fondo_i()
        soldado.espejado=True

pilas.escena.suelta_tecla.conectar(cuando_suelta_tecla)
pilas.escena.pulsa_tecla.conectar(cuando_pulsa_tecla)
#1 cuchillo
#2 pistola
#3 metralleta
#4 sniper
#5 escopeta
#6 bazuca
#7 granada
pilas.ejecutar()
