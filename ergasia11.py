f = open('numbers.txt','r')
flag = 1
metr = 0
allcombos = []
m = 0
n = 0
num = []
numbers = []
while (metr < 6):
    print("Give number from 1 to 9 !")
    numb = int(input())
    if ( numb <= 9 and numb >=1 ):
        numbers.append(numb)
        metr = metr + 1
    else:
        print "This is not a number from 1 to 9"
combos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
combos[0] = int(str(numbers[0]) + str(numbers[1]) + str(numbers[2]) + str(numbers[3]))
combos[1] = int(str(numbers[0]) + str(numbers[1]) + str(numbers[2]) + str(numbers[4]))
combos[2] = int(str(numbers[0]) + str(numbers[1]) + str(numbers[2]) + str(numbers[5]))
combos[3] = int(str(numbers[0]) + str(numbers[1]) + str(numbers[3]) + str(numbers[4]))
combos[4] = int(str(numbers[0]) + str(numbers[1]) + str(numbers[3]) + str(numbers[5]))
combos[5] = int(str(numbers[0]) + str(numbers[1]) + str(numbers[4]) + str(numbers[5]))
combos[6] = int(str(numbers[0]) + str(numbers[2]) + str(numbers[3]) + str(numbers[4]))
combos[7] = int(str(numbers[0]) + str(numbers[2]) + str(numbers[3]) + str(numbers[5]))
combos[8] = int(str(numbers[0]) + str(numbers[2]) + str(numbers[4]) + str(numbers[5]))
combos[9] = int(str(numbers[0]) + str(numbers[3]) + str(numbers[4]) + str(numbers[5]))
combos[10] = int(str(numbers[1]) + str(numbers[2]) + str(numbers[3]) + str(numbers[4]))
combos[11] = int(str(numbers[1]) + str(numbers[2]) + str(numbers[3]) + str(numbers[5]))
combos[12] = int(str(numbers[1]) + str(numbers[2]) + str(numbers[4]) + str(numbers[5]))
combos[13] = int(str(numbers[1]) + str(numbers[3]) + str(numbers[4]) + str(numbers[5]))
combos[14] = int(str(numbers[2]) + str(numbers[3]) + str(numbers[4]) + str(numbers[5]))
for i in range(0,15):
    num1 = str(combos[i])[0]
    num2 = str(combos[i])[1]
    num3 = str(combos[i])[2]
    num4 = str(combos[i])[3]
    allcombos.append(int(num1 + num2 + num3 + num4))
    allcombos.append(int(num1 + num2 + num4 + num3))
    allcombos.append(int(num1 + num3 + num2 + num4))
    allcombos.append(int(num1 + num3 + num4 + num2))
    allcombos.append(int(num1 + num4 + num2 + num3))
    allcombos.append(int(num1 + num4 + num3 + num2))
    allcombos.append(int(num2 + num1 + num3 + num4))
    allcombos.append(int(num2 + num1 + num4 + num3))
    allcombos.append(int(num2 + num3 + num1 + num4))
    allcombos.append(int(num2 + num3 + num4 + num1))
    allcombos.append(int(num2 + num4 + num1 + num3))
    allcombos.append(int(num2 + num4 + num3 + num1))
    allcombos.append(int(num3 + num1 + num2 + num4))
    allcombos.append(int(num3 + num1 + num4 + num2))
    allcombos.append(int(num3 + num2 + num1 + num4))
    allcombos.append(int(num3 + num2 + num4 + num1))
    allcombos.append(int(num3 + num4 + num1 + num2))
    allcombos.append(int(num3 + num4 + num2 + num1))
    allcombos.append(int(num4 + num1 + num2 + num3))
    allcombos.append(int(num4 + num1 + num3 + num2))
    allcombos.append(int(num4 + num2 + num1 + num3))
    allcombos.append(int(num4 + num2 + num3 + num1))
    allcombos.append(int(num4 + num3 + num1 + num2))
    allcombos.append(int(num4 + num3 + num2 + num1))   
num = []
for line in f:
    for number in line.split():
        num.append(int(number))
        n = n + 1
for i in range(0,360):
    for j in range(0,n):
            if ( allcombos[i] == num[j] and flag == 1 ):
                print "Vrethike tetrada kai einai h :", str(num[j])[0] ,",", str(num[j])[1] ,",", str(num[j])[2] ,",", str(num[j])[3]
                flag = 0               
            else:
                m = m + 1                            
if ( m == 360*n ):
    print "Den vrethike tetrada , parakalw dwste allh ejada"