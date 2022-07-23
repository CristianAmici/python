import math
def medidas_hoja_A(N):
    result=(841,1189)
    if N==0:
        return result
    else:
        result=medidas_hoja_A(N-1)
        result=(math.floor(result[1]/2),result[0])
        return result