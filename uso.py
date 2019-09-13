from sys import stdin
import numcomplejos

def main():
    while True:
        print('digite la operación que desea realizar')
        print('OPERACIONES:')
        print('0. Salir')
        print('1. Suma de complejos')
        print('2. Resta de complejos')
        print('3. Multiplicación de complejos')
        print('4. División de complejos')
        print('5. El módulo de un complejo')
        print('6. El conjugado de un complejo')
        print('7. Convertir un complejo de cartesiano a polar')
        print('8. Convertir un complejo de polar a cartesiano')
        print('9. Suma de matrices complejas')
        print('10. Inversa de matrices complejas')
        print('11. Multiplicación escalar de matrices complejas')
        print('12. Matriz transpuesta')
        print('13. Matriz conjugada')
        print('14. Matriz adjunta')
        print('15. Calcular la "Acción" de una matriz')
        print('16. Norma de una matriz')
        print('17. Distancia entre matrices')
        print('18. Revisar si la matriz es unaria')
        print('19. Revisar si la matriz es hermitian')
        print('20. Producto tensor')

        opc=int(stdin.readline().strip())
        if opc==0:
            break
        
        if opc == 1:
            c1=tuple(stdin.readline().strip().split(','))
            c2=tuple(stdin.readline().strip().split(','))
            print(numcomplejos.suma(c1,c2))
        elif opc ==2:
            c1=tuple(stdin.readline().strip().split(','))
            c2=tuple(stdin.readline().strip().split(','))
            print(numcomplejos.resta(c1,c2))
        elif opc == 3:
            c1=tuple(stdin.readline().strip().split(','))
            c2=tuple(stdin.readline().strip().split(','))
            print(numcomplejos.mult(c1,c2))
        elif opc==4:
            c1=tuple(stdin.readline().strip().split(','))
            c2=tuple(stdin.readline().strip().split(','))
            print(numcomplejos.div(c1,c2))
        elif opc==5:
            c1=tuple(stdin.readline().strip().split(','))
            print(numcomplejos.modulo(c1))
        elif opc==6:
            c1=tuple(stdin.readline().strip().split(','))
            print(numcomplejos.conj(c1))
        elif opc == 7:
            c1=tuple(stdin.readline().strip().split(','))
            print(numcomplejos.polar(c1))
        elif opc==8:
            c1=tuple(stdin.readline().strip().split(','))
            print(numcomplejos.cart(c1))

        elif opc==9:
            print('Digite las dimensiones de las matrices: ')
            d1=tuple(stdin.readline().strip().split(','))
            d2=tuple(stdin.readline().strip().split(','))
            if d1!=d2:
                print('Las matrices no pueden ser sumadas')
            else:
                m1=[]
                m2=[]
                for i in range(int(d1[0])):
                    f=[]
                    x=int(d1[1])
                    print('digite los elementos de la fila de la primera matriz')
                    while x > 0:
                        y=tuple(stdin.readline().strip().split(','))
                        f.append(y)
                        x-=1
                    m1.append(f)

                for j in range(int(d1[0])):
                    f=[]
                    x=int(d1[1])
                    print('digite los elementos de la fila de la segunda matriz')
                    while x > 0:
                        y=tuple(stdin.readline().strip().split(','))
                        f.append(y)
                        x-=1
                    m2.append(f)
                print(numcomplejos.sumatrices(m1,m2))
                
        elif opc ==10:
            print('Digite las dimensiones de la matriz')
            dm=tuple(stdin.readline().strip().split(','))
            m=[]
            signo=[]
            for j in range(int(dm[0])):
                f=[]
                x=int(dm[1])
                print('digite los elementos de la fila de la matriz')
                while x > 0:
                    y=tuple(stdin.readline().strip().split(','))
                    f.append(y)
                    x-=1
                m.append(f)
            print(numcomplejos.matrinv(m))

        elif opc==11:
            print('digite el escalar')
            e=tuple(stdin.readline().strip().split(','))
            print('Digite las dimensiones de la matriz')
            dm=tuple(stdin.readline().strip().split(','))
            m=[]
            for j in range(int(dm[0])):
                f=[]
                x=int(dm[1])
                print('digite los elementos de la fila de la matriz')
                while x > 0:
                    y=tuple(stdin.readline().strip().split(','))
                    f.append(y)
                    x-=1
                m.append(f)

            print(numcomplejos.escalar(e,m))

        elif opc ==12:
            print('Digite las dimensiones de la matriz')
            dm=tuple(stdin.readline().strip().split(','))
            m=[]
            for j in range(int(dm[0])):
                f=[]
                x=int(dm[1])
                print('digite los elementos de la fila de la matriz')
                while x > 0:
                    y=tuple(stdin.readline().strip().split(','))
                    f.append(y)
                    x-=1
                m.append(f)

            print(numcomplejos.transpuesta(m,dm))

        elif opc ==13:
            print('Digite las dimensiones de la matriz')
            dm=tuple(stdin.readline().strip().split(','))
            m=[]
            for j in range(int(dm[0])):
                f=[]
                x=int(dm[1])
                print('digite los elementos de la fila de la matriz')
                while x > 0:
                    y=tuple(stdin.readline().strip().split(','))
                    f.append(y)
                    x-=1
                m.append(f)

            print(numcomplejos.matrizconj(m))

        elif opc==14:
            print('Digite las dimensiones de la matriz')
            dm=tuple(stdin.readline().strip().split(','))
            m=[]
            signo=[]
            for j in range(int(dm[0])):
                f=[]
                x=int(dm[1])
                print('digite los elementos de la fila de la matriz')
                while x > 0:
                    y=tuple(stdin.readline().strip().split(','))
                    f.append(y)
                    x-=1
                m.append(f)
            print(numcomplejos.adjmatriz(m,dm))

        elif opc==15:
            print('Digite las dimensiones de la matriz')
            dm=tuple(stdin.readline().strip().split(','))
            m=[]
            for j in range(int(dm[0])):
                f=[]
                x=int(dm[1])
                print('digite los elementos de la fila de la matriz')
                while x > 0:
                    y=tuple(stdin.readline().strip().split(','))
                    f.append(y)
                    x-=1
                m.append(f)

            print(numcomplejos.normatriz(m,dm))
        
        elif opc==16:
            print('Digite las dimensiones de la matriz')
            dm=tuple(stdin.readline().strip().split(','))
            m=[]
            for j in range(int(dm[0])):
                f=[]
                x=int(dm[1])
                print('digite los elementos de la fila de la matriz')
                while x > 0:
                    y=tuple(stdin.readline().strip().split(','))
                    f.append(y)
                    x-=1
                m.append(f)

            print(numcomplejos.normatriz(m,dm))

        elif opc==17:
            print('Digite las dimensiones de las matrices: ')
            d1=tuple(stdin.readline().strip().split(','))
            d2=tuple(stdin.readline().strip().split(','))
            if d1!=d2:
                print('Las matrices deben tener las mismas dimensiones')
            else:
                m1=[]
                m2=[]
                for i in range(int(d1[0])):
                    f=[]
                    x=int(d1[1])
                    print('digite los elementos de la fila de la primera matriz')
                    while x > 0:
                        y=tuple(stdin.readline().strip().split(','))
                        f.append(y)
                        x-=1
                    m1.append(f)

                for j in range(int(d1[0])):
                    f=[]
                    x=int(d1[1])
                    print('digite los elementos de la fila de la segunda matriz')
                    while x > 0:
                        y=tuple(stdin.readline().strip().split(','))
                        f.append(y)
                        x-=1
                    m2.append(f)
                print(numcomplejos.dismat(m1,m2,d1))

        elif opc==18:
            print('Digite las dimensiones de la matriz')
            dm=tuple(stdin.readline().strip().split(','))
            m=[]
            identidad=[]
            for j in range(int(dm[0])):
                f=[]
                x=int(dm[1])
                print('digite los elementos de la fila de la matriz')
                while x > 0:
                    y=tuple(stdin.readline().strip().split(','))
                    f.append(y)
                    x-=1
                m.append(f)
            z=('1','0')
            w=('0','0')
            for i in range(len(m)):
                f=[]
                for j in range(len(m[i])):
                    if i==j:
                        f.append(z)
                    else:
                        f.append(w)
                identidad.append(f)
            print(numcomplejos.unita(m))

        elif opc==19:
            print('Digite las dimensiones de la matriz')
            dm=(stdin.readline().strip().split(','))
            m=[]
            for j in range(int(dm[0])):
                f=[]
                x=int(dm[1])
                print('digite los elementos de la fila de la matriz')
                while x > 0:
                    y=list(map(int,stdin.readline().strip().split(',')))
                    f.append(y)
                    x-=1
                m.append(f)

            print(numcomplejos.hermitian(m,dm))

        elif opc==20:
            print('Digite las dimensiones de las matrices: ')
            d1=tuple(stdin.readline().strip().split(','))
            d2=tuple(stdin.readline().strip().split(','))
            if d1!=d2:
                print('Las matrices deben tener las mismas dimensiones')
            else:
                m1=[]
                m2=[]
                for i in range(int(d1[0])):
                    f=[]
                    x=int(d1[1])
                    print('digite los elementos de la fila de la primera matriz')
                    while x > 0:
                        y=tuple(stdin.readline().strip().split(','))
                        f.append(y)
                        x-=1
                    m1.append(f)

                for j in range(int(d1[0])):
                    f=[]
                    x=int(d1[1])
                    print('digite los elementos de la fila de la segunda matriz')
                    while x > 0:
                        y=tuple(stdin.readline().strip().split(','))
                        f.append(y)
                        x-=1
                    m2.append(f)

            print(numcomplejos.tensor(m1,m2))

            

main()
        
