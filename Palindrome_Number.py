from math import log10
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): #Si x es negativo o termina en 0 pero no es 0.
            return False
        
        if x==0: #No existe log10(0)
            return True
        
        divider = 10**((log10(x)) // 1)
            
        while x: #mientras x no sea 0
            if (x % 10) != (x // divider): #si el número de la derecha no es igual al número de la izquierda
                return False
            
            x = (x % divider) // 10 #
            divider = divider/100 #por qué se reducio el numero de digitos en 2 (uno a la derecha y otro a la izquierda)
        
        return True #Si el código llega hasta aca, es verdadero.