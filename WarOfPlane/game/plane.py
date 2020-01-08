'''
飞机的基类
1， 我方飞机
2， 敌方飞机：1 小型飞机  2 中型飞机   3 大型飞机
'''
import pygame

from WarOfPlane import constants
from WarOfPlane.game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    '''
    飞机基类
    '''
    # 飞机的图片
    plane_images = []
    # 飞机爆炸图片
    destroy_images = []
    # 飞机坠毁的音乐地址
    down_sound_src = None
    # 飞机的状态 : True 活的，  False 死的
    active = True
    # 飞机发射子弹的精灵组
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed = None):
        super().__init__()
        # 加载的静态资源
        self._screen = screen
        self._img_list = []
        self._destroy_img_list = []
        self._down_sound = None
        # 飞机飞行的速度
        self._speed = speed or 10
        self.loadsrc()
        # 获取飞机的位置
        self.rect = self._img_list[0].get_rect()
        #游戏窗口的大小
        self._width, self._height = self._screen.get_size()
        # 飞机的大小
        self.plane_w, self.plane_h = self._img_list[0].get_size()
        # 改变飞机的初始化位置
        self.rect.left = int((self._width - self.plane_w)/2)
        self.rect.top = int(self._height - self.plane_h)





    def loadsrc(self):
        '''
        加载静态资源
        '''
        # 飞机的图像
        for img in self.plane_images:
            self._img_list.append(pygame.image.load(img))

        # 飞机坠毁的图片
        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))

        # 坠毁的音乐
        if self.down_sound_src:
            self._down_sound = pygame.mixer.Sound(self.down_sound_src)
    @property
    def image(self):
        return self._img_list[0]


    def blit_me(self):
        self._screen.blit(self.image, self.rect)

    def move_up(self):
        self.rect.top -= self._speed

    def move_down(self):
        self.rect.top += self._speed

    def move_left(self):
        self.rect.left -= self._speed

    def move_right(self):
        self.rect.left += self._speed

    def broken_down(self):
        # 1 播放坠毁音乐
        if self._down_sound:
            self._down_sound.play()

        # 2 播放坠毁动画
        for img in self._destroy_img_list:
            self._screen.blit(img, self.rect)


        # 3 坠毁后
        self.active = False


    def shoot(self):
        bullet = Bullet(self._screen, self, 30)
        self.bullets.add(bullet)




class OurPlane(Plane):

    # 飞机的图片
    plane_images = [constants.OUR_PLANE_IMG1, constants.OUR_PLANE_IMG2]
    # 飞机爆炸图片
    destroy_images = constants.OUR_DESTROY_IMG_LIST
    # 飞机坠毁的音乐地址
    down_sound_src = None
    def update(self, frame):
        '''更新飞机的动画效果'''
        if frame % 5:
            self._screen.blit(self._img_list[0], self.rect)
        else:
            self._screen.blit(self._img_list[1], self.rect)

    def move_up(self):
        super(OurPlane, self).move_up()
        if self.rect.top <= 0:
            self.rect.top = 0

    def move_down(self):
        super(OurPlane, self).move_down()
        if self.rect.top >= self._height - self.plane_h:
            self.rect.top = self._height - self.plane_h

    def move_left(self):
        super(OurPlane, self).move_left()
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_right(self):
        super(OurPlane, self).move_right()
        if self.rect.left >= self._width - self.plane_w:
            self.rect.left = self._width - self.plane_w