#Дополнительное практическое задание по модулю: "Основные операторы"
#Задание "Слишком древний шифр"
n = int(input('Введите число: '))
code = []
for i in range(1,n):
    for j in range(i+1,n):
        #if (i+j)<n:       #Если добавить следующие 2 строки,исключаются делители
          #  continue      #меньшего значения, чем введённое число
        if n % (i+j) == 0:
           code.append(i)
           code.append(j)
print(*code)