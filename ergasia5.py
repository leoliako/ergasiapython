m = 0
with open('words.txt','r') as f:
    for line in f:
            for word in line.split():
                word = word.replace('.' , '')
                word = word.replace(',' , '')
                word = word.replace("'" , '')
                for i in word:                   
                    m = m + 1	
                if( m > 3 ): 
                    wo1 = word
                    last = word[0]
                    wo = word[1:]
                    wo2 = wo + (last) + ( "ay" )
                    print wo2
                else:
                    print word
                                
                m = 0