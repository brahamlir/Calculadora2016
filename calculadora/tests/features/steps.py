# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora


@step(u'dado que tengo los operadores "([^"]*)" y "([^"]*)"')
def dado_que_tengo_los_operadores_group1_y_group1(step, num1, num2):
    world.operador1 = int(num1)
    world.operador2 = int(num2)
    world.cal = Calculadora()


@step(u'cuando realizo la suma')
def cuando_realizo_la_suma(step):
    world.operacion = world.cal.suma(world.operador1, world.operador2)


@step(u'entonces el resultado que obtengo es "([^"]*)"')
def entonces_el_resultado_que_obtengo_es_group1(step, resultado):
    assert world.operacion == int(
        resultado), 'El resultado  esperado no es el mismo' +\
        resultado + 'no es' + str(world.operacion)


@step(u'cuando realizo la resta')
def cuando_realizo_la_resta(step):
    world.operacion = world.cal.resta(world.operador1, world.operador2)


@step(u'cuando realizo la multiplicacion')
def cuando_realizo_la_multiplicacion(step):
    world.operacion = world.cal.multiplicacion(
        world.operador1, world.operador2)


@step(u'cuando realizo la divicion')
def cuando_realizo_la_divicion(step):
    world.operacion = world.cal.divicion(world.operador1, world.operador2)
