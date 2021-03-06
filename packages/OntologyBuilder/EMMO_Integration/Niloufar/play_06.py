#!/usr/local/bin/python3
# encoding: utf-8

"""
===============================================================================
 Ontology design facility
===============================================================================

This program is part of the ProcessModelling suite

"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2015, PREISIG, Heinz A"
__since__ = "16.09.2019"
__license__ = "GPL planned -- until further notice for Bio4Fuel & MarketPlace internal use only"
__version__ = "5.04"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"

# import emmo_attach as O
from emmo_attach import ProMoOwlOntology

# import record_definitions as O

#from record_definitions import RecordVariable_6
#from record_definitions import RecordEquation

from owlready2 import *

name = "play"
owlfile = name+".owl"

# onto  = O.setup_ontology(name)
o = ProMoOwlOntology()
onto = o.setupOnto()

a = onto.VAR("a")
a.has_unit_time = [-2]
a.has_unit_mass = [1]

b = onto.VAR("b")
c = onto.VAR("c")

a.is_function_of = [onto.b]
c.is_function_of = [onto.a]


#--------------------------------
d = onto.RecordVariable("d")
d.has_unit_time = [-2]
d.has_unit_mass = [1]


f = onto.RecordEquation("f")
f.has_unit_time = [-2]
f.has_unit_mass = [1]

#--------------------------------


# onto.sync_attributes()

# sync_reasoner_pellet([onto])
# sync_reasoner([onto])


onto.save(owlfile)
print("end")


