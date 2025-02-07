class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,v2):
        x=self.x+v2.x
        y=self.y+v2.y
        z=self.z+v2.z
        return vector(x,y,z)
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
v1=vector(1,2,3)
v2=vector(5,6,7)
print("sum of vectors:")
print(v1+v2)