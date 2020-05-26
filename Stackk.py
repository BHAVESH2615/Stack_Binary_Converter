class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return  self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
if __name__ == '__main__':

    s=Stack()
    while True:
        print("select appropriate option....")
        print("1.Stack is Empty or not\t2.Push\t3.Pop\t4.Peek\t5.Quit")
        op=int(input("enter the Value you want to Add:- "))
        if op==1:
            print(s.is_empty())
        elif op==2:
            add=input("Enter The Value want to add:- ")
            s.push(add)
            print(s.get_stack())
        elif op==3:
            s.pop()
            print(s.get_stack())
        elif op==4:
            print(s.peek())
        elif op==5:
            exit()
        else:
            print("enter Valid Output...!")

