# -*- encoding: utf-8 -*-
#
# Imagenes utilizadas desde el link:
#
#             http://mechanox.deviantart.com/gallery/?catpath=%2Fdigitalart&offset=0
#

import pilasengine
pilas=pilasengine.iniciar(capturar_errores=False)


class Pasto (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="data/fondo/Floor.png"
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
        self.imagen = pilas.imagenes.cargar_animacion("data/soldado/animacion.png", 8)
        self.y = -145
        self.x = -150
        self.ir_izquierda = False
        self.ir_derecha = False
        self.saltando = False
        self.agachado = False

        self.imagen.definir_animacion('corre', [3, 4], 10)
        self.imagen.definir_animacion('parado', [6], 10)
        self.imagen.definir_animacion('saltando', [3], 10)
        self.imagen.definir_animacion('agachado', [0], 10)
        self.realizar(Parado)

    def realizar(self, estado):
        #print "Pasando al estado:", estado
        self.estado_actual = estado(self)
        self.estado_actual.iniciar()

    def actualizar(self):
        self.estado_actual.actualizar()

    def mover_fondo(self):
        self.pasto.mover()
        self.fondo.mover()

    def mover_fondo_i(self):
        self.pasto.mover_i()
        self.fondo.mover_i()

    def agachar(self):
        self.imagen = pilas.imagenes.cargar_grilla("data/soldado/agachado.png", 1)

    def parar(self):
        self.imagen = pilas.imagenes.cargar_grilla("data/soldado/corredor.png", 1)

    def saltar(self):
        if not self.saltando:
            self.imagen = pilas.imagenes.cargar_grilla("data/soldado/salto.png", 1)
            self.realizar(Saltar)

    def pulsa_tecla(self, tecla):
        self.comportamiento_actual.pulsa_tecla(tecla)

class Estado(object):

    def __init__(self, receptor):
        self.receptor = receptor

    def actualizar(self):
        pass

    def saltar(self):
        pass

    def agachar(self):
        pass

    def pulsa_tecla(self, tecla):
        pass
        #print "pulsa_tecla", tecla

    def suelta_tecla(self, tecla):
        pass
        #print "suelta tecla", tecla

class Parado(Estado):

    def iniciar(self):
        self.receptor.imagen.cargar_animacion('parado')

    def actualizar(self):
        self.receptor.imagen.avanzar()

    def saltar(self):
        pass

    def agachar(self):
        pass

    def pulsa_tecla(self, tecla):
        if tecla == 'w':
            self.receptor.realizar(Saltar)

        if tecla == 's':
            self.receptor.realizar(Agachado)

        if tecla == 'd':
            self.receptor.realizar(CorreDerecha)

        if tecla == 'a':
            self.receptor.realizar(CorreIzquierda)

class Agachado(Estado):

    def iniciar(self):
        self.receptor.imagen.cargar_animacion('agachado')

    def suelta_tecla(self, tecla):
        if tecla == 's':
            self.receptor.realizar(Parado)


class CorreDerecha(Estado):

    def iniciar(self):
        self.receptor.imagen.cargar_animacion('corre')
        self.receptor.espejado = False

    def suelta_tecla(self, tecla):
        if tecla == 'd':
            self.receptor.realizar(Parado)

    def actualizar(self):
        self.receptor.imagen.avanzar()
        self.receptor.mover_fondo()


class CorreIzquierda(Estado):

    def iniciar(self):
        self.receptor.imagen.cargar_animacion('corre')
        self.receptor.espejado = True

    def suelta_tecla(self, tecla):
        if tecla == 'a':
            self.receptor.realizar(Parado)

    def actualizar(self):
        self.receptor.imagen.avanzar()
        self.receptor.mover_fondo_i()



class Saltar(Estado):
    """Realiza un salto, cambiando los atributos 'y'."""

    def iniciar(self, velocidad_inicial=13, cuando_termina=None):
        """Se invoca cuando se anexa el comportamiento a un actor.

        :param receptor: El actor que comenzará a ejecutar este comportamiento.
        """
        self.velocidad_inicial = velocidad_inicial
        self.suelo = int(self.receptor.y)
        self.velocidad = self.velocidad_inicial
        self.receptor.saltando = True
        self.receptor.imagen.cargar_animacion('saltando')

    def actualizar(self):
        self.receptor.imagen.avanzar()
        self.receptor.y += self.velocidad
        self.velocidad -= 1

        if self.receptor.y <= self.suelo:
            self.velocidad=0
            self.receptor.y =-150
            self.receptor.saltando=False
            self.receptor.realizar(Parado)


class Zombie(pilasengine.actores.Actor):
    def iniciar(self):
        #self.imagen="zombies2.png"
        self.escala=0.7
        self.imagen=pilas.imagenes.cargar_grilla("data/zombie/caminando.png",6)
    def actualizar(self):
        self.imagen.avanzar(5)
        self.x -=+1
class Fondo (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="data/fondo/fondo.png"
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
        self.imagen="data/barra/bloque.png"
        self.y=150
        self.x=-50
        self.sonido=pilas.sonidos.cargar("data/sonidos/pop.wav")

    def seleccionar(self):
        self.sonido.reproducir()
        self.imagen="data/barra/bloque_naranja.png"
    def deshacer(self):
        self.imagen="data/barra/bloque.png"



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
zombie.x=400
zombie.y=-130
fondo.zombie=zombie

dist=90
bloque7.x=dist*3
bloque7.escala=0.5
balas_7=pilas.actores.Texto()
balas_7.texto="0"
balas_7.escala=0.4
balas_7.x=305
balas_7.y=135

bloque6.x=dist*2
bloque6.escala=0.7
balas_6=pilas.actores.Texto()
balas_6.texto="0"
balas_6.escala=0.6
balas_6.x=230
balas_6.y=130



bloque5.x=dist*1
bloque5.escala=0.84
balas_5=pilas.actores.Texto()
balas_5.texto="0"
balas_5.escala=0.7
balas_5.x=150
balas_5.y=125


bloque4.x=dist*0
bloque4.seleccionar()
balas_4=pilas.actores.Texto()
balas_4.texto="0"
balas_4.escala=0.9
balas_4.x=70
balas_4.y=123


bloque3.x=dist*-1
bloque3.escala=0.84
balas_3=pilas.actores.Texto()
balas_3.texto="0"
balas_3.escala=0.7
balas_3.x=-30
balas_3.y=125


bloque2.x=dist*-2
bloque2.escala=0.7
bloque6.x=dist*2
bloque6.escala=0.7
balas_6=pilas.actores.Texto()
balas_6.texto="0"
balas_6.escala=0.6
balas_6.x=-130
balas_6.y=130


bloque1.x=dist*-3
bloque1.escala=0.5
bloque_seleccionado=3





actor=pilas.actores.Actor()
actor.imagen="data/barra/escopeta.png"
actor.escala=2
actor.x=89
actor.y=143


actor2=pilas.actores.Actor()
actor2.imagen="data/barra/minigun.png"
actor2.escala=1.6
actor2.x=184
actor2.y=145



actor3=pilas.actores.Actor()
actor3.imagen="data/barra/granato.png"
actor3.escala=1.5
actor3.x=267
actor3.y=145



actor4=pilas.actores.Actor()
actor4.imagen="data/barra/metra.png"
actor4.escala=1.5
actor4.x=-90
actor4.y=145


actor5=pilas.actores.Actor()
actor5.imagen="data/barra/cuchillito.png"
actor5.escala=1.8
actor5.x=-270
actor5.y=145



actor6=pilas.actores.Actor()
actor6.imagen="data/barra/pistol.png"
actor6.escala=1.3
actor6.x=-180
actor6.y=145



actor6=pilas.actores.Actor()
actor6.imagen="data/barra/sniper.png"
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

    soldado.estado_actual.pulsa_tecla(e.codigo)

def cuando_suelta_tecla(e):
    soldado.estado_actual.suelta_tecla(e.codigo)

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
