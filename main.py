import pygame
import button
from tkinter import*
pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

While=(255,255,255)
Gray=(128,128,128)
Gray_1=(236,236,236)
Hard_Blue=(0,178,191)
#define fonts

font = pygame.font.SysFont("arialblack", 40)

#define colours
Font2=pygame.font.SysFont('sabs',20)
TEXT_COL = (255, 255, 255)


#load button images
resume_img = pygame.image.load("button_resume.png").convert_alpha() 
bfs_img = pygame.image.load('bfs.png').convert_alpha()
dfs_img = pygame.image.load('dfs.png').convert_alpha()
tt_img = pygame.image.load("tt.png").convert_alpha()
quit_img = pygame.image.load("button_quit.png").convert_alpha()
A_img = pygame.image.load('A.png').convert_alpha()
B_img = pygame.image.load('B.png').convert_alpha()
C_img = pygame.image.load('C.png').convert_alpha()
back_img = pygame.image.load('button_back.png').convert_alpha()

#create button instances
resume_button = button.Button(297, 125, resume_img, 1)
bfs_button = button.Button(226, 75, bfs_img, 1)
dfs_button = button.Button(225, 200, dfs_img, 1)
tt_button = button.Button(297, 250, tt_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
A_button = button.Button(226, 75, A_img, 1)
B_button = button.Button(225, 200, B_img, 1)
C_button = button.Button(227, 325, C_img, 1)
back_button = button.Button(332, 450, back_img, 1)
def draw(screen,font,text,color,x,y):
  text=font.render(text,True,color)
  screen.blit(text,(x,y))
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:
  
  screen.fill((250, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
       
      if resume_button.draw(screen):
        menu_state = "resume"

      if tt_button.draw(screen):
        menu_state = "tt"
      if quit_button.draw(screen):
        run = False
    if menu_state == "resume":
      if bfs_button.draw(screen):
        print("bfs Settings")
      if dfs_button.draw(screen):
        print("dfs Settings")
      if C_button.draw(screen):
        print("Change C")
      if back_button.draw(screen):
        menu_state = "main"
    #check if the options menu is open
    if menu_state == "tt":
      #draw the different options buttons
    
      if A_button.draw(screen):
        
       
        root=Tk()
       
        Label(root,text='Nhap A*',font=('camvria',20),width=25 ).grid(row=1)
        root.minsize(height=500,width=400)
        Label(root,width=60,height=20).grid(row=1,column=2)
        

        Entry(root,width=25,textvariable=id).grid(row=2,column=1)
        button=Frame(root)
        
        Button(button,text='back', command=root.quit).pack(side=LEFT)
 
        button.grid(row=3,column=1)

      
           
        root.mainloop()
        

        Button(button,text='back').pack(side=LEFT)
        if back_button.draw(screen):
           menu_state = "main"
      if B_button.draw(screen):
        print("B Settings") 
      
      if back_button.draw(screen):
        menu_state = "main"
    

     
      if back_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("Game thuat toan!!!", font, TEXT_COL, 160, 250)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
