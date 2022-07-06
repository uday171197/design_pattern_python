



class RoundPeg:
    def __init__(self,radius) -> None:
        self._radius = radius
        
    def getRadius(self):
        return self._radius
    
class RoundHole(RoundPeg):
    def __init__(self,radius) -> None:
        self._radius = radius
        
    def getRadius(self):
        return self._radius
    
    def fits(self,cls):
        return self._radius >= cls._radius
    
class SquarePeg:
    def __init__(self,width) -> None:
        self._width = width
    
    @property
    def width(self):
        return self._width
    
    
class SquarePegAdepter(SquarePeg):
    def __init__(self,cls):
        self._radius = cls.width*pow(2,0.5)/2
    
    @property
    def radius(self):
        return self._radius
         


hole = RoundHole(5)
rpeg = RoundPeg(5)
hole.fits(rpeg)


small_sqpeg = SquarePeg(5)
large_sqpeg = SquarePeg(10)
hole.fits(small_sqpeg) 

small_sqpeg.width

small_sqpeg_adapter = SquarePegAdepter(small_sqpeg)
large_sqpeg_adapter = SquarePegAdepter(large_sqpeg)
hole.fits(small_sqpeg_adapter) 
hole.fits(large_sqpeg_adapter)


