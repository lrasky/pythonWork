import pygame

from WarOfPlane import constants


class Bullet(pygame.sprite.Sprite):
    '''子弹类'''
    # 子弹状态 True 表示或者 超出屏幕或撞击 False
    active = True
    def __init__(self, screen, plane, speed = None):
        super().__init__()
        self._screen = screen
        #速度
        self._speed =  speed or 1
        self._plane = plane

        self.image = pygame.image.load(constants.BULLET_IMG)
        # 改变子弹的位置
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top

        #发射的音乐效果
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_SOUND)
        self.shoot_sound.set_volume(0.2)
        self.shoot_sound.play()



    def update(self, *args):
        '''更新子弹的位置'''
        self.rect.top -= self._speed
        if self.rect.top < 0:
            self.remove(self._plane.bullets)

        self._screen.blit(self.image, self.rect)