import random
Rflag=False
def getrange(lon,ini,fin):
    rango=[]
    for a in range(lon):
        rango.append(random.randint(ini,fin))
    print(rango)
    return rango
def getmax(rango, primer_rayo, ultimo_rayo):
    return max(rango[primer_rayo:ultimo_rayo])

def getmin(rango, primer_rayo, ultimo_rayo):
    return min(rango[primer_rayo:ultimo_rayo])

def getangle(rango):
    extinider=0
    extfinder=4
    extinizq=4
    extfinizq=6
    angle_derecha=0
    angle_izquierda=0
    valor_izquierda_mayor=getmax(rango, extinizq, extfinizq)
    valor_derecha_mayor=getmax(rango, extinider, extfinder)
    valor_izquierda=getmin(rango, extinizq, extfinizq)
    valor_derecha=getmin(rango, extinider, extfinder)
    print ("valor derecha mayor", valor_derecha_mayor)
    print ("valor izquierda mayor", valor_izquierda_mayor)
    print ("valor derecha menor", valor_derecha)
    print ("valor izquierda menor", valor_izquierda)
   

    valor_mayor=valor_derecha_mayor-valor_izquierda_mayor
    angle_mayor=(valor_mayor*10)
    print ("Diferencia de la derecha mayor menos la izquierda mayor", valor_mayor)
    print ("El angulo mayores", angle_mayor)

    if valor_derecha<= 0.25:
        angle_derecha=-0.3
        print ("Entro al IF, el valor menor de la derecha fue menor que 0.25, angulo derecha:", angle_derecha)
    elif valor_derecha<=2:
        valor_derecha= valor_derecha*0.15
        print ("Entro al ELIF, el valor menor de la derecha es menor que 25, angulo derecha:", angle_derecha)
        angle_derecha=-0.3+valor_derecha
    elif valor_derecha_mayor>2:
        angle_derecha=0
        print ("Entro al ELIF, el valor menor de la derecha fue mayor que 2, angulo derecha:", angle_derecha)
    if valor_izquierda<=0.25:
        angle_izquierda=0.3
        print ("Entro al IF, el valor menor de la izquierda fue menor que 0.25, angulo izquierda:", angle_izquierda)
    elif valor_izquierda <=2:
        valor_izquierda= valor_izquierda*0.15
        angle_izquierda=0.3-valor_izquierda
        print ("Entro al ELIF, el valor menor de la izquierda fue menor que 2, angulo izquierda:", angle_izquierda)
    elif valor_izquierda_mayor>2:
        angle_izquierda=0
        print ("Entro al ELIF, el valor menor de la izquierda fue mayor que 2, angulo izquierda:", angle_izquierda)
   
    velocidad= False

    if angle_izquierda + angle_derecha ==0:
        print ("Entro al IF, angulo izquierdo + angulo derecha fue cero:")
        if angle_mayor==0:
            angle=0.01
            print ("Entro al IF, el angulo mayor es cero, angulo:", angle)
        else:
            angle=angle_mayor
            print ("Entro al ELSE, el angulo mayor NO es cero, angulo:", angle)
        velocidad= True

    elif angle_izquierda==3:
        angle= angle_izquierda
    elif angle_derecha==3:
        angle=angle_derecha
    elif angle_izquierda>angle_derecha:
        angle= angle_izquierda+angle_derecha
    else:
        angle=angle_derecha + angle_izquierda
    if angle>0.3:
        angle=0.3
        print ("Entro al IF, el angulo es mayor a 0.3 y se igualo a 0.3")
    if angle < -0.3:
        angle=-0.3
        print ("Entro al IF, el angulo es menor a 0.3 y se igualo a 0.3")
    myangle=angle
    
    print ("*********************angulo", myangle)
    print ("*********************velocidad", velocidad)
    return angle, velocidad
def getspeed (rango): #Obtener el valord del laser enfrente
    global Rflag
    limite_derecha = 3
    limite_izquierda = 5

    menor=getmin(rango, limite_derecha, limite_izquierda)
    print ("Funcion Getspeed, el rayo menor fue:", menor)
    if menor<0.30 or Rflag:
            if Rflag==False:
                Rflag= True
            speed=-0.4
            print ("Entro al IF del OR, rayo menor es menor a 0.3 entra reversa")
            if menor>0.6:
                Rflag=False
    elif menor<1:
        speed=menor
        print ("Entro al ELIF, el rayo menor es menor a 1, velocidad:", speed)
    else:
        speed=1
        signo=1
        print ("Entro al ELIF, el rayo menor no es menora a 1, velocidad a 1")
    return speed
def callback():
    rango=getrange(6,0,10)
    angle2=getangle(rango)
    getspeed(rango)
    print("angulo final", angle2)
while(True):
    callback()