def PUESTO1():
    Text3="""

¿Qué desea hacer en el PUESTO1?
A) Registrar Venta
B)Consultar inventario
C)Regresar al Inicio """
    print(Text3)
    Accion=(input("\n¿Qué acción quieres realizar: ")).upper().replace(')','')
    if Accion=="A":
       # TAMALES PUESTO 1
        otraventa1='si'
        while otraventa1=='si':
            def leerInventario1():
                archivo = open('puestoo1.txt', 'r')
                listaProductos = archivo.readlines()
                archivo.close()
                inven = []
                for linea in listaProductos:
                    lin = linea.split('@')
                    lin[1] = int(lin[1])
                    lin[2] = float(lin[2][ : -1])
                    inven.append(lin)
                return inven
            def escribeInventario1():
                archivo = open('puestoo1.txt','w')
                for producto in inventario:
                    cadena = producto[0] + '@' + str(producto[1]) + '@' + str(producto[2]) + '\n'
                    archivo.write(cadena)
                archivo.close() 
            inventario = leerInventario1()
            ticket = []

            def main1():
                while True:
                    print('𝙿𝚁𝙾𝙳𝚄𝙲𝚃𝙾𝚂'.center(20))
                    for prod in range (len(inventario)):
                        print(f"{prod+1}.- {inventario[prod][0]}")

                    while True:
                        identificador = input('¿Qué quieres comprar?: ')
                        if identificador.isdigit() and 1 <= int(identificador) and int(identificador) <= len(inventario):
                            identificador = int(identificador)
                            break
                        else:
                            print('Por favor, ingresa un valor válido')
                    
                    # Obtener la cantidad a comprar
                    while True:
                        cuantas = input('¿Cuántas quieres comprar?: ')
                        if cuantas.isdigit() and int(cuantas) > 0:
                            cuantas = int(cuantas)
                            break
                        else:
                            print('Por favor, ingresa una cantidad válida')
                    
                    # Verificar el inventario
                    if inventario[identificador - 1][1] < cuantas:
                        print('No hay suficientes artículos, intenta de nuevo.')
                    else:
                        inventario[identificador - 1][1] -= cuantas
                        escribeInventario1()
                        tipotamal1 = inventario[identificador - 1][0]
                        precio1 = inventario[identificador - 1][2]
                        ticket.append([tipotamal1, cuantas, precio1])
                        print('Producto añadido al ticket.')
                    
                    # Preguntar si quiere continuar comprando
                    vuelta = input('¿Quieres agregar otro producto? (si/no): ').strip().lower().replace('í','i')
                    if vuelta != 'si':
                        break

                # Mostrar el ticket
                suma1 = 0
                print('\n')
                print('Productos registrados con éxito')
                print('𝐓𝐈𝐂𝐊𝐄𝐓'.center(32,'-'))
                print(' 𝐄𝐥 𝐭𝐚𝐦𝐚𝐥𝐢𝐭𝐨 '.center(26,'🫔')+'\n')
                for prod in ticket:
                    subtotal = prod[1] * prod[2]
                    suma1 += subtotal
                    print(f"{prod[0]} {prod[1]} x ${prod[2]:.2f} = ${subtotal:.2f}")
                    print("".rjust(30,'-'))
                print(' 𝚃𝙾𝚃𝙰𝙻 '.center(32,'-'))
                print(f'${suma1:.2f}'.center(30,'-'))
                print(' 𝐆𝐫𝐚𝐜𝐢𝐚𝐬 𝐩𝐨𝐫 𝐬𝐮 𝐜𝐨𝐦𝐩𝐫𝐚'.center(34))
            main1()
            otraventa1=input('\n¿Desea realizar otra venta?').strip().lower().replace('í','i')
        PUESTO1()
    elif Accion=="B":
        def leerInventario1():
            archivo = open('puestoo1.txt', 'r')
            listaProductos = archivo.readlines()
            archivo.close()
            inven = []
            for linea in listaProductos:
                lin = linea.split('@')
                lin[1] = int(lin[1])
                lin[2] = float(lin[2][ : -1])
                inven.append(lin)
            return inven
        def impInventario1():
            inventario = leerInventario1()
            print(inventario)
            print('𝙸𝙽𝚅𝙴𝙽𝚃𝙰𝚁𝙸𝙾 𝙿𝚄𝙴𝚂𝚃𝙾 𝟷'.center(24, '🫔'))

            for x in range(len(inventario)):
                nombre = inventario[x][0].ljust(15)  # Ajusta el valor para cambiar el espacio
                cantidad = str(inventario[x][1]).rjust(5)
                print(f"{nombre} {cantidad}")
            print('Que responsable trabajador por checar el inventario')
        impInventario1()
        PUESTO1()
    elif Accion=='C':
        empleado_or_admin()
    else:
        print('Acción no válida')
        PUESTO1()
def PUESTO2():
    Text3="""¿Qué desea hacer en el PUESTO 2?
A) Registrar Venta
B)Consultar inventario
C) Regresar al Inicio"""
    print(Text3)
    Accion=input("¿Qué desea hacer?: ").upper().replace(')','').strip()
    if Accion=="A":
       # TAMALES PUESTO 2
        otraventa2='si'
        while otraventa2=='si':
            def leerInventario2():
                archivo = open('puestoo2.txt', 'r')
                listaProductos = archivo.readlines()
                archivo.close()
                inven = []
                for linea in listaProductos:
                    lin = linea.split('@')
                    lin[1] = int(lin[1])
                    lin[2] = float(lin[2][ : -1])
                    inven.append(lin)
                return inven
            def escribeInventario2():
                archivo = open('puestoo2.txt','w')
                for producto in inventario:
                    cadena = producto[0] + '@' + str(producto[1]) + '@' + str(producto[2]) + '\n'
                    archivo.write(cadena)
                archivo.close() 
            inventario = leerInventario2()
            ticket = []

            def main2():
                while True:
                    print('𝙿𝚁𝙾𝙳𝚄𝙲𝚃𝙾𝚂'.center(20))
                    for prod in range (len(inventario)):
                        print(f"{prod+1}.- {inventario[prod][0]}")

                    while True:
                        identificador = input('¿Qué quieres comprar?: ')
                        if identificador.isdigit() and 1 <= int(identificador) and int(identificador) <= len(inventario):
                            identificador = int(identificador)
                            break
                        else:
                            print('Por favor, ingresa un valor válido')
                    
                    # Obtener la cantidad a comprar
                    while True:
                        cuantas = input('¿Cuántas quieres comprar?: ')
                        if cuantas.isdigit() and int(cuantas) > 0:
                            cuantas = int(cuantas)
                            break
                        else:
                            print('Por favor, ingresa una cantidad válida')
                    
                    # Verificar el inventario
                    if inventario[identificador - 1][1] < cuantas:
                        print('No hay suficientes artículos, intenta de nuevo.')
                    else:
                        inventario[identificador - 1][1] -= cuantas
                        escribeInventario2()
                        tipotamal2 = inventario[identificador - 1][0]
                        precio2 = inventario[identificador - 1][2]
                        ticket.append([tipotamal2, cuantas, precio2])
                        print('Producto añadido al ticket.')
                    
                    # Preguntar si quiere continuar comprando
                    vuelta = input('¿Quieres agregar otro producto? (si/no): ').strip().lower().replace('í','i')
                    if vuelta != 'si':
                        break

                # Mostrar el ticket
                suma2 = 0
                print('\n')
                print('Productos registrados con éxito')
                print('𝐓𝐈𝐂𝐊𝐄𝐓'.center(32,'-'))
                print(' 𝐄𝐥 𝐭𝐚𝐦𝐚𝐥𝐢𝐭𝐨 '.center(26,'🫔')+'\n')
                for prod in ticket:
                    subtotal = prod[1] * prod[2]
                    suma2 += subtotal
                    print(f"{prod[0]} {prod[1]} x ${prod[2]:.2f} = ${subtotal:.2f}")
                    print("".rjust(30,'-'))
                print(' 𝚃𝙾𝚃𝙰𝙻 '.center(32,'-'))
                print(f'${suma2:.2f}'.center(30,'-'))
                print(' 𝐆𝐫𝐚𝐜𝐢𝐚𝐬 𝐩𝐨𝐫 𝐬𝐮 𝐜𝐨𝐦𝐩𝐫𝐚'.center(34))
            main2()
            otraventa2=input('\n¿Desea realizar otra venta?').strip().lower().replace('í','i')
        PUESTO2()
    elif Accion=="B":
        def leerInventario2():
            archivo = open('puestoo2.txt', 'r')
            listaProductos = archivo.readlines()
            archivo.close()
            inven = []
            for linea in listaProductos:
                lin = linea.split('@')
                lin[1] = int(lin[1])
                lin[2] = float(lin[2][ : -1])
                inven.append(lin)
            return inven
        def impInventario2():
            inventario = leerInventario2()
            print(inventario)
            print('𝙸𝙽𝚅𝙴𝙽𝚃𝙰𝚁𝙸𝙾 𝙿𝚄𝙴𝚂𝚃𝙾 𝟸'.center(24, '🫔'))

            for x in range(len(inventario)):
                nombre = inventario[x][0].ljust(15)  # Ajusta el valor para cambiar el espacio
                cantidad = str(inventario[x][1]).rjust(5)
                print(f"{nombre} {cantidad}")
            print('Que responsable trabajador por checar el inventario')
        impInventario2()
        PUESTO2()
    elif Accion=='C':
        empleado_or_admin()
    else:
        print('Acción no válida')
        PUESTO2()

def PUESTO3():
    Text3="""

¿Qué desea hacer en el PUESTO DEMO?
A) Registrar Venta
B)Consultar inventario
C) Regresar al Inicio"""
    print(Text3)
    Accion=(input("¿Que acción desea realizar? ")).upper().replace(')','').strip()
    if Accion=="A":
                # TAMALES PUESTO 3
        otraventa3='si'
        while otraventa3=='si':
            def leerInventario3():
                archivo = open('puestoo3.txt', 'r')
                listaProductos = archivo.readlines()
                archivo.close()
                inven = []
                for linea in listaProductos:
                    lin = linea.split('@')
                    lin[1] = int(lin[1])
                    lin[2] = float(lin[2][ : -1])
                    inven.append(lin)
                return inven
            def escribeInventario3():
                archivo = open('puestoo3.txt','w')
                for producto in inventario:
                    cadena = producto[0] + '@' + str(producto[1]) + '@' + str(producto[2]) + '\n'
                    archivo.write(cadena)
                archivo.close() 
            inventario = leerInventario3()
            ticket = []

            def main3():
                while True:
                    print('𝙿𝚁𝙾𝙳𝚄𝙲𝚃𝙾𝚂'.center(20))
                    for prod in range (len(inventario)):
                        print(f"{prod+1}.- {inventario[prod][0]}")

                    while True:
                        identificador = input('¿Qué quieres comprar?: ')
                        if identificador.isdigit() and 1 <= int(identificador) and int(identificador) <= len(inventario):
                            identificador = int(identificador)
                            break
                        else:
                            print('Por favor, ingresa un valor válido')
                    
                    # Obtener la cantidad a comprar
                    while True:
                        cuantas = input('¿Cuántas quieres comprar?: ')
                        if cuantas.isdigit() and int(cuantas) > 0:
                            cuantas = int(cuantas)
                            break
                        else:
                            print('Por favor, ingresa una cantidad válida')
                    
                    # Verificar el inventario
                    if inventario[identificador - 1][1] < cuantas:
                        print('No hay suficientes artículos, intenta de nuevo.')
                    else:
                        inventario[identificador - 1][1] -= cuantas
                        escribeInventario3()
                        tipotamal3 = inventario[identificador - 1][0]
                        precio3 = inventario[identificador - 1][2]
                        ticket.append([tipotamal3, cuantas, precio3])
                        print('Producto añadido al ticket.')
                    
                    # Preguntar si quiere continuar comprando
                    vuelta = input('¿Quieres agregar otro producto? (si/no): ').strip().lower().replace('í','i')
                    if vuelta != 'si':
                        break

                # Mostrar el ticket
                suma3 = 0
                print('\n')
                print('Productos registrados con éxito')
                print('𝐓𝐈𝐂𝐊𝐄𝐓'.center(32,'-'))
                print(' 𝐄𝐥 𝐭𝐚𝐦𝐚𝐥𝐢𝐭𝐨 '.center(26,'🫔')+'\n')
                for prod in ticket:
                    subtotal = prod[1] * prod[2]
                    suma3 += subtotal
                    print(f"{prod[0]} {prod[1]} x ${prod[2]:.2f} = ${subtotal:.2f}")
                    print("".rjust(30,'-'))
                print(' 𝚃𝙾𝚃𝙰𝙻 '.center(32,'-'))
                print(f'${suma3:.2f}'.center(30,'-'))
                print(' 𝐆𝐫𝐚𝐜𝐢𝐚𝐬 𝐩𝐨𝐫 𝐬𝐮 𝐜𝐨𝐦𝐩𝐫𝐚'.center(34))
            main3()
            otraventa3=input('\n¿Desea realizar otra venta?').strip().lower().replace('í','i')
        PUESTO3()
    elif Accion=="B":
        def leerInventario3():
            archivo = open('puestoo3.txt', 'r')
            listaProductos = archivo.readlines()
            archivo.close()
            inven = []
            for linea in listaProductos:
                lin = linea.split('@')
                lin[1] = int(lin[1])
                lin[2] = float(lin[2][ : -1])
                inven.append(lin)
            return inven
        def impInventario3():
            inventario = leerInventario3()
            print('𝙸𝙽𝚅𝙴𝙽𝚃𝙰𝚁𝙸𝙾 𝙿𝚄𝙴𝚂𝚃𝙾 𝙳𝙴𝙼𝙾'.center(24, '🫔'))

            for x in range(len(inventario)):
                nombre = inventario[x][0].ljust(15)  # Ajusta el valor para cambiar el espacio
                cantidad = str(inventario[x][1]).rjust(5)
                print(f"{nombre} {cantidad}")
            print('')
            print('ℚ𝕦𝕖 𝕣𝕖𝕤𝕡𝕠𝕟𝕤𝕒𝕓𝕝𝕖 𝕥𝕣𝕒𝕓𝕒𝕛𝕒𝕕𝕠𝕣 𝕡𝕠𝕣 𝕔𝕙𝕖𝕔𝕒𝕣 𝕖𝕝 𝕚𝕟𝕧𝕖𝕟𝕥𝕒𝕣𝕚𝕠')
        impInventario3()
        PUESTO3()
    elif Accion=='C':
        empleado_or_admin()
    else:
        print('Acción no válida')
        PUESTO3()
        
def Empleado_opciones(nombre):
    if nombre=="Gaby":
        puesto1=PUESTO1()
    elif nombre=="Jorge":
        puesto2=PUESTO2()
    else:
        puesto3=PUESTO3()
        
##################################################################
def inventorio_puesto1():
    archivo = open("Puesto1.txt", "r")
    stock = archivo.readlines()
    archivo.close()
    lista = []
    for line in stock:
        separar = line.split("--@--")
        separar[1] = int(separar[1])
        separar[2] = float(separar[2][:-1])
        lista.append(separar)
    return lista

#imprimir los valores dentro del archivo de texto

def introducirstock():
    archivo = open("Puesto1.txt", "w")
    for Cant in stock1:
        cadena=Cant[0]+"--@--"+str(Cant[1])+"--@--"+str(Cant[2])+ "\n"
        archivo.write(cadena)
    archivo.close()
def accion(stock1):
    con=0
    cont=1
    salir=input("¿Regresar a menu?")
    a1=salir.lower()
    while cont!=0:
        if salir=="si":
            Registrar_elaboración_diaria()
        elif salir =="no" and cont==1 :
            ncom=int(input("Que quieren reestockear: #numero: "))
            cuantas=int(input("cantidad por agregar:"))
            print(stock1)
            stock1[ncom-1][1]+=cuantas
            print(stock1)
            con=con+1
        else:
            a=accion(stock1)
    

        
        
        
##################################################################

def reg_vent():
    vent=[' 1) Tamal verde ',' 2) Tamal de rajas ',' 3) Tamal de mole ', ' 4) Tamal de guayaba ',' 5) Torta verde ',' 6) Torta de rajas ',' 7) Torta de mole ',' 8) Torta de guayaba ',' 9) Atole chico ', ' 10) Atole grande ',' 11) Bolillo ']
    vent1=['Tamal verde','Tamal de rajas','Tamal de mole', 'Tamal de guayaba','Torta verde','Torta de rajas','Torta de mole','Torta de guayaba','Atole chico', 'Atole grande','Bolillo']
    b=1
    a=0
    for x in vent:
        if a==11:
            break
        c=vent1[a]
        cant=str(input('Cantidad vendida de '+str(c)+': '))
        vent.insert(b,cant)
        b=b+2
        a=a+1
    #print(vent)
    vent_final=''.join(vent)
    #print(vent_final)
    d=0
    e=1
    for x in (vent):
        if e==23:
            break
        elif d==0:
            print('TIKET'.center(30,'='))
        f=len(vent[d])
        g=30-f
        lista=vent[d]+vent[e].rjust(g,'-')
        print(lista)
        d=d+2
        e=e+2
##################################################1################
       
def Administrador_opciones():
    accion="""Accion deseas realizar:
    A)Reporte de venta
    B)Registrar la elaboracion diaria
    C)Consulta de inventario Global
    Escribe inicio para volver a la pestaña inicial"""
    print(accion)
    Opcion=(input("Escribe A, B o C: ")).upper().strip().replace(')','')
    if Opcion == "A":
        avpriv = '''Por razones de privacidad y por posibles errores en el área de producción,
                    introducir la cantidad real de tamales producidos este día'''
    #En este negocio puede haber venta negativa, esto nos indica que hay tamales sobrantes de un día anterior
        #que todavía no se venden (triste, pero cierto)
        print("REPORTE DE VENTA".center(30, '-'))
        puest = input('¿Qué puesto quiere ver? ')
        if puest.isdigit() and int(puest) == 1:
            archivo = open('puestoo1.txt', 'r')
            listaProductos = archivo.readlines()
            archivo.close()
            inven = []
            
            for linea in listaProductos:
                lin = linea.split('@')
                lin[1] = int(lin[1])
                lin[2] = float(lin[2][:-1])
                inven.append(lin)

            while True:
                tv1 = input('Tamales verdes: ')
                try:
                    tv1 = int(tv1)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            
            while True:
                tr1 = input('Tamales rajas: ')
                try:
                    tr1 = int(tr1)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            
            while True:
                tm1 = input('Tamales mole: ')
                try:
                    tm1 = int(tm1)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            
            while True:
                td1 = input('Tamales dulce: ')
                try:
                    td1 = int(td1)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            print(f'{inven[0][0]}: {(tv1) - (inven[0][1])}')
            print(f'{inven[1][0]}: {(tr1) - (inven[1][1])}')
            print(f'{inven[2][0]}: {(tm1) - (inven[2][1])}')
            print(f'{inven[3][0]}: {(td1) - (inven[3][1])}')
        
            
        elif puest.isdigit() and int(puest) == 2:
            archivo = open('puestoo2.txt', 'r')
            listaProductos = archivo.readlines()
            archivo.close()
            inven = []
            
            for linea in listaProductos:
                lin = linea.split('@')
                lin[1] = int(lin[1])
                lin[2] = float(lin[2][:-1])
                inven.append(lin)
            

            while True:
                tv2 = input('Tamales verdes: ')
                try:
                    tv2 = int(tv2)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            
            while True:
                tr2 = input('Tamales rajas: ')
                try:
                    tr2 = int(tr2)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            
            while True:
                tm2 = input('Tamales mole: ')
                try:
                    tm2 = int(tm2)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            
            while True:
                td2 = input('Tamales dulce: ')
                try:
                    td2 = int(td2)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            print(f'{inven[0][0]}: {(tv2) - (inven[0][1])}')
            print(f'{inven[1][0]}: {(tr2) - (inven[1][1])}')
            print(f'{inven[2][0]}: {(tm2) - (inven[2][1])}')
            print(f'{inven[3][0]}: {(td2) - (inven[3][1])}\n')
            
        elif puest.isdigit() and int(puest) == 3:
            archivo = open('puestoo3.txt', 'r')
            listaProductos = archivo.readlines()
            archivo.close()
            inven = []
            
            for linea in listaProductos:
                lin = linea.split('@')
                lin[1] = int(lin[1])
                lin[2] = float(lin[2][:-1])
                inven.append(lin)

            while True:
                tv3 = input('Tamales verdes: ')
                try:
                    tv3 = int(tv3)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            
            while True:
                tr3 = input('Tamales rajas: ')
                try:
                    tr3 = int(tr3)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            
            while True:
                tm3 = input('Tamales mole: ')
                try:
                    tm3 = int(tm3)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            
            while True:
                td3 = input('Tamales dulce: ')
                try:
                    td3 = int(td3)
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            print(f'{inven[0][0]}: {(tv3) - (inven[0][1])}')
            print(f'{inven[1][0]}: {(tr3) - (inven[1][1])}')
            print(f'{inven[2][0]}: {(tm3) - (inven[2][1])}')
            print(f'{inven[3][0]}: {(td3) - (inven[3][1])}')        
        else:
            print('Valor no válido')
            Administrador_opciones()
    elif Opcion=="B":
        pue=input('¿A qué puesto quiere agregar/disminuir tamales?')
        if pue.isdigit() and int(pue)==1:
            def leerInventario1():
                archivo = open('puestoo1.txt', 'r')
                listaProductos = archivo.readlines()
                archivo.close()
                inven = []
                for linea in listaProductos:
                    lin = linea.split('@')
                    lin[1] = int(lin[1])
                    lin[2] = float(lin[2][ : -1])
                    inven.append(lin)
                return inven
            def escribeInventario1():
                archivo = open('puestoo1.txt','w')
                for producto in inventario:
                    cadena = producto[0] + '@' + str(producto[1]) + '@' + str(producto[2]) + '\n'
                    archivo.write(cadena)
                archivo.close() 
            inventario = leerInventario1()
            while True:
                rgtv1 = input('Tamales verdes: ')
                try:
                    rgtv1 = int(rgtv1)
                    if rgtv1+(inventario[0][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[0][1] += rgtv1
                        escribeInventario1()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            while True:
                rgtr1 = input('Tamales rajas: ')
                try:
                    rgtr1 = int(rgtr1)
                    if rgtr1+(inventario[1][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[1][1] += rgtr1
                        escribeInventario1()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            while True:
                rgtm1 = input('Tamales mole: ')
                try:
                    rgtm1 = int(rgtm1)
                    if rgtm1+(inventario[2][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[2][1] += rgtm1
                        escribeInventario1()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            while True:
                rgtd1 = input('Tamales dulce: ')
                try:
                    rgtd1 = int(rgtd1)
                    if rgtd1+(inventario[3][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[3][1] += rgtd1
                        escribeInventario1()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
                    
        if pue.isdigit() and int(pue)==2:
            def leerInventario2():
                archivo = open('puestoo2.txt', 'r')
                listaProductos = archivo.readlines()
                archivo.close()
                inven = []
                for linea in listaProductos:
                    lin = linea.split('@')
                    lin[1] = int(lin[1])
                    lin[2] = float(lin[2][ : -1])
                    inven.append(lin)
                return inven
            def escribeInventario2():
                archivo = open('puestoo2.txt','w')
                for producto in inventario:
                    cadena = producto[0] + '@' + str(producto[1]) + '@' + str(producto[2]) + '\n'
                    archivo.write(cadena)
                archivo.close() 
            inventario = leerInventario2()
            while True:
                rgtv2 = input('Tamales verdes: ')
                try:
                    rgtv2 = int(rgtv2)
                    if rgtv2+(inventario[0][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[0][1] += rgtv2
                        escribeInventario2()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            while True:
                rgtr2 = input('Tamales rajas: ')
                try:
                    rgtr2 = int(rgtr2)
                    if rgtr2+(inventario[1][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[1][1] += rgtr2
                        escribeInventario2()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            while True:
                rgtm2 = input('Tamales mole: ')
                try:
                    rgtm2 = int(rgtm2)
                    if rgtm2+(inventario[2][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[2][1] += rgtm2
                        escribeInventario2()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            while True:
                rgtd2 = input('Tamales dulce: ')
                try:
                    rgtd2 = int(rgtd2)
                    if rgtd2+(inventario[3][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[3][1] += rgtd2
                        escribeInventario2()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
                    
        if pue.isdigit() and int(pue)==3:
            def leerInventario3():
                archivo = open('puestoo3.txt', 'r')
                listaProductos = archivo.readlines()
                archivo.close()
                inven = []
                for linea in listaProductos:
                    lin = linea.split('@')
                    lin[1] = int(lin[1])
                    lin[2] = float(lin[2][ : -1])
                    inven.append(lin)
                return inven
            def escribeInventario3():
                archivo = open('puestoo3.txt','w')
                for producto in inventario:
                    cadena = producto[0] + '@' + str(producto[1]) + '@' + str(producto[2]) + '\n'
                    archivo.write(cadena)
                archivo.close() 
            inventario = leerInventario3()
            while True:
                rgtv3 = input('Tamales verdes: ')
                try:
                    rgtv3 = int(rgtv3)
                    if rgtv3+(inventario[0][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[0][1] += rgtv3
                        escribeInventario3()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            while True:
                rgtr3 = input('Tamales rajas: ')
                try:
                    rgtr3 = int(rgtr3)
                    if rgtr3+(inventario[1][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[1][1] += rgtr3
                        escribeInventario3()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            while True:
                rgtm3 = input('Tamales mole: ')
                try:
                    rgtm3 = int(rgtm3)
                    if rgtm3+(inventario[2][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[2][1] += rgtm3
                        escribeInventario2()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
            while True:
                rgtd3 = input('Tamales dulce: ')
                try:
                    rgtd3 = int(rgtd3)
                    if rgtd3+(inventario[3][1])<0:
                        print('Valor no válido')
                    else:
                        inventario[3][1] += rgtd3
                        escribeInventario3()
                    break
                except ValueError:
                    print('Valor no válido, por favor ingresa un número.')
    elif Opcion=="C":
        def leerInventario1():
            archivo = open('puestoo1.txt', 'r')
            listaProductos = archivo.readlines()
            archivo.close()
            inven = []
            for linea in listaProductos:
                lin = linea.split('@')
                lin[1] = int(lin[1])
                lin[2] = float(lin[2][ : -1])
                inven.append(lin)
            return inven
        def leerInventario2():
            archivo = open('puestoo2.txt', 'r')
            listaProductos = archivo.readlines()
            archivo.close()
            inven = []
            for linea in listaProductos:
                lin = linea.split('@')
                lin[1] = int(lin[1])
                lin[2] = float(lin[2][ : -1])
                inven.append(lin)
            return inven
        def leerInventario3():
            archivo = open('puestoo3.txt', 'r')
            listaProductos = archivo.readlines()
            archivo.close()
            inven = []
            for linea in listaProductos:
                lin = linea.split('@')
                lin[1] = int(lin[1])
                lin[2] = float(lin[2][ : -1])
                inven.append(lin)
            return inven
        inven1=leerInventario1()
        inven2=leerInventario2()
        inven3=leerInventario3()
        print('𝙸𝙽𝚅𝙴𝙽𝚃𝙰𝚁𝙸𝙾 𝙿𝚄𝙴𝚂𝚃𝙾 𝟷'.center(30,'-'))
        for x in range(len(inven1)):
            print(f'{inven1[x][0]}  : {inven1[x][1]}')
        print('𝙸𝙽𝚅𝙴𝙽𝚃𝙰𝚁𝙸𝙾 𝙿𝚄𝙴𝚂𝚃𝙾 𝟸'.center(30,'-'))
        for x in range(len(inven2)):
            print(f'{inven2[x][0]}  : {inven2[x][1]}')
        print('𝙸𝙽𝚅𝙴𝙽𝚃𝙰𝚁𝙸𝙾 𝙿𝚄𝙴𝚂𝚃𝙾 𝟹'.center(30,'-'))
        for x in range(len(inven3)):
            print(f'{inven3[x][0]}  : {inven3[x][1]}')
        

    elif Opcion=="inicio" or Opcion=="INICIO" or Opcion=="Inicio":
        print("Volviendo a pestaña inicial")
        inicio=empleado_or_admin
    else:
        print("Algo salio mal, por favor vuelve a introducir la accion: ")
        Administrador_opciones()
    Administrador_opciones()
##################################################################

def empleado_or_admin():
    a='''¿Qué rol juegas en la empresa?
    1) Administrador
    2) Vendedor '''
    print (a)
    tipe_of_user=input('Ingresa tu tipo de usuario (1 o 2): ')
    try:
      tipe_of_user=int(tipe_of_user)

      if tipe_of_user==1:
          print("            BIENVENIDO ADMINISTRADOR       ")
          textb="""  Si desea volver al inicio teclee Inicio
  Por favor teclee la contraseña para ingresar:"""
          print(textb)
          contador=0
          while contador<3:
              Password=str(input())
              if Password=="Tamalito123":
                  print("ACCESO PERMITIDO")
                  TASK= Administrador_opciones()
                  break

              elif Password=="Inicio" or Password=="inicio":
                  print("Volviendo a inicio")
                  inicio=empleado_or_admin()
              else:
                  print("La contraseña es incorrecta")
                  contador=contador+1
                  print(textb)
                  if contador==3:
                      print("Demasiados intentos")
                      inicio=empleado_or_admin()
      elif tipe_of_user==2:
          print("            BIENVENIDO EMPLEADO       ")
          name_list=["Gaby","Jorge","Hazel"]
          textb="""  Si desea volver al inicio teclee Inicio"""
          print(textb)
          contador=0
          while contador<3:
              name=str(input("¿Cual es tu nombre? "))
              Password=str(input("Por favor teclee la contraseña para ingresar: "))
              if Password=="TheBigTamale":
                  print("𝐀𝐂𝐂𝐄𝐒𝐎 𝐏𝐄𝐑𝐌𝐈𝐓𝐈𝐃𝐎".center(30,'-'))
                  print('')
                  print(f"Bienvenido {name}".center(25,' '))
                  Task_Em=Empleado_opciones(name)
                  break
              elif Password=="Inicio" or Password=="inicio":
                  print("Volviendo a inicio")
                  inicio=empleado_or_admin()
              else:
                  print("La contraseña o usuario son incorrectos")
                  contador=contador+1
                  print(textb)
                  if contador==3:
                      print("Demasiados intentos")
                      inicio=empleado_or_admin()
      else:
          print("No valido")
          inicio=empleado_or_admin()
    except ValueError:
      print('El valor ingresado no es válido, intente de nuevo')
      empleado_or_admin()

empleado_or_admin()