import math

# -------- Translation --------
def translate_2d(point, tx, ty):
    x, y = point
    return x + tx, y + ty


# -------- Scaling --------
def scale_2d(point, sx, sy):
    x, y = point
    return sx * x, sy * y


# -------- Rotation --------
def rotate_2d(point, theta):
    x, y = point
    theta = math.radians(theta)
    x_new = x * math.cos(theta) - y * math.sin(theta)
    y_new = x * math.sin(theta) + y * math.cos(theta)
    return x_new, y_new


# -------- Reflection --------
def reflect_2d(point, axis):
    x, y = point
    if axis == "x":
        return x, -y
    elif axis == "y":
        return -x, y
    elif axis == "origin":
        return -x, -y
    else:
        raise ValueError("axis must be x, y, or origin")


# -------- Shearing --------
def shear_2d(point, shx=0, shy=0):
    x, y = point
    return x + shx * y, y + shy * x


# ================== 3D ==================

# -------- Translation --------
def translate_3d(point, tx, ty, tz):
    x, y, z = point
    return x + tx, y + ty, z + tz


# -------- Scaling --------
def scale_3d(point, sx, sy, sz):
    x, y, z = point
    return sx * x, sy * y, sz * z


# -------- Rotation X --------
def rotate_x(point, theta):
    x, y, z = point
    theta = math.radians(theta)
    y_new = y * math.cos(theta) - z * math.sin(theta)
    z_new = y * math.sin(theta) + z * math.cos(theta)
    return x, y_new, z_new


# -------- Rotation Y --------
def rotate_y(point, theta):
    x, y, z = point
    theta = math.radians(theta)
    x_new = x * math.cos(theta) + z * math.sin(theta)
    z_new = -x * math.sin(theta) + z * math.cos(theta)
    return x_new, y, z_new


# -------- Rotation Z --------
def rotate_z(point, theta):
    x, y, z = point
    theta = math.radians(theta)
    x_new = x * math.cos(theta) - y * math.sin(theta)
    y_new = x * math.sin(theta) + y * math.cos(theta)
    return x_new, y_new, z


# -------- Reflection --------
def reflect_3d(point, axis):
    x, y, z = point
    if axis == "x":
        return x, -y, -z
    elif axis == "y":
        return -x, y, -z
    elif axis == "z":
        return -x, -y, z
    else:
        raise ValueError("axis must be x, y, or z")


# -------- Shearing (X-direction) --------
def shear_3d_x(point, shy=0, shz=0):
    x, y, z = point
    return x, y + shy * x, z + shz * x