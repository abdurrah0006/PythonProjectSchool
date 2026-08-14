def isempty(s):
    if len(s)==0:
        return True
    else:
        return False
    
def push(s,item):
    s.append(item)
    top=len(s)-1

def pop():
    if isempty(s):
        return ('underflow!')
    else:
        item=s.pop()
        if len(s)==0:
            top=None
        else:
            top=len(s)-1
            return item

def peek(s):
    if isempty(s):
        return 'underflow'
    else:
        top=len(s)-1
        return s[top]

def display(s):
    if isempty(s):
        print('sorry no item stack')
    else:
        t=len(s)-1
        print('(top)',end=' ')
        while(t>=0):
            print(s[t],'<==top')
            for i in range(top-1,-1,-1):
                print(s[i])
            t-=1    
        print()
s=[]
top=None
while True:
    print('....STACK IMPLEMENTED....')
    print('1.push')
    print('2.pop')
    print('3.display')
    print('4.peek')
    print('0.exit')
    ch=int(input('enter choice:'))
    if ch==1:
        val=int(input('enter item to push:'))
        push(s,iter)
    elif ch==2:
        val=pop()
        if val=='underflow':
            print('underflow!empty stack')
        else:
            ('\ndeleted item was;',val)
    elif ch==3:
        item=peek(s)
        if item=='underflow':
            print('underflow!empty stack')
        else:
            print('Top Item:',val)
    elif ch==4:
        display(s)
    elif ch==0:
        print('Bye')
        Break

        
