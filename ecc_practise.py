p = int(input("enter p: "))
a = int(input("enter a: "))
b = int(input("enter b: "))


listlhs = list()
listrhs = list()

def rhslhs():
    x = 0
    while x<p:
        lhs = (x*x)%p
        listlhs.append(lhs)
        rhs = (x*x*x+a*x+b)%p
        listrhs.append(rhs)
        x+=1
    print(f'lhs {listlhs}')
    print(f'rhs{listrhs}')


def affinePoints():
    point = 0
    i = 0
    for n in listrhs:
        r=0
        for n2 in listlhs:
            if n!=n2:
                r+=1
            else:
                r2=r
                r+=1
                point=r2
                print(f'({i},{point})')
        i+=1


def check(x,y):
    if x==xg:
        return 0
    else:
        return 1
rhslhs()
print("list of affine points: ")
affinePoints()

xg=int(input('enter generator point(xg): '))
yg=int(input('enter generator point(yg): '))

su = (3*pow(xg,2)+a)%p
sd =(2*yg)%p
s = ((su%p)*(pow))