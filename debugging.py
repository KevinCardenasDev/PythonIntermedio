
def divisors(num):
    try:
        divisors = []

        if num < 0:
            raise ValueError ("No se puede ingresar números negativos")
        
        for i in range (1, num + 1):
            if num % i == 0:
                divisors.append(i)
    
        return divisors

    except ValueError as ve:
        print(ve)
        return False



def main():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Termino el Programa")
    
    except ValueError:
        print("Debes ingresar un número")
    


if __name__ == "__main__":
    main()