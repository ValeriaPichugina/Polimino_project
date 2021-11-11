def decoord(h,m,coord):
    return round((coord-m-100)/(h+m))

def cell_found(h,m,coord):
    return [decoord(h,m,i) for i in coord]

def right_coord(n,m,coord):
    return all([0<=coord[0]<=m and 0<=coord[1]<=n])

def cell_coord(h,m,cell):
    return [((h + m)*i + m + 100) for i in cell]
pygame.init()
background_colour = (234, 212, 252)
screen = pygame.display.set_mode((2000,1000))