class dict_parsing:
    def __init__(self,a):
        self.a=a
     
    def notdict(self):
        if type(self.a)!= dict:
            raise Exception(self.a, "Not a dictionary")
            
        return 1
        
    def getkeys(self):
        if self.notdict():
            return list(self.a.keys())
    
    def getvalues(self):
        if self.notdict():
            return list(self.a.values())
        
    def userinputs(self):
        self.a = eval(input())
        print(self.a , type(self.a))
        print(self.getkeys())
        print(self.getvalues())
        
    def insertion(self,k,v):
        self.a[k]=v
       
       
class dict_parsing2:
    def __init__(self,a):
        self.a=a
     
    def notdict(self):
        if type(self.a)!= dict:
            raise Exception(self.a, "Not a dictionary")
            
        return 1
        
    def getkeys(self):
        if self.notdict():
            return list(self.a.keys())
    
    def getvalues(self):
        if self.notdict():
            return list(self.a.values())
        
    def userinputs(self):
        self.a = eval(input())
        print(self.a , type(self.a))
        print(self.getkeys())
        print(self.getvalues())
        
    def insertion(self,k,v):
        self.a[k]=v
        