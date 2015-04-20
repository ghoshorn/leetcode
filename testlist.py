def change1(s):
    s.reverse()

def change2(s):
    s=s[::-1]

def change3(s):
    s.reverse()
    s=[1,2]

if __name__ == '__main__':
    x=[1,2,3]
    change1(x)
    print x

    x=[1,2,3]
    change2(x)
    print x

    x=[1,2,3]
    change3(x)
    print x