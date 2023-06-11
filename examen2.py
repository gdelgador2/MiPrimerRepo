# Problema 10 Examen


MONTHS = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

def main():
    # solicitamos fecha
    while True:
        cadena = input('Date: ').strip()
        
        if '/' in cadena:
            # fechas tipo: mm/dd/yyyy
            m,d,y = cadena.split('/')
        else:
            # fechas tipo 'Septiembre 8, 1636'
            m,d,y = cadena.replace(',','').split(' ')
            m = m.title()
            # buscamos mes en lista meses
            if m in MONTHS:
                m = MONTHS.index(m) + 1
                
        try:
            # retornamos fecha en formato correcto 'yyyy-mm-dd'
            y = int(y)
            m= int(m)
            d=int(d)
            print(f'{y}-{m:02}-{d:02}')
            break
        except:
            pass
    pass

main()