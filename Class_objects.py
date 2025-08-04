class Myteam:
      def __init__(self,name,age,place):
           self.x = name
           self.y = age
           self.z = place
   
      def display(self):
           print("Name : ",self.x)
           print("Age : ",str(self.y))
           print("Place : ",self.z)
      def relocate(self,a):
          self.z = a
      @staticmethod
      def hello():
          print("Hello Welcome to Class and Objects")

Myteam.hello()
print("----------")
x = Myteam("Sachin",27,"Palakkad")
y = Myteam("Rishad",25,"Calicat")
x.display()
print("---------------------------------------------------")
y.display()
print("---------------------------------------------------")
x.relocate("Mumbai")
y.relocate("Goa")
x.display()
print("---------------------------------------------------")
y.display()
print("----------------------------------------------------")
x.add_age()
y.add_age()
x.display()
print("---------------------------------------------------")
y.display()
print("----------------------------------------------------")

