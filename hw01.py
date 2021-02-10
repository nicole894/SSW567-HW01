import numbers

def checktypes(a, b, c):

    atype = isinstance(a, numbers.Number)
    btype = isinstance(b, numbers.Number)
    ctype = isinstance(c, numbers.Number)

    if atype and btype and ctype:
        return "Valid"
    else:
        return 'Invalid'

def check_sides(s1, s2, s3):

    sum = s1 + s2
    if sum > s3:
        return True
    else:
        return False


def typeOfTriangle(a, b, c):

    if a == b and b == c:
        return 'Equilateral'
    elif a != b and b != c and c != a:
        return 'Scalene'
    else:
        return 'Isosceles'


def checkRightTriangle(a, b, c):

    sides = [a, b, c]
    sides.sort()
    if sides[2] ** 2 == ((sides[0] ** 2) + (sides[1] ** 2)):
        return 'Right'
    else:
        return 'NotRight'


def classify_triangle(a, b, c):

    dtypes = checktypes(a, b, c)
    if dtypes == 'Invalid':
        return 'Invalid Data'

    ab = check_sides(a, b, c)
    bc = check_sides(b, c, a)
    ca = check_sides(c, a, b)

    if ab and bc and ca:
        pass
    else:
        print("It is not Triangle")
        return 'NotATriangle'

    verdict = checkRightTriangle(a, b, c)
    if verdict == 'Right':
        print("Right angled Triangle")
        return verdict

    tritype = typeOfTriangle(a, b, c)
    print(f"Type of Triangle: {tritype}")
    return tritype


if __name__ == '__main__':
    classify_triangle(3, 4, 5)   # Right Triangle Input
    classify_triangle(6, 6, 6)   # Equilateral
    classify_triangle(7, 7, 9)   # Isosceles
    classify_triangle(8, 3, 7)   # Scalene
    classify_triangle(2, 3, 1)   # Not a Triangle

