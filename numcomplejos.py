from sys import stdin
import math

def suma(c1,c2):
    resp=[0,0]
    resp[0]=int(c1[0])+int(c2[0])
    resp[1]=int(c1[1])+int(c2[1])
    t=(resp[0],resp[1])
    r=''
    if t[0]==0:
        if t[1]==0:
            r+=str(t[0])
        else:
            r+=str(t[1])+'i'
    else:
        if t[1]==0:
            r+=str(t[0])
        else:
            if t[1]>0:
                r+=str(t[0])+'+'+str(t[1])+'i'
            else:
                r+=str(t[0])+str(t[1])+'i'
    return r

def resta(c1,c2):
    resp=[0,0]
    resp[0]=int(c1[0])-int(c2[0])
    resp[1]=int(c1[1])-int(c2[1])
    t=(resp[0],resp[1])
    r=''
    if t[0]==0:
        if t[1]==0:
            r+=str(t[0])
        else:
            r+=str(t[1])+'i'
    else:
        if t[1]==0:
            r+=str(t[0])
        else:
            if t[1]>0:
                r+=str(t[0])+'+'+str(t[1])+'i'
            else:
                r+=str(t[0])+str(t[1])+'i'
    return r

def mult(c1,c2):
    resp=[0,0]
    resp[0]=int(c1[0])*int(c2[0])+((int(c1[1])*int(c2[1]))*-1)
    resp[1]=int(c1[0])*int(c2[1])+int(c1[1])*int(c2[0])
    t=(resp[0],resp[1])
    r=''
    if t[0]==0:
        if t[1]==0:
            r+=str(t[0])
        else:
            r+=str(t[1])+'i'
    else:
        if t[1]==0:
            r+=str(t[0])
        else:
            if t[1]>0:
                r+=str(t[0])+'+'+str(t[1])+'i'
            else:
                r+=str(t[0])+str(t[1])+'i'
    return r

def bonito(c2):
    x=''
    if int(c2[0])==0:
        if int(c2[1])==0:
            x+='0'
        else:
            x+=str(c2[1])+'i'
    else:
        if int(c2[1])==0:
            x+=str(c2[0])
        elif int(c2[1])>0:
            x+=str(c2[0])+'+'+str(c2[1])+'i'
        else:
            x+=str(c2[0])+str(c2[1])+'i'
    return x

def div(c1,c2):
    c3=[0,0]
    c3[0]=int(c2[0])
    c3[1]=int(c2[1])*-1
    x=mult(c1,c3)
    y=mult(c2,c3)
    return x+'/'+y

def modulo(c1):
    x=bonito(c1)
    a=((int(c1[0])**2)+(int(c1[1])**2))**(1/2)
    return a
    


def conj(c1):
    resp=[0,0]
    resp[0]=int(c1[0])
    resp[1]=int(c1[1])*-1
    x=bonito(resp)
    return x

def polar(c1):
    r=((float(c1[0])**2)+(float(c1[1])**2))**(1/2)
    a=math.atan(float(c1[1])/float(c1[0]))
    coord=(r,a)
    return coord

def cart(c1):
    resp=[0,0]
    resp[0]=(float(c1[0])*math.cos(float(c1[1])))
    resp[1]=(float(c1[0])*math.sin(float(c1[1])))
    x=bonito(resp)
    return x
    
def sumatrices(m1,m2):
    res=[]
    
    for i in range(len(m1)):
        f=[]
        for j in range(len(m1[0])):
            x=suma((m1[i][j]),(m2[i][j]))
            f.append(x)
        res.append(f)
    return res


def matrinv(m):
    return escalar((-1,0),m)

def escalar(e,m):
    mn=[]
    for i in range(len(m)):
        f=[]
        for j in range(len(m[i])):
            f.append(mult(e,m[i][j]))
        mn.append(f)
    return mn

def transpuesta(m,dm):
    t=[]
    i=int(dm[0])
    j=int(dm[1])
    x=0
    while x< j:
        f=[]
        y=0
        while y<i:
            f.append(bonito(m[y][x]))
            y+=1
        x+=1
        t.append(f)

    return t

def matrizconj(m):
    res=[]
    for i in range(len(m)):
        f=[]
        for j in range(len(m[i])):
            f.append(conj(m[i][j]))
        res.append(f)
    return res

def normatriz(m,dm):
    m1=[]
    fil=int(dm[0])
    col=int(dm[1])
    x=0
    while x< col:
        f=[]
        y=0
        while y<fil:
            f.append(m[y][x])
            y+=1
        x+=1
        m1.append(f)

    r=[]
    for i in range(len(m1)):
        f=[]
        for j in range(len(m1)):
            v1=m1[i]
            v2=m1[j]
            f.append(dual(v1,v2))
        r.append(f)
    n=(0,0)
    for i in range(len(r)):
        for j in range(len(r[i])):
            if i==j:
                n=sumar(n,r[i][j])
            else:
                continue
    if n[1]==0:
        x=math.sqrt(int(n[0]))
        return x
    else:
        y='('+bonito(n)+')**(1/2)'
        return y
            
    
    
def dual(v1,v2):
    t=[]
    for i in range(len(v1)):
        x=multiplica(v1[i],v2[i])
        t.append(x)
    while len(t)>1:
        y=sumar(t[0],t[1])
        t.pop(0)
        t.pop(0)
        t.insert(0,y)
    return t[0]

def sumar(c1,c2):
    resp=[0,0]
    resp[0]=int(c1[0])+int(c2[0])
    resp[1]=int(c1[1])+int(c2[1])
    t=(resp[0],resp[1])
    return t
    
def multiplica(c1,c2):
    resp=[0,0]
    resp[0]=int(c1[0])*int(c2[0])+((int(c1[1])*int(c2[1]))*-1)
    resp[1]=int(c1[0])*int(c2[1])+int(c1[1])*int(c2[0])
    t=(resp[0],resp[1])
    return t

def conjugado(c1):
    resp=[0,0]
    resp[0]=int(c1[0])
    resp[1]=int(c1[1])*-1
    return resp

def maconj(m):
    res=[]
    for i in range(len(m)):
        f=[]
        for j in range(len(m[i])):
            f.append(conjugado(m[i][j]))
        res.append(f)
    return res

def adjmatriz(m,dm):
    return transpuesta(maconj(m),dm)


    
def dismat(m1,m2,d1):
    m1t=[]
    i=int(d1[0])
    j=int(d1[1])
    x=0
    while x< j:
        f=[]
        y=0
        while y<i:
            f.append(m1[y][x])
            y+=1
        x+=1
        m1t.append(f)
    total=[]
    for k in range(len(m1t)):
        for i in range(len(m1t[k])):
            x=multiplica(m1t[k][i],m2[k][i])
            total.append(x)
        while len(total)>1:
            y=sumar(total[0],total[1])
            total.pop(0)
            total.pop(0)
            total.insert(0,y)
    return bonito(total[0])

def unita(m):
    mt=[]
    i=int(d1[0])
    j=int(d1[1])
    x=0
    while x< j:
        f=[]
        y=0
        while y<i:
            f.append(m[y][x])
            y+=1
        x+=1
        mt.append(f)

def hermitian(m,dm):
    x=adjunma(m,dm)
    if m ==x:
        return True
    else:
        return False

    
def tra(m,dm):
    t=[]
    i=int(dm[0])
    j=int(dm[1])
    x=0
    while x< j:
        f=[]
        y=0
        while y<i:
            f.append(m[y][x])
            y+=1
        x+=1
        t.append(f)

    return t

def adjunma(m,dm):
    return tra(maconj(m),dm)

def tensor(m1,m2):
    resp=[]
    for i in range(len(m1)):
        f=[]
        for j in range(len(m1[i])):
            temp=m2
            x=escalar(m1[i][j],m2)
            f.append(x)
        y=union(f[0],f[1])
        resp.append(y[0])
        resp.append(y[1])
    return resp


def union(m1,m2):
    r=[]
    for i in range(len(m1)):
        f=[]
        for j in m1[i]:
            f.append(j)
        for k in m2[i]:
            f.append(k)
        r.append(f)
    return r
            

