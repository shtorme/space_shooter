from data import*


class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height, image= None, speed= 5):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.SPEED = speed


class Hero(Sprite):
    def __init__(self, x, y, width, height, image= None, speed= 5):
        super().__init__(x, y, width, height, image, speed)
        self.MOVE = {"LEFT":  False, "RIGHT":  False}

    def move(self, window):
        if self.MOVE["LEFT"] == True and self.x > 0:
            self.x -= self.SPEED
        if self.MOVE["RIGHT"] == True and self.x + self.width < setting_win["WIDTH"]:
            self.x += self.SPEED
        pygame.draw.rect(window, (120,120,120), self)
    
    
    

