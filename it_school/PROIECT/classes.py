import pygame

class Buttons:

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
    

        return button_surface