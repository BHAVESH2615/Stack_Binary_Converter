from  Stackk import Stack

def Binary(no):
    s = Stack()
    while no>0:
        rem=no%2
        s.push(rem)
        no=no//2

    lst=""
    while not s.is_empty():
        lst += str(s.pop())
    return lst


if __name__ == '__main__':
    while True:
        no=int(input("Enter the Number:- "))
        print(Binary(no))
