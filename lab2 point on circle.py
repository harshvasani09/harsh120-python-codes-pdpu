def point_circle(x, y, cx, cy, r):
    from math import sqrt
    d = sqrt((x - cx)**2 + (y - cy)**2)
    print("Inside" if d < r else "On" if d == r else "Outside")
