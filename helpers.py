import random

def get_random_value():
    value = random.randint(1,9)
    return value

def get_sector(x,y,table):
    sector_x = get_cordetanes(x)
    sector_y = get_cordetanes(y)
    sector = []
    for i, l in enumerate(table):
        if sector_y[0] <= i <= sector_y[1]:
            sector.append(l[sector_x[0]:sector_x[1]+1])
    return sector

def get_cordetanes(c):
    if 0 <= c < 3:
        return (0,2)
    if 3 <= c < 6:
        return (3,5)
    if 6 <= c < 9:
        return (6,8)
    
def prRed(skk, end): print("\033[91m{}\033[00m" .format(skk), end=end)
def prGreen(skk, end): print("\033[92m{}\033[00m" .format(skk), end=end)

def get_x_value(builder):
    value = builder(())