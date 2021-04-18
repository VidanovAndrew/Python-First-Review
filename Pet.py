from random import randrange
import pygame


class Pet:
    boredom_decrement = 5
    hunger_decrement = 5
    boredom_limit = 100
    total_bored_limit = 150
    hunger_limit = 125
    total_hungry_limit = 170
    x = 100
    y = 100
    image_happy = pygame.image.load("sources/Grampy cat/happy_cat.gif")
    image_bored = pygame.image.load("sources/Grampy cat/bored_cat.gif")
    image_hungry = pygame.image.load("sources/Grampy cat/haungry.gif")
    image_very_hungry = pygame.image.load("sources/Grampy cat/very_hungry.gif")
    image_very_bored = pygame.image.load("sources/Grampy cat/very_bored.gif")
    image = image_happy

    def __init__(self, name="Boris"):
        self.name = name
        self.hunger = randrange(self.hunger_limit // 2)
        self.boredom = randrange(self.boredom_limit // 2)

    def update(self):
        if self.boredom < 250:
            self.boredom += 1
        if self.hunger < 250:
            self.hunger += 1
        mood = self.mood()
        if mood == "happy":
            self.image = self.image_happy
        elif mood == "very hungry":
            self.image = self.image_very_hungry
        elif mood == "hungry":
            self.image = self.image_hungry
        elif mood == "very bored":
            self.image = self.image_very_bored
        elif mood == "bored":
            self.image = self.image_bored

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def mood(self):
        if self.hunger <= self.hunger_limit and self.boredom <= self.boredom_limit:
            return "happy"
        elif self.hunger > self.total_hungry_limit:
            return "very hungry"
        elif self.hunger > self.hunger_limit:
            return "hungry"
        elif self.boredom > self.total_bored_limit:
            return "very bored"
        else:
            return "bored"

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
