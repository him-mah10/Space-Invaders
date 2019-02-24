class Missiles(object):

    x = 3
    y = 5

    def __init__(self,spaceship):
        self.y = spaceship.pos
        self.x = 7


class i_Missile(Missiles):

    def __init__(self, spaceship):
        super(i_Missile, self).__init__(spaceship)
        self.speed = 1
        self.character = 'i'


class l_Missile(Missiles):

    def __init__(self, spaceship):
        super(l_Missile, self).__init__(spaceship)
        self.speed = 2
        self.character = 'l'
