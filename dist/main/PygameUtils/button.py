import pygame

#Button class, the optional parameters correspond to the text displayed, its size and font
class button():
    def __init__(self, color, x, y, width, height, text="", size=60, font=None, outline=0):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont(font, size)
        self.outline = outline

    #Draws the button, outline may be provided
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.outline)

        if self.text != "":
            text = self.font.render(self.text, 1, (0,0,0))
            
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        

    #Returns true if the given pos (either tuple or list) is over the button
    def isOver(self, pos):
        return pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

