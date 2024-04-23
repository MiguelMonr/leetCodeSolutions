class Search(object):
    def linearSearch(arr, x): 
        left= 0  # Aqui obtenemos el inicio del arreglo
        right= len(arr)-1 #En esta parte obtenemos el final 
        mid = left + right //2 #Aqui obtenemos la mitad del arreglo
        
        while (left<= right):
            mid = left + right //2 #Aqui obtenemos la mitad del arreglo
            if x == arr[mid]:
                return True
            elif x > mid: 
                left = arr[mid+1]
                
                