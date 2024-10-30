from helpers import *

class Value:
    def __init__(self, value):
        self.value = self.get_value_as_dict(value)


    def get_value_as_dict(self, value):
        as_dict = {
            0:value[0], # x
            1:value[1], # y
            2:value[2], # num
            # validation: 0 -> wrong, 1 -> right, 2 -> auto set
            3:2, 
        }
        return as_dict


class Tablero:
    def __init__(self):
        self.table = []

    def print(self):
        print('\n\n')
        self.draw_table()
        print('\n\n')

    def get_empty_table(self):
        h = 9
        l = 9
        while len(self.table) < h:
            line = []
            for n in range(0, l):
                line.append('x')
            self.table.append(line)
    
    def draw_table(self):
        current_table = [row[:] for row in self.table]
        
        for i, l in enumerate(current_table):
            l = l[:9] + ['x'] * (9 - len(l))
            
            if len(l) == 9:
                l.insert(3, '|')
                l.insert(7, '|')
            
            for v in l:
                if v != 'x' and v != '|':
                    if v[3] == 2:
                        print(v[2], end=' ')
                    elif v[3] == 1:
                        prGreen(v[2], end=' ')
                    elif v[3] == 0:
                        prRed(v[2], end=' ')
                else:
                    print(v, end=" ")
            print()
            
            if i == 2 or i == 5:
                print('---------------------')

    
    def check_in_lines(self, value):
        for l in self.table:
            if l[value[0]] == value[2]:
                return False
            if value[2] in l:
                return False
        return True
    
    def check_in_sector(self, value):
        sector = get_sector(value[0], value[1], self.table)

        for l in sector:
            for v in l:
                if v == 'x':
                    return True
                if v[2] == value[2]:
                    return False
        return True
        
    def set_value(self, value):
        print(f'aca {value}')
        if self.check_in_lines(value) and self.check_in_sector(value):
            value[3] = 1
            self.table[value[1]][value[0]] = value
        else:
            value[3] = 0
            self.table[value[1]][value[0]] = value
        
    def handle_user_value(self, value):
    # el user va a cargar el value como una tupla (x,x,x)
    # se va a instanciar en Value y obtendremos el valor correspondiente, usando los checkers para determinar el ultimo valor del objeto Value
        inputed_value = Value(value).value
        self.set_value(inputed_value)

