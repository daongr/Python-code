import os.path
import turtle as t  # 导入turtle内置模块，t变成turtle的别名
import math as m
import pygame
import sys

# 初始化pygame的mixer模块
pygame.mixer.init()

# 移动海龟（留下痕迹）
def trace_turtle(x1, y1, colors):
    t.pencolor(colors)
    t.goto(x1, y1)  # 海龟位置(x1,y1)


# 画椭圆/类三角函数（3）
def draw_x(a, i1):  # x = a * cos(t1)
    t1 = m.radians(i1)  # 角度值变成弧度制
    return a * m.cos(t1)


# 画椭圆/类三角函数（3）
def draw_y(b, i1):  # y = b * sin(t1)
    t1 = m.radians(i1)
    return b * m.sin(t1)


# 画椭圆/类三角函数（2）
def draw_graphics1(i1, a, b, x2, y2, nums1, nums2):
    x1 = draw_x(a, i1 * nums1) + x2
    y1 = draw_y(b, i1 * nums2) + y2
    t.goto(x1, y1)


# 画椭圆/类三角函数（1）
def draw_graphics(i1, i2, a, b, x2, y2, nums1, nums2, add, color1):
    t.pencolor(color1)
    if add:
        while i1 <= i2:
            draw_graphics1(i1, a, b, x2, y2, nums1, nums2)
            i1 += 5
    else:
        while i1 >= i2:
            draw_graphics1(i1, a, b, x2, y2, nums1, nums2)
            i1 -= 5


# 移动海龟的函数（不留痕迹）
def move_turtle(x1, y1):
    t.penup()
    t.goto(x1, y1)
    t.pendown()


# 填充颜色的函数
def fill_color(colors):
    t.fillcolor(colors)  # 将颜色填充到从turtle.start_fill()到turtle.end_fill()的图形里
    t.end_fill()

def resoures_path(path):
    if getattr(sys, 'frozen', False):
        base_path=sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, path)


# （1）设置画布情况
t.bgcolor((211 / 255, 218 / 255, 232 / 255))  # 背景颜色
t.setup(800, 600)  # 背景大小 800, 600--->Width, height
t.title("test")   # 可自定义

# 加载音频文件，替换为自己的音乐文件路径
music_path = resoures_path(os.path.join('cake', 'music.mp3'))
pygame.mixer.music.load(music_path)
# 执行循环播放
pygame.mixer.music.play(-1)


# （2）画底盘
# 1.主体部分
move_turtle(150, -70)  # 移动海龟
draw_colors = (254 / 255, 245 / 255, 247 / 255)
t.begin_fill()
draw_graphics(0, 360, 150, 60, 0, -70, 1, 1, True, draw_colors)  # 画椭圆
fill_color(draw_colors)  # 填充颜色
# 2.下面部分
draw_colors = (246 / 255, 226 / 255, 230 / 255)
t.begin_fill()
draw_graphics(0, 180, 150, 60, 0, -70, -1, -1, True, 'white')
draw_graphics(180, 360, 150, 70, 0, -70, 1, 1, True, 'white')
fill_color(draw_colors)


# （3）生日蛋糕
def cake(x1, y1, x2, y2, a1, b1, b2, y3, top_b, top_y, cake_colors, curve_colors, top_colors, bottom):
    # 主体部分
    move_turtle(x1, y1)
    t.begin_fill()
    trace_turtle(x1, y2, cake_colors)
    draw_graphics(0, 180, a1, b1, 0, y2, 1, 1, True, cake_colors)
    trace_turtle(x2, y1, cake_colors)
    draw_graphics(180, 360, a1, b1, 0, y1, 1, 1, True, cake_colors)
    fill_color(cake_colors)
    # 是否有底部装饰
    if bottom[0]:
        t.begin_fill()
        draw_graphics(0, 180, a1, b1, 0, y1, -1, -1, True, bottom[1])
        draw_graphics(180, 360, a1, b1, 0, y1 + 10, 1, 1, True, bottom[1])
        fill_color(bottom[1])
    # 花边
    move_turtle(x1, y2)
    t.begin_fill()
    t.pensize(4)
    draw_graphics(0, 1799, a1, b2, 0, y3, 0.1, 1, True, curve_colors)
    trace_turtle(x2, y2, curve_colors)
    t.pensize(1)
    draw_graphics(180, 0, a1, b1, 0, y2, 1, 1, False, curve_colors)
    fill_color(curve_colors)
    # 上层填充
    move_turtle(x1 - 10, y2)
    t.begin_fill()
    draw_graphics(0, 360, a1 - 10, top_b, 0, top_y, 1, 1, True, top_colors)
    fill_color(top_colors)


# 1.下层的蛋糕
cake_color = (203 / 255, 217 / 255, 249 / 255)
bottom_color = (255 / 255, 167 / 255, 157 / 255)
curve_color = (255 / 255, 240 / 255, 243 / 255)
top_color = 'white'
cake(120, -70, -120, 0, 120, 48, -18, -60, 40, 2, cake_color, curve_color, top_color, (True, bottom_color))
# 2.上层的蛋糕
cake_color = (111 / 255, 55 / 255, 50 / 255)
curve_color = (255 / 255, 170 / 255, 160 / 255)
top_color = (255 / 255, 195 / 255, 190 / 255)
cake(80, 4, -80, 54, 80, 32, -12, 14, 28, 55, cake_color, curve_color, top_color, (False,))


# （4）生日蜡烛
def candle(x1, y1, x2, y2):
    # 蜡烛主体
    move_turtle(x1, y1)
    draw_color = (177 / 255, 201 / 255, 233 / 255)
    t.begin_fill()
    trace_turtle(x1, y2, draw_color)
    draw_graphics(0, 180, 4, 2, x1 - 4, y2, 1, 1, True, draw_color)
    trace_turtle(x2, y1, draw_color)
    draw_graphics(180, 360, 4, 2, x2 + 4, y1, 1, 1, True, draw_color)
    fill_color(draw_color)
    # 蜡烛痕迹
    draw_color = 'white'
    move_turtle(x2, y1)
    t.pensize(2)
    for i1 in range(1, 6):
        trace_turtle(x1, y1 + 10 * i1, draw_color)
        move_turtle(x2, y1 + 10 * i1)
    # 蜡烛与火光的连接处
    move_turtle(x1 - 4, y2)
    trace_turtle(x1 - 4, y2 + 10, draw_color)
    t.pensize(1)
    # 蜡烛的火光
    draw_color = (241 / 255, 173 / 255, 209 / 255)
    t.begin_fill()
    draw_graphics(0, 360, 4, 10, x1 - 4, y2 + 20, 1, 1, True, draw_color)
    fill_color(draw_colors)


# 五根蜡烛
candle(-56, 54, -64, 104)
candle(-26, 44, -34, 94)
candle(4, 64, -4, 114)
candle(34, 44, 26, 94)
candle(64, 54, 56, 104)

# （5）输出 '生日快乐' 的字符串
t.seth(90)  # 海龟的朝向角度210
t.pu()
t.goto(-180, 180)
t.pd()
t.pencolor((241 / 255, 173 / 255, 209 / 255))
t.write("生日快乐！", font=("Curlz MT", 45, 'bold'))  # 输出'生日快乐'

t.done()  # 等待关闭图形窗口
pygame.mixer.music.stop()  # 关闭音乐背景