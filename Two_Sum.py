# Two Sum Problem

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]  # La lista de números enteros
        :type target: int       # El objetivo que buscamos
        :rtype: List[int]      # Devuelve una lista de índices
        """
        num_to_index = {}  # Diccionario para almacenar números y sus índices
        
        # Iteramos sobre cada número en nums usando enumerate para obtener tanto el índice como el valor
        for i, val in enumerate(nums):
            diff = target - val  # Calculamos la diferencia necesaria para alcanzar el target
            
            # Comprobamos si el valor actual ya está en el diccionario
            if val in num_to_index:
                # Si está, retornamos los índices del valor que sumado a val da el target
                return [num_to_index[val], i]
            
            # Guardamos la diferencia como clave y el índice como valor en el diccionario
            num_to_index[diff] = i  # Aquí se debe usar `num_to_index[diff] = i` para almacenar correctamente la diferencia
