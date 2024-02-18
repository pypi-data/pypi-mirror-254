"""
Auxiliary module for carrying out 3D Vec3 operations

It contemplates Vec3 operations 

"""

import math as m

class Vec3:
    """
    Implement a 3D metric Vec3 space
    """

    def __init__(self, *args):
        """Construct a Vec3 using three coordinates that can be
        packed into a single list or tuple.
        """
        if len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
        else:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
    
    @property
    def coords(self):
        """
        Returns the coordinates as a tuple
        """
        return self.x, self.y, self.z
    
    def tuple(self):
        return self.coords
    
    def __str__(self):
        return "(%8.4f %8.4f %8.4f)" % (self.x, self.y, self.z)
    
    def __repr__(self):
        return repr((self.x,self.y,self.z))
    
    def __add__(self, other):
        if isinstance(other, tuple):
            return (other[0], self.x + other[1], self.y + other[2],
                self.z + other[3])
        else:
            return Vec3(self.x+other.x, self.y+other.y, self.z+other.z)
            
    def __radd__(self, other):
        if isinstance(other, tuple):
            return (other[0], self.x + other[1], self.y + other[2],
                self.z + other[3])
        else:
            return Vec3(self.x+other.x, self.y+other.y, self.z+other.z)
        
    
    def __comp__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __div__(self, number):
        return Vec3(self.x/number, self.y/number, self.z/number)
    
    def __sub__(self, other):
        if isinstance(other, tuple):
            return (other[0], self.x - other[1], self.y - other[2],
                self.z - other[3])
        else:
            return Vec3(self.x-other.x, self.y-other.y, self.z-other.z)

    def __rsub__(self, other):
        if isinstance(other, tuple):
            return (other[0], other[1] - self.x , other[2] - self.y,
                other[3]-self.z)
        else:
            return Vec3(other.x-self.x, other.y-self.y, other.z-self.z)

    
    def __rmul__(self, number):
        return Vec3(self.x*number, self.y*number, self.z*number)
    
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)
    
    def copy(self):
        return Vec3(self.x, self.y, self.z)
    
    def xrotate(self, theta):
        ct = m.cos(theta)
        st = m.sin(theta)
        ny = self.y*ct - self.z*st
        nz = self.y*st + self.z*ct
        self.y = ny
        self.z = nz
        return self
    
    def yrotate(self, theta):
        ct = m.cos(theta)
        st = m.sin(theta)
        nx = self.x*ct + self.z*st
        nz = -self.x*st + self.z*ct
        self.x = nx
        self.z = nz
        return self
    
    def zrotate(self, theta):
        ct = m.cos(theta)
        st = m.sin(theta)
        nx = self.x*ct - self.y*st
        ny = self.x*st + self.y*ct
        self.x = nx
        self.y = ny
        return self
    
    def xmirror(self):
        self.x = -self.x
        return self
    
    def ymirror(self):
        self.y = -self.y
        return self

    def zmirror(self):
        self.z = -self.z
        return self

    def __abs__(self):
        return m.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    
    def translate(self, v):
        self.x += v.x
        self.y += v.y
        self.z += v.z
        return self
    
    def invert(self):
        self.x =- self.x
        self.y =- self.y
        self.z =- self.z
        return self
    
    def rescale(self, value):
        self.x *= value
        self.y *= value
        self.z *= value
        return self
     

def toVec3(v):
    """Convert a list or tuble to a Vec3"""
    if isinstance(v, Vec3):
        return v.copy()
    else:
        return Vec3(*v)


def xrotate(p, theta):
    """Return a new Vec3 after performing a rotation on p around
    the x axis"""
    p = p.copy()
    return p.xrotate(theta)

def yrotate(p, theta):
    """Return a new Vec3 after performing a rotation on p around
    the y axis"""
    p = p.copy()
    return p.yrotate(theta)

def zrotate(p,theta):
    """Return a new Vec3 after performing a rotation on p around
    the x axis"""
    p = p.copy()
    return p.zrotate(theta)

def xmirror(p):
    """Return a new Vec3 after performing a specular reflection on p
    on the yz plane"""
    p = p.copy()
    return p.xmirror()

def ymirror(p):
    """Return a new Vec3 after performing a specular reflection on p
    on the xz plane"""
    p = p.copy()
    return p.ymirror()


def zmirror(p):
    """Return a new Vec3 after performing a specular reflection on p
    on the xy plane"""
    p = p.copy()
    return p.zmirror()

def translate(p,v):
    """Return a new Vec3 after performing a translation along the
    Vec3 v
    """
    p = p.copy()
    return p.translate(v)

def invert(p):
    """Perform an inversion"""
    p = p.copy()
    return p.invert()

def rescale(p, a):
    """Rescale p by a factor a"""
    p = p.copy()
    return p.scale(a)


def dist(p1, p2):
    """Distance between p1 and p2"""
    return abs(p2 - p1)

def dist2(p1,p2):
    """Square of the distance between p1 and p2"""
    return (p1.x-p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2

def scalar(p1, p2):
    """Scalar product between p1 and p2"""
    return p1.x*p2.x + p1.y*p2.y + p1.z*p2.z

def vprod(p1, p2):
    """Cross product between p1 and p2"""
    return Vec3(p1.y*p2.z - p1.z*p2.y,
                  p1.z*p2.x - p1.x*p2.z,
                  p1.x*p2.y - p1.y*p2.x)

def triple(p1, p2, p3):
    """Triple product of p1, p2, and p3"""
    return scalar(vprod(p1, p2), p3)

def angle(p1, p2):
    """Return the angle between two Vec3s in radians"""
    r = scalar(p1, p2)/(abs(p1)*abs(p2))
    if r > 1.:
        r = 1.
    elif r < -1.:
        r = -1.
    return m.acos(r)

def getangle(ct, st):
    """Return the angle given the cosine and sine of an angle"""
    t = m.acos(ct)
    if st < 0:
        t=-t
    return t
    
    

   
