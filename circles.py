import matplotlib.pyplot as plt
import numpy as np


# =========================
# 1. Bresenham Circle
# =========================
def bresenham_circle(xc, yc, r):
    xk = 0
    yk = r
    pk = 3 - 2 * r

    points = []

    while xk <= yk:
        # Step: plot current point
        points.append((xc + xk, yc + yk))

        # Step: check pk
        if pk < 0:
            # Case 1
            x_next = xk + 1
            y_next = yk

            # update pk
            pk = pk + 4 * x_next + 6

        else:
            # Case 2
            x_next = xk + 1
            y_next = yk - 1

            # update pk
            pk = pk + 4 * (x_next - y_next) + 10

        # move to next point
        xk = x_next
        yk = y_next

    return points


# =========================
# 2. Midpoint Circle
# =========================
def midpoint_circle(xc, yc, r):
    xk = 0
    yk = r
    pk = 1 - r

    points = []

    while xk <= yk:
        points.append((xc + xk, yc + yk))

        if pk < 0:
            # Case 1
            x_next = xk + 1
            y_next = yk

            pk = pk + 2 * x_next + 1

        else:
            # Case 2
            x_next = xk + 1
            y_next = yk - 1

            pk = pk + 2 * x_next - 2 * y_next + 1

        xk = x_next
        yk = y_next

    return points


# =========================
# 3. Midpoint Ellipse
# =========================
def midpoint_ellipse(xc, yc, rx, ry):
    points = []

    # initial point
    xk = 0
    yk = ry

    rx2 = rx * rx
    ry2 = ry * ry

    # ================= REGION 1 =================
    pk = ry2 - (rx2 * ry) + (0.25 * rx2)

    dx = 2 * ry2 * xk
    dy = 2 * rx2 * yk

    while dx < dy:
        points.append((xc + xk, yc + yk))

        if pk < 0:
            # Case 1
            x_next = xk + 1
            y_next = yk

            pk = pk + (2 * ry2 * x_next) + ry2

        else:
            # Case 2
            x_next = xk + 1
            y_next = yk - 1

            pk = pk + (2 * ry2 * x_next) - (2 * rx2 * y_next) + ry2

        xk = x_next
        yk = y_next

        dx = 2 * ry2 * xk
        dy = 2 * rx2 * yk

    # ================= REGION 2 =================
    pk = (ry2 * (xk + 0.5)**2) + (rx2 * (yk - 1)**2) - (rx2 * ry2)

    while yk >= 0:
        points.append((xc + xk, yc + yk))

        if pk > 0:
            # Case 1
            x_next = xk
            y_next = yk - 1

            pk = pk - (2 * rx2 * y_next) + rx2

        else:
            # Case 2
            x_next = xk + 1
            y_next = yk - 1

            pk = pk + (2 * ry2 * x_next) - (2 * rx2 * y_next) + rx2

        xk = x_next
        yk = y_next

    return points




def expand_circle(points, xc=0, yc=0):
    full_points = []

    for (x, y) in points:
        full_points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x),
        ])

    return list(set(full_points))