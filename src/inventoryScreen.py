import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

def drawInventory(screen, bg, inventoryItems):
    screen.blit(bg, (0, 0))
    pygame.display.update()

    if(inventoryItems[0] == 1):
        door = pygame.image.load('../assets/door.png')
        door = pygame.transform.scale(door, (104, 139))
        screen.blit(door, (120, 220))
    if (inventoryItems[1] == 1):
        fender = pygame.image.load('../assets/fender.png')
        fender = pygame.transform.scale(fender, (140, 84))
        screen.blit(fender, (100, 440))
    if (inventoryItems[2] == 1):
        wheel = pygame.image.load('../assets/wheel.png')
        wheel = pygame.transform.scale(wheel, (157, 156))
        screen.blit(wheel, (87, 610))
    if (inventoryItems[3] == 1):
        windshield = pygame.image.load('../assets/windshield.png')
        windshield = pygame.transform.scale(windshield, (136, 160))
        screen.blit(windshield, (100, 820))
    if (inventoryItems[4] == 1):
        nail = pygame.image.load('../assets/nail.png')
        nail = pygame.transform.scale(nail, (28, 136))
        screen.blit(nail, (380, 220))
    if (inventoryItems[5] == 1):
        barrel = pygame.image.load('../assets/barrel.png')
        barrel = pygame.transform.scale(barrel, (95, 139))
        screen.blit(barrel, (345, 420))
    pygame.display.update()

def inventory(screen, inventoryItems):
    bg = pygame.image.load('../assets/Inventory.png')
    bg = pygame.transform.scale(bg, (1920, 1080))
    cont = 1

    while cont == 1:
        for event in pygame.event.get():
            drawInventory(screen, bg, inventoryItems)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    cont = 0

def determineInventory(playerX, playerY, inventoryItems):
    if(playerX > -5000 and playerX < -4400 and playerY > -2500 and playerY < -1850):
        inventoryItems[0] = 1
    if (playerX > -450 and playerX < 100 and playerY > -4200 and playerY < -3800):
        inventoryItems[1] = 1
    if (playerX > -2075 and playerX < -1250 and playerY > -4025 and playerY < -3450):
        inventoryItems[2] = 1
    if (playerX > -6275 and playerX < -5975 and playerY > -4150 and playerY < -3650):
        inventoryItems[3] = 1
    if (playerX > 150 and playerX < 550 and playerY > -4125 and playerY < -3850):
        inventoryItems[4] = 1
    if (playerX > -3500 and playerX < -2750 and playerY > -4200 and playerY < -3475):
        inventoryItems[5] = 1