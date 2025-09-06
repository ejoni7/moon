from math import sqrt, fabs,sin,cos
import os

def is_star(wid,i,j,radios,shift,x,r2,R1,X0,Y0,R2,start_n,start_deg,deg_step,z):
    count=0
    o=start_deg+deg_step*(z-start_n)
    if sqrt((wid/2-i)**2+(wid/2-j)**2) <= radios and shift*sqrt(
        (i-wid/2)**2+(j-wid/2-shift*x)**2)>=shift*r2:
        count+=1
    if sqrt((i+R1*sin(o)-Y0)**2+(j+R1*cos(o)-X0)**2)<=R2 and z>=start_n:
        count+=1
    return count%2

def moon (n_slice,radios,R1,X0,Y0,R2,start_n,start_deg,deg_step):
    wid=radios*2+4
    for z in range(1,n_slice+1):
        os.system('cls')
        y=fabs(radios-radios*2*z/n_slice)
        x=(radios**2-y**2)/(2*y+10**(-3))
        r2=(radios**2+y**2)/(2*y+10**(-3))
        mid=n_slice/2
        shift=(-1)**(int((mid-z)/(mid+z)+2))
        for i in range(1,wid):
            for j in range(1,wid):
                if is_star(wid,i,j,radios,shift,x,r2,R1,X0,Y0,R2,start_n,start_deg,deg_step,z):
                    print('*',end='  ')
                else:
                    print(' ',end='  ')
            print()
        input()

moon(28,25,40,50,50,5,10,0,3.14/25)