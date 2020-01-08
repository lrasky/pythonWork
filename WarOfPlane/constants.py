import os
#跟目录
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
#静态文件目录
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
# 背景图片
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
#标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')
# 开始按钮图片
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')
#背景音乐
BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/game_bg_music.mp3')

# 我方飞机的静态资源
OUR_PLANE_IMG1 = os.path.join(ASSETS_DIR, 'images/hero1.png')
OUR_PLANE_IMG2 = os.path.join(ASSETS_DIR, 'images/hero2.png')

OUR_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png')
    ]

# 子弹图片

BULLET_IMG = os.path.join(ASSETS_DIR, 'images/bullet1.png')

# 子弹的音乐效果
BULLET_SHOOT_SOUND = os.path.join(ASSETS_DIR, 'sounds/bullet.wav')