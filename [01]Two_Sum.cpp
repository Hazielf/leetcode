#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) { //Dos parametros, el vector nums y el entero target
        std::unordered_map<int, int> numToIndex; //Se crea el hashmap

        for (int i = 0; i < nums.size(); i++) { //Hasta que i sea igual que el #elementos en nums, intervalo abierto.
            int val = nums[i]; //declara el valor del elemento en especìfico
            int difference = target - val;

            if (numToIndex.contains(val)) { //Si el valor "val" ya esta en el mapa:
                return {numToIndex[val], i}; //Devuelve los indices
            }

            numToIndex[difference] = i; //De otra manera, guarda la diferencia en el mapa
        }

        return {}; //Si llega hasta aca, es que no se encontro nada. Por lo que devuelve la lista vacia
        //Esto no es necesario en leetcode, pero igual lo agrego.
    }
};
