def collinear(x1,y1,x2,y2,x3,y3):
    print("Collinear" if (y2 - y1)*(x3 - x2) == (y3 - y2)*(x2 - x1) else "Not Collinear")
