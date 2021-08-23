def main():
    #escribe tu código abajo de esta línea
    peso = float(input('Peso en kg: '))
    altura = float(input('Altura en m: '))

    bmi = (peso / (altura**2))

    if bmi < 20 and bmi>0:
         print('PESO BAJO')
    else:
         if bmi<=0:
              print('Revisa tus datos, alguno de ellos es erróneo.')
         else:
              if 20 <= bmi < 25:
                   print('NORMAL')
              else:
                   if 25 <= bmi < 30:
                        print('SOBREPESO')
                   else:
                        if 30 <= bmi < 40:
                             print('OBESIDAD')
                        else:
                             if bmi >= 40:
                                  print('OBESIDAD MORBIDA')
if __name__=='__main__':
    main()
