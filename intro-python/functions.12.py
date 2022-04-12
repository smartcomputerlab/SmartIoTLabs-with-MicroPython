
def getFunction(full=True):
     'Outer Function'
     print(getFunction.__doc__)
     
     def p(frm=0, to=1, step=1):
         'Inner Function'
         print(p.__doc__)
         return (x ** 3 for x in range(frm, to, step))
     
     if (full):
         return p
     else:
         return lambda frm = 0, to = 1, step = 1: (x ** 3 \
              for x in range(frm, to, step))

print(__doc__)
t = getFunction()
print("Check the elaborate function")
for v in t(step=1, to=10):
     print(v)
t = getFunction(False)
print("Check the lambda function")
for v in t(1, 5):
    print(v)