'''
Created on Jan 2, 2017

@author: sidtyagi
'''
class MaxSizeList(object):
    def __init__(self,val):
        self.max_ele=val
        self.val=[]
    def push(self,val):        
        self.val.append(val)
    def get_list(self):                
        #return self.val[0:self.max_ele]
        return self.val[-self.max_ele:]


a=MaxSizeList(3)
b=MaxSizeList(1)

a.push('hh1')
a.push('hh2')
a.push('hh3')
a.push('hh4')
a.push('hh5')

b.push('ab1')
b.push('ab2')
b.push('ab3')
b.push('ab4')
b.push('ab5')

print a.get_list()
print b.get_list()