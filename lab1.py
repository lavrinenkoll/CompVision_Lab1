from graphics import *
import numpy as np
import math as mt
import matplotlib.colors as mcolors


# calculate coordinates of triangle in 2d
def calculate_coordinates2d(window_width, window_height):
    # calculate side length of triangle
    side_length = (window_width / 2 * window_height / 3) ** 0.5 / 2

    # calculate coordinates of triangle
    coordinates = np.array([
        [0, side_length / 2, 1],
        [side_length / 2, -side_length / 2, 1],
        [-side_length / 2, -side_length / 2, 1]
    ])

    return np.array(coordinates)


# calculate coordinates of pyramid in 3d
def calculate_coordinates3d(window_width, window_height):
    # calculate height and base length of pyramid on the base of window size
    height = window_height / 3
    base = window_width / 10

    # calculate coordinates of pyramid
    base1 = [-base, -base, 0, 1]
    base2 = [base, -base, 0, 1]
    base3 = [base, base, 0, 1]
    base4 = [-base, base, 0, 1]

    high = [0, 0, height, 1]

    return np.array([base1, base2, base3, base4, high])


# draw triangle in 2d with given coordinates and color
def draw_triangle2d(triangle, color):
    # get coordinates of triangle
    Ax, Ay, A1 = triangle[0]
    Bx, By, B1 = triangle[1]
    Cx, Cy, C1 = triangle[2]

    # draw triangle
    obj = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Cx, Cy))
    obj.setOutline(color)
    obj.draw(window1)

    window1.setBackground("white")

    return draw_triangle2d


# draw pyramid in 3d with given coordinates and colors of fill and outline
def draw_pyramid3d(pyramid, color_fill, color_outline):
    # get coordinates of pyramid
    Ax, Ay, Az, A1 = pyramid[0]
    Bx, By, Bz, B1 = pyramid[1]
    Cx, Cy, Cz, C1 = pyramid[2]
    Dx, Dy, Dz, D1 = pyramid[3]
    Ex, Ey, Ez, E1 = pyramid[4]

    # draw labels
    # label_A = Text(Point(Ax, Ay), "A")
    # label_B = Text(Point(Bx, By), "B")
    # label_C = Text(Point(Cx, Cy), "C")
    # label_D = Text(Point(Dx, Dy), "D")
    # label_E = Text(Point(Ex, Ey), "E")
    #
    # label_A.setTextColor(color_outline)
    # label_B.setTextColor(color_outline)
    # label_C.setTextColor(color_outline)
    # label_D.setTextColor(color_outline)
    # label_E.setTextColor(color_outline)
    #
    # label_A.draw(window)
    # label_B.draw(window)
    # label_C.draw(window)
    # label_D.draw(window)
    # label_E.draw(window)

    # draw pyramid with fill and outline
    obj = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Cx, Cy), Point(Dx, Dy))
    obj.setFill(color_fill)
    obj.setOutline(color_outline)
    obj.draw(window2)
    obj = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Ex, Ey))
    obj.setFill(color_fill)
    obj.setOutline(color_outline)
    obj.draw(window2)
    obj = Polygon(Point(Bx, By), Point(Cx, Cy), Point(Ex, Ey))
    obj.setFill(color_fill)
    obj.setOutline(color_outline)
    obj.draw(window2)
    obj = Polygon(Point(Cx, Cy), Point(Dx, Dy), Point(Ex, Ey))
    obj.setFill(color)
    obj.setOutline(color_outline)
    obj.draw(window2)
    obj = Polygon(Point(Dx, Dy), Point(Ax, Ay), Point(Ex, Ey))
    obj.setFill(color)
    obj.setOutline(color_outline)
    obj.draw(window2)

    # draw pyramid with outline (for animation)
    obj = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Cx, Cy), Point(Dx, Dy))
    obj.setOutline(color_outline)
    obj.draw(window2)
    obj = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Ex, Ey))
    obj.setOutline(color_outline)
    obj.draw(window2)
    obj = Polygon(Point(Bx, By), Point(Cx, Cy), Point(Ex, Ey))
    obj.setOutline(color_outline)
    obj.draw(window2)
    obj = Polygon(Point(Cx, Cy), Point(Dx, Dy), Point(Ex, Ey))
    obj.setOutline(color_outline)
    obj.draw(window2)
    obj = Polygon(Point(Dx, Dy), Point(Ax, Ay), Point(Ex, Ey))
    obj.setOutline(color_outline)
    obj.draw(window2)

    window2.setBackground("white")

    return draw_pyramid3d


# move triangle in 2d
def move2d(triangle, move_x, move_y):
    # create matrix of move
    f = np.array([[1, 0, move_x],
                  [0, 1, move_y],
                  [1, 0, 1]])
    # transpose matrix
    ft = f.T
    # multiply matrix of move and coordinates of triangle
    Prxy = triangle.dot(ft)
    return Prxy


# scale triangle in 2d
def scale2d(triangle, scale_x, scale_y):
    # create matrix of scale
    f = np.array([[scale_x, 0, 0],
                  [0, scale_y, 0],
                  [0, 0, 1]])
    # transpose matrix
    ft = f.T
    # multiply matrix of scale and coordinates of triangle
    Prxy = triangle.dot(ft)
    return Prxy


# project pyramid in 3d
def trimetric_prct3d(pyramid, TetaG1, TetaG2, TetaG3):
    # convert degrees to radians
    TetaR1 = (TetaG1 * mt.pi) / 180
    TetaR2 = (TetaG2 * mt.pi) / 180
    TetaR3 = (TetaG3 * mt.pi) / 180

    # create matrices of projection
    f1 = np.array([
        [1, 0, 0, 0],
        [0, mt.cos(TetaR1), -mt.sin(TetaR1), 0],
        [0, mt.sin(TetaR1), mt.cos(TetaR1), 0],
        [0, 0, 0, 1]
    ])

    f2 = np.array([
        [mt.cos(TetaR2), 0, mt.sin(TetaR2), 0],
        [0, 1, 0, 0],
        [-mt.sin(TetaR2), 0, mt.cos(TetaR2), 0],
        [0, 0, 0, 1]
    ])

    f3 = np.array([
        [mt.cos(TetaR3), -mt.sin(TetaR3), 0, 0],
        [mt.sin(TetaR3), mt.cos(TetaR3), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    # multiply matrices of projection and coordinates of pyramid
    Prxy1 = np.dot(pyramid, f1.T)
    Prxy2 = np.dot(Prxy1, f2.T)
    Prxy3 = np.dot(Prxy2, f3.T)

    return Prxy3


# move pyramid in 3d
def move3d(pyramid, move_x, move_y, move_z):
    # create matrix of move
    f = np.array([[1, 0, 0, move_x],
                  [0, 1, 0, move_y],
                  [0, 0, 1, move_z],
                  [1, 0, 0, 1]])
    # transpose matrix
    ft = f.T
    # multiply matrix of move and coordinates of pyramid
    Prxy = pyramid.dot(ft)
    return Prxy


# rotate pyramid around center in 3d
def rotate_around_center3d(pyramid, TetaX, TetaY, TetaZ):
    # calculate center of pyramid
    center_x = np.mean(pyramid[:, 0])
    center_y = np.mean(pyramid[:, 1])
    center_z = np.mean(pyramid[:, 2])

    # move pyramid to center
    pyramid[:, 0] -= center_x
    pyramid[:, 1] -= center_y
    pyramid[:, 2] -= center_z

    # convert degrees to radians
    TetaRX = (TetaX * mt.pi) / 180
    TetaRY = (TetaY * mt.pi) / 180
    TetaRZ = (TetaZ * mt.pi) / 180

    # create matrices of rotation
    f_x = np.array([
        [1, 0, 0, 0],
        [0, mt.cos(TetaRX), -mt.sin(TetaRX), 0],
        [0, mt.sin(TetaRX), mt.cos(TetaRX), 0],
        [0, 0, 0, 1]
    ])

    f_y = np.array([
        [mt.cos(TetaRY), 0, mt.sin(TetaRY), 0],
        [0, 1, 0, 0],
        [-mt.sin(TetaRY), 0, mt.cos(TetaRY), 0],
        [0, 0, 0, 1]
    ])

    f_z = np.array([
        [mt.cos(TetaRZ), -mt.sin(TetaRZ), 0, 0],
        [mt.sin(TetaRZ), mt.cos(TetaRZ), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    # multiply matrices of rotation and coordinates of pyramid
    pyramid = pyramid.dot(f_x).dot(f_y).dot(f_z)

    # move pyramid back to original position
    pyramid[:, 0] += center_x
    pyramid[:, 1] += center_y
    pyramid[:, 2] += center_z

    return pyramid


# window settings
window_width = 500
window_height = 600

# task I
# create window
window1 = GraphWin("Lab 1, I task", window_width, window_height)
# calculate coordinates of triangle
coord = calculate_coordinates2d(window_width, window_height)
coord_now = coord
flag = True

# enable animation
while flag:
    # move triangle
    coord_now = move2d(coord, 100, 100)
    # draw triangle
    draw_triangle2d(coord_now, "black")

    # scale triangle
    coord_scale = scale2d(coord, 0.5, 0.5)
    coord_scale_safe = coord_scale

    # move triangle again and draw it
    time.sleep(0.5)
    draw_triangle2d(coord_now, "white")
    coord_now = move2d(coord_scale, 100, 100)
    draw_triangle2d(coord_now, "black")

    # move triangle to the right bottom corner, animation
    for i in range(100, window_width - 100, 10):
        coord_move = move2d(coord_scale, i, i)
        time.sleep(0.05)
        draw_triangle2d(coord_now, "white")
        coord_now = coord_move
        draw_triangle2d(coord_move, "black")

    # scale triangle again
    coord_scale = scale2d(coord_scale_safe, 2, 2)

    # move triangle to the left top corner and draw it
    time.sleep(0.5)
    draw_triangle2d(coord_now, "white")
    coord_now = move2d(coord_scale, window_width - 100, window_width - 100)
    draw_triangle2d(coord_now, "black")

    # move triangle to the left top corner, animation
    for i in range(window_width - 100, 100, -10):
        coord_move = move2d(coord_scale, i, i)
        time.sleep(0.05)
        draw_triangle2d(coord_now, "white")
        coord_now = coord_move
        draw_triangle2d(coord_move, "black")

    time.sleep(0.5)
    draw_triangle2d(coord_now, "white")

    # check if mouse clicked, if yes, close window
    if window1.checkMouse():
        flag = False
        window1.close()

# task II
# create window
window2 = GraphWin("Lab 1, II task", window_width, window_height)
# calculate coordinates of pyramid
coord = calculate_coordinates3d(window_width, window_height)
rotate_y = 0
flag = True

# enable animation
while flag:
    # set default coordinates of shift
    x_default = 50
    y_default = 500
    z_default = -200
    # set random coordinates of shift
    x = x_default + np.random.randint(-50, 50)
    y = y_default + np.random.randint(-300, 300)
    z = z_default + np.random.randint(-80, 80)
    # move pyramid
    coord_move = move3d(coord, x, y, z)
    # project pyramid
    coord_ax = trimetric_prct3d(coord_move, 75, 25, 0)
    # set random colors
    r = np.random.randint(0, 200)
    g = np.random.randint(0, 200)
    b = np.random.randint(0, 200)
    # rotate pyramid around center with saving rotation angle
    coord_moving = rotate_around_center3d(coord_ax, 0, rotate_y, 0)

    # animation of rotation and color change
    for i in range(0, 50, 3):
        rotate_y += 5
        # rotate pyramid around center
        coord_moving = rotate_around_center3d(coord_moving, 0, 5, 0)
        # calculate transparency
        a = i * 2 / 200
        a2 = i * 2 / 100
        # calculate colors
        color1 = "#{:02X}{:02X}{:02X}".format(r, g, b)
        color2 = "#FFFFFF"
        color1_outline = "#{:02X}{:02X}{:02X}".format(r, g, b)
        rgb1 = mcolors.hex2color(color1)
        rgb2 = mcolors.hex2color(color2)
        rgb1_outline = mcolors.hex2color(color1_outline)
        color_mix = [(c1 * a + c2 * (1 - a)) for c1, c2 in zip(rgb1, rgb2)]
        color_mix_outline = [(c1 * a2 + c2 * (1 - a2)) for c1, c2 in zip(rgb1_outline, rgb2)]
        color_mix = [min(max(c, 0), 1) for c in color_mix]
        color_mix_outline = [min(max(c, 0), 1) for c in color_mix_outline]
        color = mcolors.to_hex(color_mix)
        color_outline = mcolors.to_hex(color_mix_outline)

        # draw pyramid
        draw_pyramid3d(coord_moving, color, color_outline)
        time.sleep(0.05)
        draw_pyramid3d(coord_moving, "white", "white")
        # reset rotation angle
        rotate_y %= 360

    # animation of rotation and color change
    for i in range(0, 50, 3):
        rotate_y += 5
        # rotate pyramid around center
        coord_moving = rotate_around_center3d(coord_moving, 0, 5, 0)
        # calculate transparency
        a = (100 - i * 2) / 200
        a2 = (100 - i * 2) / 100
        # calculate colors
        color1 = "#{:02X}{:02X}{:02X}".format(r, g, b)
        color2 = "#FFFFFF"
        color1_outline = "#{:02X}{:02X}{:02X}".format(r, g, b)
        rgb1 = mcolors.hex2color(color1)
        rgb2 = mcolors.hex2color(color2)
        rgb1_outline = mcolors.hex2color(color1_outline)
        color_mix = [(c1 * a + c2 * (1 - a)) for c1, c2 in zip(rgb1, rgb2)]
        color_mix = [min(max(c, 0), 1) for c in color_mix]
        color_mix_outline = [(c1 * a2 + c2 * (1 - a2)) for c1, c2 in zip(rgb1_outline, rgb2)]
        color_mix_outline = [min(max(c, 0), 1) for c in color_mix_outline]
        color = mcolors.to_hex(color_mix)
        color_outline = mcolors.to_hex(color_mix_outline)

        # draw pyramid
        draw_pyramid3d(coord_moving, color, color_outline)
        time.sleep(0.05)
        draw_pyramid3d(coord_moving, "white", "white")
        rotate_y %= 360

    # check if mouse clicked, if yes, close window
    if window2.checkMouse():
        flag = False
        window2.close()
