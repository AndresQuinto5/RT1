#AndresEmilioQ - 18288
#RT1 Esferas
import struct
from gl import color

class Texture(object):
    
    def __init__(self, path):
        self.path = path
        self.readTexture()
    
    def readTexture(self):
        
        img = open(self.path, 'rb')
        img.seek(2 + 4 + 4)
        header_size = struct.unpack('=l', img.read(4))[0]
        img.seek(2 + 4 + 4 + 4 + 4)

        self.width = struct.unpack('=l', img.read(4))[0]
        self.height = struct.unpack('=l', img.read(4))[0]
        self.pixels = []
        
        img.seek(header_size)

        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(img.read(1))
                g = ord(img.read(1))
                r = ord(img.read(1))
                self.pixels[y].append(color(r, g, b))
        
        img.close()
    
    def getColor(self, tx, ty, intensity = 1):

        x = int(tx * self.width)
        y = int(ty * self.height)

        try:
            return bytes(
                map(
                    lambda b: round(b * intensity) if b * intensity > 0 else 0,
                    self.pixels[y][x]
                )
            )
        except IndexError:
            return bytes(
                map(
                    lambda t: int(round(t*intensity)) if (t * intensity) > 0 else 0,
                    self.pixelesBuffer[y-1][x-1]
                )
            )
    
    def getDimensions(self):

        return self.height, self.width