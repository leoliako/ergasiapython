from __future__ import division
dict = {}
i=1
foros = input('Dwse ton foro se klimaka 100%....p.x 14... :')
name = raw_input('Dwse onoma agoras..otan theleis na stamatiseis dwse gia onoma TELOS :')
while name != 'TELOS':
    if i >= 2:
        name = raw_input('Dwse onoma agoras neou adikeimenou..otan theleis na stamatiseis dwse gia onoma TELOS :')
    if name != 'TELOS':
        price = input('Dwse timh agoras:')
        dict[name] = price
    i = i + 1
def my_function(dictionary , forostimis):
    sum = 0
    teltimi = 0
    for x in dictionary:
        sum = sum + dictionary[x]
    foro = sum*forostimis/100
    teltimi = sum + foro
    
    return teltimi

print("H teliki timh einai mazi me ton foro einai :",my_function(dict , foros))
