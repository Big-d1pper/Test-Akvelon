class NumberFormatter:
    def parseInt():
        """
        функция принемает значение введеное пользователем, проверяет наличие знака
        перед числом, дальше исходя какой знак выполняет функцию 'number_list_constructor'
        стоставив спиок превращает его в эдиное число с учетом знака
        """
        enter_number = input('Enter data :')
        if enter_number == '':
            print('Your string is empty')
        else:

            def number_list_constructor(num):
                """
                функция принимает значение из цикла перебора спииска,
                перебирая все числа, и состовляет список ужее из целочисленных значений
                """
                if num == '0':
                    num = 0
                elif num == '1':
                    num = 1
                elif num == '2':
                    num = 2
                elif num == '3':
                    num = 3
                elif num == '4':
                    num = 4
                elif num == '5':
                    num = 5
                elif num == '6':
                    num = 6
                elif num == '7':
                    num = 7
                elif num == '8':
                    num = 8
                elif num == '9':
                    num = 9
                list_number.append(num)

            list_number = []
            if enter_number[0] == '+':

                for number in enter_number[1:]:
                    number_list_constructor(number)

                print(sum(d * 10 ** i for i, d in enumerate(list_number[::-1])))

            elif enter_number[0] == '-':

                for number in enter_number[1:]:
                    number_list_constructor(number)

                print(sum(d * 10 ** i for i, d in enumerate(list_number[::-1])) * -1)

            else:

                for number in enter_number:
                    number_list_constructor(number)

                print(sum(d * 10 ** i for i, d in enumerate(list_number[::-1])))


    parseInt()


