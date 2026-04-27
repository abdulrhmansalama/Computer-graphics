def dda(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps
    x = x0
    y = y0
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc
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
    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    x = x0
    y = y0
    while x <= x1:
        points.append((x, y))
        if d < 0:
            d = d + 2 * dy
        else:
            y += 1
            d = d + 2 * (dy - dx)
        x += 1
    return points