import pygame,math,sys

pygame.init()
clock = pygame.time.Clock()
game = "off"

screen_width = 1500
screen_height = screen_width/2
#map_size = 8
cell_length = 20
map_length = int(screen_width/cell_length)
map_height = int(screen_height/cell_length)

#max_depth = int(map_size*cell_length)
l = 50

white = (211,81,0)
bg_color = (248,161,69)
black = (0, 0, 0)  
lblack = (15, 15, 15)
mid = (240, 121, 0)
ghost_line = (0,0,0)
red = (255,0,0)
blue = (135,206,235)

screen = pygame.display.set_mode ((screen_width, screen_height))
pygame.display.set_caption('Game of Life')

MAP = ('        '
       '        '
       '        '
       '    #   '
       '        '
       '        '
       '        '
       '        ')

greenlist=[]
green_index_list =[]
buffer_list = []



def draw_map():
    global green_index_list, buffer_list

    buffer_list = green_index_list.copy()
    for row in range(map_height):
        for col in range(map_length):
            index = row *map_length + col

            if game == "on":
                live_or_die(index)            

            #drawingstuff
            if (index) not in green_index_list:
                pygame.draw.rect(screen,(100,100,100), (col*(cell_length),row*cell_length, cell_length-2,cell_length-2))
            else:
                pygame.draw.rect(screen,(0,100,100), (col*(cell_length),row*cell_length, cell_length-2,cell_length-2))
    green_index_list = buffer_list.copy()


def get_clickIndex(pos, delete=False):

    row = int(pos[1]/cell_length)
    col = int(pos[0]/cell_length)
    if delete is True:
        print('hm')
        el = row *map_length + col
        if el in green_index_list:
            print('removed')
            green_index_list.remove(el)
            greenlist.remove((row,col))
        return
    greenlist.append((row,col))
    green_index_list.append(row *map_length + col)
    

def live_or_die(cellindex):
    global buffer_list
    top_cell = cellindex-map_length
    bottom_cell = cellindex + map_length
    left_cell = cellindex-1
    right_cell = cellindex+1
    top_left_cell = top_cell-1
    top_right_cell = top_cell+1
    bottom_left_cell = bottom_cell -1
    bottom_right_cell = bottom_cell +1
    
    n = [top_cell,top_left_cell,top_right_cell, left_cell, right_cell, bottom_cell, bottom_left_cell, bottom_right_cell]
    neighbours =[]
    for i in n:
        if i in range(0, map_height*map_length):
            neighbours.append(i)
        else:
            neighbours.append(None)

    c = 0
    for i in neighbours:
        if i in green_index_list:
            c+=1
    if cellindex in green_index_list:
        if c<2:
            buffer_list.remove(cellindex)
        if c>3:
            buffer_list.remove(cellindex)
    else:
        if c == 3:
            buffer_list.append(cellindex)







    


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                get_clickIndex(pos)
            elif event.button == 3:
                pos = pygame.mouse.get_pos()
                get_clickIndex(pos, True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                game = "on"
                dup = green_index_list.copy()
                for i in dup:
                    if green_index_list.count(i) >= 2:
                        green_index_list.remove(i)
            
    
    screen.fill(black)
    draw_map()
        
    
    pygame.display.flip()
    
    clock.tick(10)
