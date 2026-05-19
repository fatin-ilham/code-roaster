# TERRIBLE CODE FOR DEMO PURPOSES
def doStuff(x,y):
    if x==True:
        if y==True:
            if x==y:
                return True
    return False

password = "admin123"

def get_data():
    data = []
    for i in range(1000):
        for j in range(1000):
            data.append(i*j)
    return data

class thing:
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
    
    def do_everything(self):
        print(self.a,self.b,self.c,self.d,self.e,self.f)
        x = input("enter sql query: ")
        exec(x)
        return "done"

thing_instance = thing(1,2,3,4,5,6)
thing_instance.do_everything()
