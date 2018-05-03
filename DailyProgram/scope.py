
#LEGB :LOCAL,ENCLOSING,GLOBAL,BUILT IN
class MyClass:
    variable = "blah"
    x="global"
    z="100"
    def function(self):
        global x
        x="123"
       
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"
myobjectx.function();
# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)