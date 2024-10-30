from classes import *
from helpers import *

lista = [1,2,3,4,5,6,7,8,9]

value1 = {0:2,1:4,2:5,3:2}
value2 = {0:5,1:7,2:2,3:2}
value3 = {0:3,1:8,2:1,3:0}
value4 = {0:3,1:7,2:1,3:1}

# por el usuario
value5 = {0:3,1:7,2:1,3:2}

tablero = Tablero()
tablero.get_empty_table()
tablero.set_value(value1)
tablero.set_value(value2)
tablero.set_value(value3)
tablero.set_value(value4)
tablero.print()
# tablero.handle_user_value((3,5,6))
# tablero.handle_user_value((1,7,6))
# tablero.handle_user_value((2,6,6))
# tablero.handle_user_value((8,8,6))
tablero.print()
