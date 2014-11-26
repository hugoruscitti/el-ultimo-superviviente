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
        self.y=-185
        self.x=-0
        self.z=6
        self.imagen.repetir_horizontal= True
        self.transparencia=100

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
        self.imagen = pilas.imagenes.cargar_animacion("data/soldado/animacion.png", 5)
        self.y = -137
        self.x = -150
        self.escala=1.2
        self.ir_izquierda = False
        self.ir_derecha = False
        self.saltando = False
        self.agachado = False
        
        self.imagen.definir_animacion('corre', [0,1,2,3], 10)
        self.imagen.definir_animacion('parado', [0], 10)
        self.imagen.definir_animacion('saltando', [3], 10)
        self.realizar(Parado)
        self.sombra=pilas.actores.Sombra() 
        self.sombra.z=1
        
    def realizar(self, estado):
        #print "Pasando al estado:", estado
        self.estado_actual = estado(self)
        self.estado_actual.iniciar()

    def actualizar(self):
        self.estado_actual.actualizar()
        pilas.camara.x=self.x+200
        
        self.sombra.x=self.x
        self.sombra.y=-203
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
        
    def reiniciar_animacion(self):
        self.imagen = pilas.imagenes.cargar_animacion("data/soldado/animacion.png", 5)
        self.imagen.definir_animacion('corre', [0,1,2,3], 10)
        self.imagen.definir_animacion('parado', [0], 10)
        self.imagen.definir_animacion('saltando', [3], 10)   
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



class Agachado(Estado):

    def iniciar(self):
        self.receptor.imagen=pilas.imagenes.cargar_grilla("data/soldado/agachado.png",1)
        self.receptor.sombra.escala=[1.25],0.1
        self.receptor.y=-155
    def suelta_tecla(self, tecla):
        if tecla == 's':
            self.receptor.reiniciar_animacion()
            self.receptor.realizar(Parado)
            self.receptor.sombra.escala=[1],0.1
            self.receptor.y=-137
class CorreDerecha(Estado):

    def iniciar(self):
        self.receptor.imagen.cargar_animacion('corre')
        self.receptor.espejado = False

    def suelta_tecla(self, tecla):
        if tecla == 'd':
            self.receptor.realizar(Parado)

    def actualizar(self):
        self.receptor.imagen.avanzar()
        self.receptor.x += 3


class CorreIzquierda(Estado):

    def iniciar(self):
        self.receptor.imagen.cargar_animacion('corre')
        self.receptor.espejado = True

    def suelta_tecla(self, tecla):
        if tecla == 'a':
            self.receptor.realizar(Parado)

    def actualizar(self):
        self.receptor.imagen.avanzar()
        self.receptor.x -= 3



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
        self.receptor.sombra.escala=[0.5,1],0.2
        
    def actualizar(self):
        self.receptor.imagen.avanzar()
        self.receptor.y += self.velocidad
        self.velocidad -= 1
        if self.receptor.y <= self.suelo:
            self.velocidad=0
            self.receptor.y =-135
            self.receptor.saltando=False
            self.receptor.realizar(Parado)


class Zombie(pilasengine.actores.Actor):
    def iniciar(self):
        #self.imagen="zombies2.png"
        self.x=pilas.camara.x+400

        self.y=-140
        self.escala=1
        self.imagen=pilas.imagenes.cargar_grilla("zombie.png",3)
        self.sombra=pilas.actores.Sombra()
    def actualizar(self):
        self.imagen.avanzar(5)
        self.x -= 1.5
        self.sombra.x=self.x
        self.sombra.y=-200
        self.sombra.z=1
        self.sombra.escala_y=1.5
        if self.x < pilas.camara.x -400:
            self.eliminar()
        if self.sombra.x < pilas.camara.x -400:
            self.sombra.eliminar()
        
class Fondo (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="background01.png"
        self.y=0
        self.x=0
        self.z=10
        self.escala=1
        self.imagen.repetir_horizontal= True


    def actualizar(self):
        self.x -=+0
        if self.x < -1400:
            self.x= -0

class Bloque (pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="data/barra/bloque.png"
        self.y=150
        self.x=-50
        self.sonido=pilas.sonidos.cargar("data/sonidos/pop.wav")
        self.fijo=True
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


def cuando_colisionan(soldado, zombie):
    zombie.sombra.eliminar()
    zombie.eliminar()
    
def crear_zombie():
    un_zombie=Zombie(pilas)
    pilas.colisiones.agregar(soldado,un_zombie,cuando_colisionan)
pilas.escena.tareas.siempre(5,crear_zombie)



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
actor.escala=0.28
actor.x=91
actor.y=143
actor.fijo=True

actor2=pilas.actores.Actor()
actor2.imagen="data/barra/dinamita.png"
actor2.escala=0.5
actor2.x=184
actor2.y=150
actor2.fijo=True


actor3=pilas.actores.Actor()
actor3.imagen="data/barra/escudo.png"
actor3.escala=0.23
actor3.x=270
actor3.y=150
actor3.fijo=True


actor4=pilas.actores.Actor()
actor4.imagen="data/barra/metra.png"
actor4.escala=0.28
actor4.x=-88
actor4.y=145
actor4.fijo=True

actor5=pilas.actores.Actor()
actor5.imagen="data/barra/cuchillito.png"
actor5.escala=0.23
actor5.x=-270
actor5.y=149
actor5.fijo=True


actor6=pilas.actores.Actor()
actor6.imagen="data/barra/pistol.png"
actor6.escala=0.5
actor6.x=-180
actor6.y=145
actor6.fijo=True


actor7=pilas.actores.Actor()
actor7.imagen="data/barra/motosierra.png"
actor7.escala=0.45
actor7.x=1
actor7.y=150
actor7.fijo=True








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
