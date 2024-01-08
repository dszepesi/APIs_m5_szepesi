from yogi import read

class Bismalah:
    """Esta clase retorna el maxim de dos enters i guarda numeros reals per a retornar el ultim"""
    
    def guardareals(n):
        """
        Llegir un número n, seguit d'una seqüència de n números reals.
        Si n no és major que 0, el programa acaba 
        """
        for i in range(n):
            dada = read(float) 
        return dada

    def maxim2int(a, b):
        """
        Retornara el maxim de dos numeros enters
        """
        maxim = max(a,b)
        return maxim

help(Bismalah)
help(Bismalah.guardareals)
help(Bismalah.maxim2int)

print(Bismalah.guardareals(3))
print(Bismalah.maxim2int(1,10))