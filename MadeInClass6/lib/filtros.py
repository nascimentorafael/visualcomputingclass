#coding=utf8
import lib.readwrite as rw
import lib.plotgraph as plot
import lib.histogram as hist
import numpy as np
import math


def passa_baixa():
    filtro = np.ones((5,5),dtype="int8")
    div = 25
    return filtro,div