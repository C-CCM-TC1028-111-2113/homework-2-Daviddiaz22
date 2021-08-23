def main():
    # Escribe el código adecuado para completar el programa
    num1 = int(input('Ingresa el primer número: '))
    num2 = int(input('Ingresa el segundo número: '))
    num3 = int(input('Ingresa el tercer número: '))

    if num1 <= num2 and num1 <= num3:
        print(num1)
    else:
        if num2 <= num1 and num2 <= num3:
            print(num2)
        else:
            if num3 <= num1 and num3<= num2:
                print(num3)   
 
    if num2 > num1 > num3 or num3 > num1 > num2 :
        print(num1)
    else:
        if num1 > num2 > num3 or num3 > num2 > num1:
            print(num2)
        else:
            if num1 > num3 > num2 or num2 > num3 > num1:
                print(num3)    

    if num1 >= num2 and num1 >= num3:
        print(num1)
    else:
        if num2 >= num1 and num2 >= num3:
            print(num2)
        else:
            if num3 >= num1 and num3>= num2:
                print(num3)   


if __name__=='__main__':
    main()
