def dda_line(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    # حساب الميل
    m = dy / dx
    x = x0
    y = y0
    points.append((round(x), round(y)))
    # نكرر لحد ما نوصل للنقطة النهائية
    while x < x1 or y < y1:
        # الحالة 1: m < 1
        if m < 1:
            x_new = x + 1
            y_new = y + m
        # الحالة 2: m > 1
        elif m > 1:
            y_new = y + 1
            x_new = x + (1 / m)
        # الحالة 3: m = 1
        else:
            x_new = x + 1
            y_new = y + 1
        x = x_new
        y = y_new
        points.append((round(x), round(y)))
    return points


def bresenham(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    p = 2 * dy - dx
    x = x0
    y = y0
    while x <= x1:
        points.append((x, y))
        if p < 0:
            p = p + 2 * dy
        else:
            y += 1
            p = p + 2 * dy - 2 * dx
        x += 1
    return points

def midpoint_line(x0, y0, x1, y1):
    points = []
    # Step 01: حساب ΔX و ΔY
    dx = x1 - x0
    dy = y1 - y0
    # Step 02: حساب Dinitial و ΔD
    D = 2 * dy - dx
    delta_D = 2 * (dy - dx)
    xk = x0
    yk = y0
    points.append((xk, yk))
    # Step 03 + Step 04
    for _ in range(dx):
        # Case 01: D < 0
        if D < 0:
            xk = xk + 1
            yk = yk
            D = D + 2 * dy
        # Case 02: D >= 0
        else:
            xk = xk + 1
            yk = yk + 1
            D = D + delta_D
        points.append((xk, yk))
    return points
