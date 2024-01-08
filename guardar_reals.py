from yogi import read

def guardareals(n):
    ''' 
    Llegir un número n, seguit d'una seqüència de n números reals.
    Si n no és major que 0, el programa acaba 
    '''
    
    for i in range(n):
        dada = read(float)
        
    return dada

help(guardareals)
print(guardareals(5))