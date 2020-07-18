while 1:
    var = int(input("enter the number:"))
    if var <= 10:
        print('not')


    if var == 100:
        print('not')


    if var == 1000:
        print('not')


    if var > 10:
        if var < 100:
            for i in range(1,10):
                if i == (var//10):
                    if i == (var%10):
                        print('polindrom')
                        break
                    else:
                     print('not')


    if var > 100:
        if var < 1000:
          for i in range(1,10):
            if i == (var//100):
              if i == (var%10):
                print('polindrom')
                break
              else:
               print('not')

