#imports
import datetime
import calendar

#menu

def menu():
    """
    initiates the program
    starts the defined functions
    returns a function depending on the user input
    """
    
    m = {1 : "1.Cotizar ROF y generar mail", 2 : "2.Diferenciales para un tipo final deaseado", 3 : "3.Consultar primas de liquidez", 4 : "4.Calcular la vida media con el cuadro de Murex 3", 5 : "5.Generar un cuadro ROF y calcular vida media"}
    

    while True:
        print("-" * 20)
        print("\n" + m[1] + "\n" + m[2] + "\n" + m[3] + "\n" + m[4] + "\n" + m[5] + "\n")
        print("-" * 20)
        
        try:
            prompt = int(input("Introduce una opción: \n"))
        except ValueError:
            print("---Introduce el número de la opcion...---\n Ej. 1")
            continue
        if prompt not in list(m):            
            print("---Esa opción no existe aún...---")
            continue
        else:
            if prompt == 1:
                print("\n---Confidencial---\n")
                return menu()
            elif prompt == 2:
                print("\n---Confidencial---\n")
                return menu()
            elif prompt == 3:
                print("\n---Confidencial---\n")
                return menu()
            elif prompt == 4:
                return get_nsch()
            elif prompt == 5:
                return get_cuadro()

#functions option 1
#functions option 2
#functions option 3

#functions option 4

def get_nsch():
    """
    gets inout frm user, returns the next function
    checks that the number of periods is positive
    """  
    while True:
        try:
            e = int(input("\nIndica el número de periodos que tiene la operación: Ej 36\n")) 
        except:
            print("---Introduce el número de periodos en un formato aceptado---")
            continue
        if e <= 0:
            print("---Introduce un número de periodos positivo---")
            continue
        else:
            break
    return get_sch_vdm(e)

def get_sch_vdm(e):
    """
    User imputs the schedule and reimaining capital
    User needs to know how to price loans and generate the schedule in Murex 3...
    "Ctrl + c" the table in Murex 3, "Ctrl + v" into the python console
    returns the next function
    """ 

    while True:
        testing =[] 
        try:
            print("\nPega las fechas del cuadro de Murex 3 y presiona Enter")
            print("--------------------------------------------------------")
            for i in range(e): 
                element = input("") 
                testing.append(element)
                
            new_date = []
            new_date1 = []

            for date in testing:
                new_list = date.split("\t")
                for date1 in new_list:
                    new_date.append(date1)
                    date_time_obj = datetime.datetime.strptime(date1, '%d/%m/%Y')
                    new_date1.append(date_time_obj)
                    

        except ValueError:
            print("---Introduce los datos en un formato aceptado, Ctrl+V el cuadro de Murex---\n\n")
            continue
        else:
            return get_c(new_date1, e)

def get_c(new_date1, e):
    """
    calculates the schedule
    gets the capitals from the user
    calculates the whole amortizing table
    calculates teh average life of the loan
    returns the menu
    """
    a = []

    for i in range(0,len(new_date1),2):
        try:        
            d = new_date1[i + 1] - new_date1[i]
            d = (d).days
            a.append(d)
        except:
            print("end of list")      
            break    

    while True:
        c = []  
        cc = [] 
        try:
            
            print("\nPega los capitales pendientes de la operación y presiona Enter")
            print("--------------------------------------------------------------")

            for i in range(e): 
                capital = input("") 
                c.append(capital) 

            for i in range(len(c)):
                cc.append(c[i].replace(",",""))   

            v = []
            vdm = 0

            for i in range(e):
                v.append(float(a[i]) * float(cc[i]) / float(cc[0]) / 365)

            for i in range(e):
                vdm += v[i]
            svdm = str(vdm)

            print("\n\n-------------------------------------------")
            print("La vida media de la operación es " + svdm[:5] + " años.")
            print("-------------------------------------------\n\n\n")


        except:
            print("---Introduce los datos en un formato aceptado, Ctrl+V los capitales de Murex---")
            continue

        else:
            break
              
    return menu()

#opcion 5

def get_cuadro():
    """
    Gets user input needed for the amortized loan, returns get_date()
    Calculates the ammout to be paid on each period, simulates de pmt() of excel
    """
    while True:
        try:
            start = datetime.datetime.strptime(get_date(), '%d/%m/%Y')
        except:
             print("---Introduce una fecha en un formato aceptado...---\n")
             continue
        else:
            break

    while True:
        try:
            pv = float(input("¿Qué nominal tiene? (Ej. 500000)\n"))
        except ValueError:
            print("---Introduce una cantidad en un formato aceptado...---\n Ej. 300000 ")
            continue
        if pv <= 0:
            print("---Introduce un nominal positivo---")
            continue
        else:
            break

    while True:
        try:
            rate = float(input("¿Qué tipo de interés tiene? (Ej. para 2% poner 0.02)\n"))
        except ValueError:
            print("---Introduce una cantidad en un formato aceptado...---\n (Ej. para 2% poner 0.02)")
            continue
        if rate <= 0:
            print("---Introduce un tipo de interés positivo---")
            continue
        else:
            break

    while True:
        try:
            years = float(input("¿Cuántos años?\n"))
        except ValueError:
            print("---Introduce un número de años...---\n Ej. 6 ")
            continue
        if years < 0:            
            print("---Introduce un número de años positivo...---")
            continue
        else:
            break

    while True:
        try:
            per = int(input("¿Cuántos periodos por año?\n"))
        except ValueError:
            print("---Introduce un número de periodos en integer...---\n Ej. 6 ")
            continue
        if per < 0:            
            print("---Introduce un número de periodos positivo...---")
            continue
        elif per > 12:            
            print("---Nunca me volvereis a romper poniendo 180 periodos ;)...---")
            continue
        else:
            break

    while True:
        try:
            carencia = int(input("¿Cuántos periodos de carencia? (si no tiene pon 0)\n"))
        except ValueError:
            print("---Introduce un número de periodos...---\n Ej. 6 ")
            continue
        if carencia < 0:            
            print("---Introduce un número de periodos positivo...---")
            continue
        elif carencia >= (per * years):
            print("---Introduce un número de periodos con sentido...---")
            continue
        else:
            break

    pmt = pv/((1/(rate/per)) - 1/((rate/per)*(1+rate/per)**((years*per)-carencia)))

    return get_cap(pv, rate, per, years, carencia, pmt, start)



def get_date():
    """
    Gets user input, calculatees de average life of the loan
    transforms the user input data from string to datetime object
    generates the amortizing table
    """
    while True:
        try:
            inicio = input("¿Cuando empieza el cuadro? (Ej. 16/01/2020)\n")
        except ValueError:
            print("---Introduce una fecha en un formato aceptado...---\n Ej. 16/01/2020 ")
            continue
        else:
            break
    return inicio

def add_months(sourcedate, months):
    """
    gets the start of the schedule and the time between periods
    returns the next period date
    """
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    p1 = datetime.date(year, month, day)
    p1 = datetime.datetime.strptime(str(p1), "%Y-%m-%d")
    return p1



def get_cap(pv, rate, per, years, carencia, pmt, start):
    """
    Builds the amortizing table
    Gets the average life of the loan
    returns the menu
    """
    cuota = pmt
    dates = [add_months(start, 0)]
    for l in range(int((years * per))):
        p1 = add_months(start, int(12/per))
        dates.append(p1)             
        start = p1
    nom = []
    interest = []
    capitals = []
    

    for j in range(int(per * years)):
        nom.append(pv)                    
        i = pv * (rate / per)
        interest.append(i)
        if carencia > 0:
            cap = 0
            carencia -= 1
        else:            
            cap = pmt - i 
        capitals.append(cap) 
        pv -= cap
    vidamedia = []
    for l in range(len(dates)):
        try:            
            dd = dates[l + 1] - dates[l]
            dd =(dd).days
            vm = nom[l] * dd / nom[0] / 365
            vidamedia.append(vm)
        except:
            break
    yeet = 0
    for v in range(len(vidamedia)):
        
        yeet += vidamedia[v]

    csv = []
    print("   Inicio       Fin       Nominal     Amort      Inter    Cuota")
    print("------------------------------------------------------------------")
    for data in range(len(dates)):
        try:
            print(str(dates[data])[:11] + "  " + str(dates[data + 1])[:11] + "  " + str(round(nom[data], 2)) + "  " + str(round(capitals[data], 2)) + "  " + str(round(interest[data], 2)) + "  " + str(round(cuota, 2)))
            csv.append(str(dates[data])[:11] + "," + str(dates[data + 1])[:11] + "," + str(nom[data]) + "," + str(capitals[data]) + "," + str(interest[data]) + "," + str(cuota))
        except:
            print("\nCuadro finalizado")
            break
    print("\n\n-------------------------------------------")
    print("La vida media de la operación es " + str(yeet)[:5] + " años.")
    print("-------------------------------------------\n\n\n")

    while True:
        try:
            excel = input("¿Quieres exportar un .csv para tratar los datos en Excel?: y/n)\n")
        except:
            print("Introduce un > y < o un > n <")
        if excel == "y":
            return get_csv(csv, data, dates, nom, capitals, interest, cuota)
        elif excel == "n":
            return menu()
        else:
            continue 
def get_csv(csv, data, dates, nom, capitals, interest, cuota):
    """
    Prints the amortizing table in csv format
    returns the menu
    """
    print("\n\n")
    print("Inicio,Fin,Nominal,Amort,Inter,Cuota")
    for cs in range(len(csv)):
        print(csv[cs])
    print("\n\nTienes que copiar el cuadro delimitado por comas y pegarlo en tu hoja de excel\n\n")
    return menu()

menu()







    
