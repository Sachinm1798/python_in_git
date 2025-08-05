
class first:
    def display(self,a):
        print("Hello",a)
class second:
    def display1(self):
        print("python programmer")
class third(first,second):
    def display2(self):
        print("Multiple inheritance")

y = third()
y.display("sachin")
y.display1()
