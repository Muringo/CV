class Circle(object):
    def __init__(self,radius,area,circumference):
        self.radius = radius
        self.area = area
        self.circumference = circumference

    def area(self,r,a):
       r = int(input("radius"));
       a = int(input("area"));
       area = a
       a = self.area
       radius = r
       r = self.radius
       a = 22/7**self.radius
       A = 22/7**r
       return A

    def circumference(self,c):
         circumference = c
         c = self.circumference
         C = 2*22/7*r
         return C


class Square(object):
    """docstring for Square"""
    def __init__(self,a):
        self.a = a

    def area(self,area):
        area = a
        a = self.a
        A = a*a
        return A

    def perimeter(self,s):
        perimeter = s
        s = 4(a)
        P = 4(a)
        return P


class Rectangle(object):
    """docstring for Rectangle"""
    def __init__(self,w,l):
        self.w = w
        self.l = l

    def area(self,q):
        area = q
        q = self.w*self.l
        A = wl
        return A

    def perimeter(self,z):
        perimeter = z
        z = 2*w + 2*l
        P = 2(l + w)
        return P


class Sphere(object):
    """docstring for Sphere"""
    def __init__(self,r):
        self.r = r

    def surface_area(self,m):
        surface_area = m
        m = 4*22/7*r*r
        A = 4*22/7*r*r
        return A
        
    def volume(self,b):
        volume = b
        b = 4/3(22/7*r*r*r)
        V = 4/3(22/7*r*r*r)
        return V
        
        
