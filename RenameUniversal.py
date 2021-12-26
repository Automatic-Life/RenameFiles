#Данная программа является частным случаем и очень ограничена в использовании, требует доработки
#! Название файлов должно иметь формат "имя файла 1 [имя автора](номер).расширение файла"
#! Файлы переименовываются по образцу
#! Образцом становится последний файл (в лексиграфическом порядке)
#! В папке переименования не должно находится посторонних файлов и директорий

import os


pathFiles = "D:\Downloads\Rename" #Директория, в которой находятся файлы, должна быть с большой буквы
listOfFiles = os.listdir(pathFiles) #Список из имен файлов формируется в лексиграфическом порядке

sample = listOfFiles[len(listOfFiles)-1] #Образец (sample) - имя последнего в списке файла
numberOfRenameFiles = len(listOfFiles) - 1 #Исключаем для переименования последний элемент (образец)

#Сортировка
#1.Создаем список из целых чисел, спарсенных из имен файлов 
listOfUnsortedNumbers = []
for i in range (numberOfRenameFiles):   
    currentElement = listOfFiles[i]
    
    pointCharPosition = currentElement.rfind('.')
    braceCharPosition = currentElement.rfind(']')
    lengthBetweenPointAndBrace = pointCharPosition - braceCharPosition 

    if lengthBetweenPointAndBrace == 4: # если однозначное число
        listOfUnsortedNumbers.append(int((currentElement[pointCharPosition-2:pointCharPosition-1])))   
    elif lengthBetweenPointAndBrace == 5: # если двухзначное число
        listOfUnsortedNumbers.append(int((currentElement[pointCharPosition-3:pointCharPosition-1])))
    elif lengthBetweenPointAndBrace == 6: # если трехзначное число
        listOfUnsortedNumbers.append(int((currentElement[pointCharPosition-4:pointCharPosition-1])))
    else:
        listOfUnsortedNumbers.append(int((currentElement[pointCharPosition-5:pointCharPosition-1])))

#2.Создаем список из отсортированных индексов
listOfSortedIndex = [i[0] for i in sorted(enumerate(listOfUnsortedNumbers), key=lambda x:x[1])]

#3.Создаем новый список из имен файлов, расположенный в нужном нам порядке
listOfSortedFiles = []
for i in range (numberOfRenameFiles):
    listOfSortedFiles.append(listOfFiles[listOfSortedIndex[i]])

#Ищем в середине названия образца символ [ и разбиваем название на части относительно еденицы
numberRename = (sample.rfind('[')) 
beginingOfName = sample[:numberRename-2]
endOfName = sample [numberRename-1:]

for i in range(numberOfRenameFiles): #Берем элементы из списка с 0-го по numberOfRenameFiles-1
    
    #Меняем номер у образца
    middleOfName = str(i+2) #Нулевой в списке элемент на самом деле второй
    name = beginingOfName + middleOfName + endOfName

    #Переименовываем файлы
    oldFileName = os.path.join(pathFiles, listOfSortedFiles[i])
    newFileName = os.path.join(pathFiles, name)
    os.rename(oldFileName, newFileName)






