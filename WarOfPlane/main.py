'''

'''
import sys

import pygame

from WarOfPlane import constants
from WarOfPlane.game.plane import OurPlane


def main():
    '''游戏入口 main方法'''
    pygame.init() #游戏初始化
    #设置游戏界面大小
    width, height = 480, 852
    screen = pygame.display.set_mode((width, height))
    #背景图片
    bg = pygame.image.load(constants.BG_IMG)
    # 标题图片
    img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
    img_game_title_react = img_game_title.get_rect()
    # 游戏标题的宽高
    t_width, t_height = img_game_title.get_size()
    img_game_title_react.topleft = (int((width - t_width) / 2),
                                    int(height / 2 - t_height))

    # 开始按钮
    btn_start = pygame.image.load(constants.IMG_GAME_START_BTN)
    btn_start_rect = img_game_title.get_rect()
    # 开始按钮的宽高
    btn_width, btn_height = btn_start.get_size()
    btn_start_rect.topleft = (int((width - btn_width) / 2),
                              int(height/2 + btn_height))

    #加载背景音乐
    pygame.mixer.music.load(constants.BG_MUSIC)
    pygame.mixer.music.play(-1) #循环播放
    pygame.mixer.music.set_volume(0.2) #设置音量
    pygame.display.set_caption('飞机大战') #设置标题

    # 绘制我方飞机
    our_plane = OurPlane(screen, 5)

    frame = 0  # 播放的总帧数
    clock = pygame.time.Clock()

    #游戏状态
    status = 0 # 0 准备中， 1 游戏中， 2 游戏结束

    while True:
        # 设置贞速率
        clock.tick(60)
        frame += 1
        if frame > 50:
            frame = 0
        # 事件监听
        for event in pygame.event.get():
            #退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if status == 0:
                    status = 1

            # 键盘事件
            # 游戏正在游戏中
            elif event.type == pygame.KEYDOWN:
                if status == 1:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        our_plane.move_up()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        our_plane.move_down()
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        our_plane.move_left()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        our_plane.move_right()
                    elif event.key == pygame.K_SPACE:
                        our_plane.shoot()
            # 更新游戏状态
            elif status == 0:
                #游戏正在准备中
                #绘制背景图
                screen.blit(bg, bg.get_rect())
                #标题
                screen.blit(img_game_title, img_game_title_react)
                # 按钮
                screen.blit(btn_start, btn_start_rect)

            elif status == 1:# 游戏开始
                # 绘制背景图
                screen.blit(bg, bg.get_rect())
                # 绘制飞机
                our_plane.update(frame)
                our_plane.bullets.update()

            pygame.display.flip()
        # screen.blit(bg, bg.get_rect())
        # pygame.display.flip()
if __name__ == '__main__':
    main()