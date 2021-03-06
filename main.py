import pygame as pg


class WalkingPumpkinMan(pg.sprite.Sprite):
    def __init__(self):
        super(WalkingPumpkinMan, self).__init__()

        self.images = []
        self.images.append(pg.image.load('images/walk1.png'))
        self.images.append(pg.image.load('images/walk2.png'))
        self.images.append(pg.image.load('images/walk3.png'))
        self.images.append(pg.image.load('images/walk4.png'))
        self.images.append(pg.image.load('images/walk5.png'))
        self.images.append(pg.image.load('images/walk6.png'))
        self.images.append(pg.image.load('images/walk7.png'))
        self.images.append(pg.image.load('images/walk8.png'))
        self.images.append(pg.image.load('images/walk9.png'))
        self.images.append(pg.image.load('images/walk10.png'))

        self.images = []
        for i in range(1, 11):
            self.images.append(pg.image.load('images/walk' + str(i) + '.png'))

        self.index = 0

        self.image = self.images[self.index]
        self.rect = pg.Rect(5,5,150,198)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]


pg.init()
screen = pg.display.set_mode((400,400))
sprite = WalkingPumpkinMan()
group = pg.sprite.Group(sprite)

clock = pg.time.Clock()

running = True

while running:

    screen.fill((120,134,163)) #RGB - Red Green Blue values from 0 to 255
    group.update()
    group.draw(screen)
    pg.display.update()
    clock.tick(30)

    key_states = pg.key.get_pressed()
    for state in key_states:
        if state:
            print("A key is pressed")

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            running = False