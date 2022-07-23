from datetime import datetime

def vida_en_segundos(fecha):
    fecha=fecha.split('/')
    t1 = datetime(year = int(fecha[2]), month = int(fecha[1]), day = int(fecha[0]))
    t2 = datetime.now()
    t3=t2-t1
    print(t3.total_seconds())
    
    
vida_en_segundos('21/1/1987')