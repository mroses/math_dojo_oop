
class MathDojo(object):
    def __init__(self):
        self.numtotal = 0

    def add(self, *numbers):
        for x in numbers:
            if type(x) == int:
                self.numtotal += x
            else: 
                self.numtotal += sum(x)
        return self
    
    def subtract(self, *numbers):
        for x in numbers:
            if type(x) == int:
                self.numtotal -= x
            else:
                self.numtotal -= sum(x)
        return self

    def result(self):
        return self.numtotal

md=MathDojo()
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()

'''
class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
            else:
                self.result += i
        return self
'''