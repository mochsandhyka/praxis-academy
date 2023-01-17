class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

points = 0
match points:
    case[]:
        print("No points")
    case[Point(0,0)]:
        print("The Origin")
    case[Point(x,y)]:
        print(f"Single point {x},{y}")
    case[Point(0,y1),Point(0,y2)]:
        print(f"Two on the Y axis at {y1},{y2}")
    case _:
        print("Something else")

match points:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not the diagonal")