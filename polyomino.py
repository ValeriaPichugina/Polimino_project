import pygame
import operator
import random
import numpy as np

class Figures(pygame.sprite.Sprite):
    def __init__(self,h,mar,coords):
        pygame.sprite.Sprite.__init__(self)
        self.size = h
        self.margin = mar
        self.arr = coords
        self.image = pygame.Surface(
            (
             self.size * (len(self.arr[0])) + self.margin*(len(self.arr[0])-1),
             self.size * (len(self.arr))    + self.margin * (len(self.arr)-1)

            )
        )
        #pygame.Surface.set_alpha(self.image, 100)
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        self.image.fill((self.r,self.g,self.b))
        self.image.set_alpha(150)
        self.rect = self.image.get_rect()
        self.rect.topleft = (1000,100)
        self.id = random.randint(1,1000000)


def decoord(h,m,coord):
    return round((coord-m-100)/(h+m))

def cell_found(h,m,coord):
    return [decoord(h,m,i) for i in coord]

def right_coord(n,m,coord):
    return all([0<=coord[0]<=m and 0<=coord[1]<=n])

def cell_coord(h,m,cell):
    return [((h + m)*i + m + 100) for i in cell]

def placeQ(grid, points):
    for pt in points:
        if grid[pt[0]][pt[1]] != 0:
            return False
    return True

def place(grid,points,id):
    for pt in points:
        grid[pt[0]][pt[1]] = id
    return grid

def remove(grid,id):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == id:
                grid[i][j] = 0
    return grid

def status(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return False
    return True

def right_crd(n, m, coords):
    for i in coords:
        if 0 <= i[0] < n and 0 <= i[1] < m:
            pass
        else:
            return False
    return True


def gener(n,m,toAdd = []):
    grid =[ [0]*m  for _ in range(n) ]
    main_base = [
        [[1]],[[1,1]],[[1,1,1]],[[1,1,1,1]],
        [[1],[1]],[[1],[1],[1]],[[1],[1],[1],[1]],
        [[1,1],[0,1]],[[0,1,0],[1,1,1]],[[1,0,0],[1,1,1]]
    ]
    base = main_base+toAdd
    all_points = [[i,j] for i in range(n) for j in range(m)]
    print(all_points)
    figs = []
    ir=0



    while not status(grid):
        print("-----------------------------------------------")
        tmp_fig = random.choice(base)
        print("chosen figure")
        print(tmp_fig)
        place_points = []
        tmp = all_points[0]
        print("center")
        print(tmp)
        filled_pts = [np.array(tmp) + np.array([i, j]) for i in range(len(tmp_fig)) for j in range(len(tmp_fig[0]))]
        print("points recta")
        print(filled_pts)
        for ind in filled_pts:
            abs_pnt = np.array(ind) - np.array(tmp)
            # print(absolute_point)
            #print("ind")
            #print(ind)
            if tmp_fig[abs_pnt[0]][abs_pnt[1]] == 1:
                place_points.append(list(ind))

        print("meanful points recta")
        print(place_points)
        if right_crd(n,m,place_points):
            print("zashel")
            if placeQ(grid,place_points):
                grid = place(grid,place_points,1)

                    #all_points = [i for i in all_points if i not in place_points]
                for i in place_points:
                    all_points.remove(list(i))

                print("all centres after placa")
                print(all_points)
                figs.append(tmp_fig)

    print("field")
    print(grid)
    print(figs)
    return figs

pygame.init()
background_colour = (234, 212, 252)
screen = pygame.display.set_mode((1500,800))


pygame.display.set_caption('polyomino')
screen.fill(background_colour)
#n*m размеронсть поля
n=4
m=7
error = False
rt = False
gr =[ [0]*m for _ in range(n) ]

print(gr)

height=round(800/max(n,m))
margin=round(height/50)
print(margin+100)
print(height)
#margin = 1
running = True
moving = False

testRect1 = pygame.Rect(30,30,height,height)
testRect2 = pygame.Rect(70,70,height,height)
test = pygame.Rect(300,800,height,height)
nw = pygame.Rect.union(testRect2,test)
figs = [testRect1,testRect2]
#pygame.draw.rect(screen, (1,1,1), testRect1)
#pygame.draw.rect(screen, (1,1,1), testRect2,  2)
#pygame.draw.rect(screen, (1,1,1), testRect3,  2)
#pygame.draw.rect(screen, (1,1,1), pygame.Rect.union_ip(testRect1,testRect2),1)
#pygame.draw.rect(screen,(255,255,255),pygame.Rect(98,98,500,500),3)
#pygame.display.flip()
x1 = Figures(height,margin,[[1,1]])
x2 = Figures(height,margin,[[1],
                           [1],
                            [1]])
x3 = Figures(height,margin,[[0,1,0],[1,1,1]])

figs_sprites = pygame.sprite.Group()
#добавление
#figs_sprites.add(x1,x2,x3)
#gen = generate(n,m)
#figs_sprites.add(*[Figures(height,margin,i) for i in gen])
fgs = gener(n,m)
print(fgs)
figs_sprites.add(*[Figures(height,margin,i) for i in fgs])

while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



            elif event.type == pygame.MOUSEBUTTONDOWN:
                for fig in figs_sprites:
                    if fig.rect.collidepoint(event.pos):
                        moving = True
                        mouse_x, mouse_y = event.pos
                        offset = tuple(np.array(fig.rect.topleft) - np.array(event.pos))
                        curr_fig = fig
                        print("Ты держишь фигуру")
                        print(curr_fig.arr)

            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False

                cr_fig_topleft = curr_fig.rect.topleft
                curr_topleft= cell_found(height,margin,cr_fig_topleft)

                aproximated_topleft = cell_coord(height,margin,curr_topleft)
                curr_fig.rect.topleft=aproximated_topleft

                if right_coord(n,m,curr_topleft):

                    cr_fig_botright = curr_fig.rect.bottomright
                    curr_botright = np.array(cell_found(height, margin, np.array(cr_fig_botright)- 0.5*margin))-1
                    #print(curr_botright)

                    if right_coord(n,m,curr_botright):
                        curr_topleft = cell_found(height,margin,aproximated_topleft)
                        #print(curr_botright, curr_topleft)
                        filled_points = [(j,i) for i in range(curr_topleft[0],curr_botright[0]+1) for j in range(curr_topleft[1],curr_botright[1]+1)]
                        #print("-------------------------")
                        #print(filled_points)
                        #print(curr_topleft)
                        #print(type(curr_topleft))
                        #print("-------------------------")
                        place_points = []
                        tmp = [curr_topleft[1],curr_topleft[0]]
                        for ind in filled_points:
                            absolute_point = np.array(ind) - np.array(tmp)
                            #print(absolute_point)
                            #print(ind)
                            if curr_fig.arr[absolute_point[0]][absolute_point[1]] == 1:
                                place_points.append(ind)

                        if placeQ(gr,place_points):
                            gr = remove(gr,curr_fig.id)
                            gr = place(gr,place_points,curr_fig.id)
                        #        gr[ind[0]][ind[1]] = curr_fig.id


                        print(gr)



                #print(cell_coord(height,m,tst))

                # #if curr_fig.collidepoint(event.pos):
                # coord = testRect1.center
                # a = cell_found(height, margin, coord)
                # print(a)
                # if right_coord(n,m,a):
                #     testRect1 = pygame.Rect(*cell_coord(height,margin,a), height,height)
                # else:
                #     print("chmo")

            elif event.type == pygame.MOUSEMOTION and moving:
                mouse_x, mouse_y = event.pos
                #curr_fig.rect.topleft = tuple(map(operator.add, event.pos, offset))
                curr_fig.rect.topleft = tuple(np.array(event.pos)+ np.array(offset))


            elif event.type == pygame.KEYUP:
                if status(gr):
                    running=False

            screen.fill(background_colour)

        #pygame.draw.rect(screen, (2,0,255), testRect2)
        #pygame.draw.rect(screen, (2,0,55), test)
        #pygame.draw.rect(screen, (2,0,55), nw)



        for row in range(n):
            for column in range(m):
                color = (255,255,255)
                pygame.draw.rect(screen,
                                 color,
                                 [(height + margin) * column + margin + 100,
                                  (height + margin) * row + margin + 100,
                                  height,
                                  height])

        #pygame.draw.rect(screen, (255, 0, 255), testRect1)
        #pygame.draw.rect(screen, (255, 0, 255), testRect2)
        for fig in figs_sprites:
            screen.blit(fig.image, fig.rect)
    #pygame.draw.polygon(screen,(255,5,5),[[0,0],[0,100],[100,0],[100,100]])
        pygame.display.update()

pygame.quit()
