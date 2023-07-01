import pygame
from classes import Buttons

pygame.init()


screen = pygame.display.set_mode((1280, 720))

""" class Buttons:

    def __init__(self) -> None:
        
        self.button_font = None
        self.button_name = None
        self.button_surface = None


    def First_button(self):

        #This function creates the button Start

        button_font = pygame.font.Font(None, 100)
        button_name = "START"
        button_surface = button_font.render(button_name, True, (255, 255, 255))
    

        return button_surface

    def Second_button(self):

        #This function creates the button Exit

        button_font = pygame.font.Font(None, 100)
        button_name = "EXIT"
        button_surface = button_font.render(button_name, True, (255, 255, 255))
    

        return button_surface """

buttons = Buttons()

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("blue")
    screen.blit(buttons.First_button(), (500, 200))
    screen.blit(buttons.Second_button(), (525,300))

    pygame.display.flip()

    

pygame.quit()
