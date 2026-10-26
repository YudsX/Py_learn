import pygame

# init sebagai run time nya, untuk menjalankan engine nya
pygame.init()

# Variable running agar window tetap berjalan
run = True 

# membuat display surface object (untuk si kotak)
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar, window_panjang)) # <- display utamanya, tempat untuk semua aset nya
pygame.display.set_caption("<- ARROW GAME ->")

clock = pygame.time.Clock() # <- biar stabil pas di press

# Object game 
# koordinat posisi
x = 250
y = 250

# ukuran 
panjang = 20
lebar = 20

# kecepatan gerak
speed = 5

while run:
    # untuk memperlambat gerak si kotak
    pygame.time.delay(40)

    #user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Game Stop Running!!")
            run = False

    # Ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # Ambil ke left (kiri)
    if keys[pygame.K_LEFT] and x > 0:
        print("Tombol kiri sedang di press!")
        x -= speed

    if keys[pygame.K_RIGHT] and x < window_lebar -  lebar:
        print("Tombol kanan sedang di press!")
        x += speed

    if keys[pygame.K_DOWN] and y < window_panjang -  panjang:
        print("Tombol bawah sedang di press!")
        y += speed

    if keys[pygame.K_UP] and y > 0:
        print("Tombol atas sedang di press!")
        y -= speed

    # update asset
    window.fill((0,0,0))
    pygame.draw.rect(window, (255,120,0), (x,y ,lebar, panjang))
    # render ke display
    pygame.display.update()

    clock.tick(60) # <- Fps press

pygame.quit()