"""
Meloonatic Melons
HPMRA Map Editor
By Harry Hitchen

Report issues to
meloonatic.help@techie.com

or send us a message at
http://www.meloonaticmessage.btck.co.uk/MessageUs
"""


import pygame, sys, math, pyglet
from scripts.UltraColor import *
from scripts.textures import *


def export_map(file, file2):
    map_data = ""
    item_data = ""

    # Get Map Dimensions
    max_x = 0
    max_y = 0

    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]

#    for i in item_data:
#        if i[0] > max_x:
#            max_x = i[0]
#        if i[1] > max_y:
#            max_y = i[1]

    # Save Map Tiles
    for tile in tile_data:
        map_data = map_data + str(int(tile[0] / Tiles.Size)) + "," + str(int(tile[1] / Tiles.Size)) + ":" + tile[2] + "-"

    for item in item_data:
        item_data = item_data + str(int(item[0] / Items.Size)) + "," + str(int(item[1] / Items.Size)) + ":" + item[2] + "-"


    # Save Map Dimensions
    map_data = map_data + str(int(max_x / Tiles.Size)) + "," + str(int(max_y / Tiles.Size))
    item_data = item_data + str(int(max_x / Items.Size)) + "," + str(int(max_y / Items.Size))


    # Write Map File
    with open(file, "w") as mapfile:
        mapfile.write(map_data)

    with open(file2, "w") as itemfile:
        itemfile.write(item_data)


def load_map(file, file2, file3):

    global tile_data
    global item_data
    global randomly_generated_data

    with open(file, "r") as mapfile:
        map_data = mapfile.read()

#    with open(file2, "r") as itemfile:
#        item_data = itemfile.read()

    map_data = map_data.split("-")
#    item_data = item_data.split("-")

    map_size = map_data[len(map_data) - 1]
    map_data.remove(map_size)
    map_size = map_size.split(",")
    map_size[0] = int(map_size[0]) * Tiles.Size
    map_size[1] = int(map_size[1]) * Tiles.Size

#    item_size = item_data[len(item_data) - 1]
#    item_data.remove(item_size)
#    item_size = item_size.split(",")
#    item_size[0] = int(item_size[0]) * Items.Size
#    item_size[1] = int(item_size[1]) * Items.Size

    tiles = []
    items = []

    for tile in range(len(map_data)):
        map_data[tile] = map_data[tile].replace("\n", "")
        tiles.append(map_data[tile].split(":"))

    for tile in tiles:
        tile[0] = tile[0].split(",")
        pos = tile[0]
        for p in pos:
            pos[pos.index(p)] = int(p)

#    for item in range(len(item_data)):
#        item_data[tile] = item_data[tile].replace("\n", "")
#        items.append(item_data[item].split(":"))

#    for item in items:
#        item[0] = item[0].split(",")
#        pos = item[0]
#        for p in pos:
#            pos[pos.index(p)] = int(p)

        tiles[tiles.index(tile)] = [pos[0] * Tiles.Size, pos[1] * Tiles.Size, tile[1]]
#        items[items.index(item)] = [pos[0] * Items.Size, pos[1] * Items.Size, item[1]]

    tile_data = tiles
#    item_data = items

window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()


txt_font = pygame.font.Font(None, 20)


mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 100 * Tiles.Size, 100 * Tiles.Size


selector = pygame.Surface((Tiles.Size, Tiles.Size), pygame.HWSURFACE | pygame.SRCALPHA)
selector.fill(Color.WithAlpha(100, Color.RedBrown))

tile_data = []
item_data = []

camera_x, camera_y = 0, 0
camera_move = 0


brush = "5"



# Initialize Default Map
for x in range(0, map_width, Tiles.Size):
    for y in range(0, map_height, Tiles.Size):
        tile_data.append([x, y, "1"])


isRunning = True


while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:

            # MOVEMENT
            if event.key == pygame.K_w:
                camera_move = 1
            elif event.key == pygame.K_s:
                camera_move = 2
            elif event.key == pygame.K_a:
                camera_move = 3
            elif event.key == pygame.K_d:
                camera_move = 4

            # BRUSHES
            if event.key == pygame.K_r:
                brush = "r"
            #elif event.key == pygame.K_F5:
             #   selection = input("Brush selection: ")
              #  brush = selection
            elif event.key == pygame.K_1:
                brush = "1"
            elif event.key == pygame.K_2:
                brush = "2"
            elif event.key == pygame.K_3:
                brush = "3"
            elif event.key == pygame.K_4:
                brush = "4"

            if event.key == pygame.K_p:
                brush = "p"
            elif event.key == pygame.K_k:
                brush = "k"
            elif event.key == pygame.K_c:
                brush = "c"


            # SAVE MAP
            if event.key == pygame.K_0:
                name = input("Map Name: ")
                name2 = input("Items Name:")
                export_map("maps/" + name + ".map", "maps/" + name2 + ".item")
                print("Map Saved Successfully!")
                pygame.quit()
                sys.exit()

            elif event.key == pygame.K_n:
                name = input("Map Name: ")
                name2 = input("Items Name: ")
                load_map("maps/" + name + ".map", "maps/" + name2 + ".item")
                print("Map Loaded Successfully!")

        elif event.type == pygame.KEYUP:
            camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / Tiles.Size) * Tiles.Size
            mouse_y = math.floor(mouse_pos[1] / Tiles.Size) * Tiles.Size

        if event.type == pygame.MOUSEBUTTONDOWN:
            tile = [mouse_x - camera_x, mouse_y - camera_y, brush]   # Keep this as a list
            item = [mouse_x - camera_x, mouse_y - camera_y, brush]

            # Is a tile already placed here?
            found = False
            for t in tile_data:
                if t[0] == tile[0] and t[1] == tile[1] :
                    found = True
                    break

            # If this tile space is empty
            if not found:
                if not brush == "r":
                    tile_data.append(tile)

            # If this tile space is not empty
            else:
                # Are we using the rubber tool?
                if brush == "r":
                    # Remove Tile
                    for t in tile_data:
                        if t[0] == tile[0] and t[1] == tile[1]:
                            tile_data.remove(t)
                            print("Tile Removed!")

                else:
                    # Sorry! A tile is already placed here!
                    print("A tile is already placed here!")

            item_found = False
            for i in item_data:
                if i[0] == item[0] and i[1] == item[1]:
                    item_found = True
                    break
            if not item_found and found:
                if not brush == "r" or "1" or "2" or "3" or "4":
                    item_data.append(item)
            else:
                if brush == "t":
                    for i in item_data:
                        if i[0] == item[0] and i[1] == item[1]:
                            item_data.remove(i)
                            print("Item Removed!")
                else:
                    print("An item is already placed here")


    # LOGIC
    if camera_move == 1:
        camera_y += Tiles.Size
    elif camera_move == 2:
        camera_y -= Tiles.Size
    elif camera_move == 3:
        camera_x += Tiles.Size
    elif camera_move == 4:
        camera_x -= Tiles.Size

    # RENDER GRAPHICS
    window.fill(Color.Blue)

    # Draw Map
    for tile in tile_data:
        try:
            window.blit(Tiles.Texture_Tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass

    for item in item_data:
        try:
            window.blit(Items.Item_Tags[item[2]], (item[0] + camera_x, item[1] + camera_y))
        except:
            pass


    # Draw Tile Highlighter (Selector)
    window.blit(selector, (mouse_x, mouse_y))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
