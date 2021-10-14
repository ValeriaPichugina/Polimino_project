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
        self.rect.topleft = (100+margin+55,100+margin)
        self.id = random.randint(1,1000000000000000000000)


def decoord(h,m,coord):
    return round((coord-m-100-1)/(h+m))

def cell_found(h,m,coord):
    return [decoord(h,m,i)-1 for i in coord]

def right_coord(n,m,coord):
    return all([0<=coord[0]<n and 0<=coord[1]<=m])

def cell_coord(h,m,cell):
    return [((h + m)*i + m + 100) for i in cell]
pygame.init()
background_colour = (234, 212, 252)
screen = pygame.display.set_mode((2000,1000))


pygame.display.set_caption('Geeksforgeeks')
screen.fill(background_colour)

n=2
m=4
error = False
rt = False
gr =[ [0]*n for _ in range(m) ]

print(gr)

height=800/max(n,m)
margin=height/50
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
x2 = Figures(height,margin,[[1],[1],[1]])
x2 = Figures(height,margin,[[0,1,0],[1,1,1]])

figs_sprites = pygame.sprite.Group()
figs_sprites.add(x1,x2)

while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



            elif event.type == pygame.MOUSEBUTTONDOWN:
                for fig in figs_sprites:
                    if fig.rect.collidepoint(event.pos):
                        moving = True
                        mouse_x, mouse_y = event.pos
                        mouse_event = tuple(i * (-1) for i in event.pos)
                        offset = tuple(map(operator.add, fig.rect.topleft, mouse_event))
                        curr_fig = fig

            elif event.type == pygame.MOUSEBUTTONUP:
                print("ывфывфывфы")
                moving = False
                tst = curr_fig.rect.topleft
                print(tst)
                a=(round((tst[0]-margin-100)/(height+margin)),
                        round((tst[1] - margin - 100) / (height + margin)))
                print(a)

                tst2 = curr_fig.rect.bottomright
                c = (round((tst2[0] - margin - 100) / (height + margin)) - 1,
                     round((tst2[1] - margin - 100) / (height + margin)) - 1)
                print(c)
                b = (
                        (height+margin)*a[0]+margin+100,
                    (height+margin)*a[1]+margin+100
                         )
                curr_fig.rect.topleft=b
                if 0<=a[1]<n and 0<=a[0]<m :

                    # b =(
                    #     (height+margin)*a[0]+margin+100,
                    #     (height+margin)*a[1]+margin+100
                    #     )
                    # curr_fig.rect.topleft=b

                    tst = curr_fig.rect.topleft
                    print(tst)
                    a = (round((tst[0] - margin - 100) / (height + margin)),
                         round((tst[1] - margin - 100) / (height + margin)))
                    print(a)

                    tst2 = curr_fig.rect.bottomright
                    c = (round((tst2[0] - margin - 100) / (height + margin))-1,
                         round((tst2[1] - margin - 100) / (height + margin))-1)
                    print(c)
                    if 0<=c[1]<n and 0<=c[0]<m:
                        arrrrrr = [(i,j) for i in range(a[0],c[0]+1) for j in range(a[1],c[1]+1)]

                        for ind in arrrrrr:
                            ssss = np.array(ind) - np.array(a)
                            if curr_fig.arr[ssss[1]][ssss[0]] == 1:
                                gr[ind[0]][ind[1]] = curr_fig.id


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
                curr_fig.rect.topleft = tuple(map(operator.add, event.pos, offset))

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
