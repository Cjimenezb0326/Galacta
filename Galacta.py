#from PIL import Image, ImageChops, ImageEnhance, ImageOps
import pygame, random, time 
import os

pygame.init()
WHITE =(255, 255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
#############################################################################################################
carpeta_imagenes = "imagenes"
def cargar_imagen(nombre_archivo):
    ruta = os.path.join(carpeta_imagenes, nombre_archivo)
    imagen = pygame.image.load(ruta)
    return imagen
nave = cargar_imagen("nave2.png")
balaimg = cargar_imagen("bala.png")
fondo = cargar_imagen("fondo1.gif")
bonus_boximg = cargar_imagen("bonus_img.png") 
fondo2 = cargar_imagen("fondo_up.png")
bonus_exp = cargar_imagen("bonus_exp.png")
bonus_tel = cargar_imagen("bonus_tel.png")
bonus_pts = cargar_imagen("bonus_pts.png")
bonus_escudo = cargar_imagen("escudo.png")
bonus_exp_d = cargar_imagen("bonus_exp_d.jpg")
bonus_vidas = cargar_imagen("bonus_vidas.png")
bonus_tel_d = cargar_imagen("bonus_tel_d.png")
bonus_pts_d = cargar_imagen("bonus_pts_d.png")
bonus_escudo_d = cargar_imagen("escudo_d.png")
bonus_vidas_d = cargar_imagen("bonus_vidas_d.png")
#############################################################################################################
carpeta_sonidos = "sonidos"
def cargar_sonido(nombre_archivo):
    ruta = os.path.join(carpeta_sonidos, nombre_archivo)
    sonido = pygame.mixer.Sound(ruta)
    return sonido
mov_sonido = cargar_sonido("movimiento.wav")
bala_sonido = cargar_sonido("bala_sonido.wav")
bonus_son=cargar_sonido("bonus_son.wav")
#############################################################################################################

screen = pygame.display.set_mode((1300, 720))
clock = pygame.time.Clock()
running = True
##############################################################################################################
class box(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = bonus_boximg
		self.rect = self.image.get_rect()
		self.image.set_colorkey(WHITE)
		self.rect.x=random.randint(10,1200)
		self.rect.y=110
		self.speed_y = 1
		
	def update(self):	
		self.rect.y += self.speed_y
		if self.rect.y >730:
			bonus_box_1.remove(bonus_box)
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = nave
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y=620
		self.rect.x=600
		self.speed_x = 0
		self.speed_y = 0

	def changespeed(self, y):
		self.speed_y += y
		if player.rect.y >=589:
			player.rect.y=579
		if player.rect.y <=100:
			player.rect.y=100
	def changespeedx(self, x):
		self.speed_x += x
		if player.rect.x >=1250:
			player.rect.x=1250
		if player.rect.x <=5:
			player.rect.x=10
			

	def update(self):
		self.rect.y += self.speed_y
		self.rect.x += self.speed_x
class Bala(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = balaimg
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()

	def update(self):
    		self.rect.y -= 15
class Bonus_exp(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = bonus_exp_d
		self.rect = self.image.get_rect()
		self.image.set_colorkey(WHITE)
		self.rect.x=1000
		self.rect.y=0
class Bonus_tel(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = bonus_tel_d
		self.rect = self.image.get_rect()
		self.image.set_colorkey(WHITE)
		self.rect.x=1000
		self.rect.y=19
class Bonus_pts(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = bonus_pts_d
		self.rect = self.image.get_rect()
		self.image.set_colorkey(WHITE)
		self.rect.x=1000
		self.rect.y=39
class Bonus_vidas(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = bonus_vidas_d
		self.rect = self.image.get_rect()
		self.image.set_colorkey(WHITE)
		self.rect.x=1000
		self.rect.y=59
class Bonus_escudo(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = bonus_escudo_d
		self.rect = self.image.get_rect()
		self.image.set_colorkey(WHITE)
		self.rect.x=1000
		self.rect.y=79
##############################################################################################################
bala_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
bonus_box_1 = pygame.sprite.Group()
player = Player()
bonus_box= box()
bonus_1= Bonus_exp()
bonus_2= Bonus_tel()
bonus_3= Bonus_pts()
bonus_4= Bonus_vidas()
bonus_5= Bonus_escudo()

all_sprite_list.add(bonus_1, bonus_2, bonus_3,bonus_4,bonus_5,bonus_box,player)
bonus_box_1.add(bonus_box)
###############################################################################################################
while running:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
					running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					player.changespeed(6)
					mov_sonido.play()
				if event.key == pygame.K_UP:
					player.changespeed(-6)
					mov_sonido.play()
				if event.key == pygame.K_RIGHT:
					player.changespeedx(6)
					mov_sonido.play()
				if event.key == pygame.K_LEFT:
					player.changespeedx(-6)
					mov_sonido.play()
				if player.rect.y >=579:
					player.changespeed(0)
				if event.key == pygame.K_SPACE:
					bala = Bala()
					bala.rect.x = player.rect.x+16
					bala.rect.y = player.rect.y +5
					bala_sonido.play()
				
					all_sprite_list.add(bala)
					bala_list.add(bala)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					player.changespeed(-6)
				if event.key == pygame.K_UP:
					player.changespeed(6)
				if event.key == pygame.K_RIGHT:
					player.changespeedx(-6)
				if event.key == pygame.K_LEFT:
					player.changespeedx(6)

	bonus_hit=pygame.sprite.spritecollide(player,bonus_box_1 ,True) 
	if bonus_hit:
			bonus_son.play()
			bonus_prob=random.randint(1,5)
			if bonus_prob==1:
				bonus_1.image=bonus_exp
			if bonus_prob==2:
				bonus_2.image=bonus_tel
			if bonus_prob==3:
				bonus_3.image=bonus_pts
			if bonus_prob==4:
				bonus_4.image=bonus_vidas
			if bonus_prob==5:
				bonus_5.image=bonus_escudo


	screen.blit(fondo,[0,0])
	screen.blit(fondo2,[0,0])
	pygame.draw.line(screen, RED, (1400,100), (0,100), 4)
	pygame.draw.line(screen, RED, (250,-150), (250,100), 4)
	pygame.draw.line(screen, RED, (1050,-150), (1050,100), 4)
	all_sprite_list.draw(screen)
	all_sprite_list.update()
	pygame.display.flip()
	clock.tick(60)  

pygame.quit()