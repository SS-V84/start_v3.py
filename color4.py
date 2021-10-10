import pyautogui as pg
import time
import numpy as np
from PIL import Image
import cv2


def start(myimg):
# while True:
#     # img_name = input(" What is the name of the picture greenhouse? ")
#     img_name=pg.prompt( "What is the name of the picture greenhouse?", "Test")
    #среднее значение пикселя картинки

    # myimg = cv2.imread(img_name)
    print(type(myimg))
    avg_color_per_row = np.average(myimg, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    # srcolos = [avg_color[2], avg_color[1], avg_color[0]] # если используем cv2
    srcolos = avg_color
    print(avg_color)
    print(srcolos)

    # находим ближайший цвет к цвету из списка цветов
    # list_of_colors = [[88,128,66],[98,129,69],[59,99,49],[37,73,47],[62,79,73], [63,65,64]] # эталон
    # list_of_colors = [[88,128,66],[210,222,202],[217,227,216],[209,218,210],[201,211,204], [202,206,203]] # оптимизировано для клевых фото
    list_of_colors = [[112,152,96],[98,129,69],[59,99,49],[38,54,29],[49,57,49], [47,48,42]] # оптимизировано
    color = srcolos
    print(list_of_colors[0])
    def closest(colors,color):
        colors = np.array(colors)
        color = np.array(color)
        distances = np.sqrt(np.sum((colors-color)**2,axis=1))
        index_of_smallest = np.where(distances==np.amin(distances))
        smallest_distance = colors[index_of_smallest]
        return smallest_distance

    closest_color = closest(list_of_colors, color)
    print(closest_color)
    # эталон
    if float((closest_color[0])[0]) == list_of_colors[0][0]:
        answer = 4
        return answer
    elif float((closest_color[0])[0]) == list_of_colors[1][0]:
        answer = 5
        return answer
    elif float((closest_color[0])[0]) == list_of_colors[2][0]:
        answer = 6
        return answer
    elif float((closest_color[0])[0]) == list_of_colors[3][0]:
        answer = 7
        return answer
    elif float((closest_color[0])[0]) == list_of_colors[4][0]:
        answer = 8
        return answer
    elif float((closest_color[0])[0]) == list_of_colors[5][0]:
        answer = 9
        return answer
# img_name=pg.prompt( "What is the name of the picture greenhouse?", "Test")
# start(img_name)
    # оптимизировано
    # if float((closest_color[0])[0]) == 112:
    #     a =('sample 4')
    #     pg.confirm(f'{a}')
    # elif float((closest_color[0])[0]) == 98:
    #     a1 = ('sample 5')
    #     pg.confirm(f'{a1}')
    # elif float((closest_color[0])[0]) == 59:
    #     a2 = ('sample 6')
    #     pg.confirm(f'{a2}')
    # elif float((closest_color[0])[0]) == 38:
    #     a3 = ('sample 7')
    #     pg.confirm(f'{a3}')
    # elif float((closest_color[0])[0]) == 49:
    #     a4 = ('образец 8')
    #     pg.confirm(f'{a4}')
    # elif float((closest_color[0])[0]) == 47:
    #     a5 = ('sample 9')
    #     pg.confirm(f'{a5}')




# найти цвет пикселя
time.sleep(4)
# x,y=pg.position()
# # s = str(s)
# print(x,y)
# r,g,b= pg.pixel(x,y)
# print(r,g,b)
# # сделать снимок экрана

# s4 = pg.screenshot("4_blanc.png", region=(680,202,64,145))
# s5 = pg.screenshot("5_blanc.png", region=(764,202,59,145))
# s6 = pg.screenshot("6_blanc.png", region=(842,202,64,145))
# s7 = pg.screenshot("7_blanc.png", region=(923,202,64,145))
# s8 = pg.screenshot("8_blanc.png", region=(1001,202,64,145))
# s9 = pg.screenshot("GH10.1.jpg", region=(871,271,64,145))


# s1 = pg.screenshot("1_blanc.png", region=(678,390,64,75))
# s4 = pg.screenshot("1.2_blanc.png", region=(760,390,64,75))
# s5 = pg.screenshot("1.3_blanc.png", region=(842,390,64,75))
# s4 = pg.screenshot("1.4_blanc.png", region=(923,390,64,75))
# s4 = pg.screenshot("1.5_blanc.png", region=(1001,390,64,75))
# s5 = pg.screenshot("1.6_blanc.png", region=(1092,390,64,75))
# s5 = pg.screenshot("1.6_blanc.png", region=(1092,390,64,75))