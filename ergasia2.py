c = 0
b = 0
with open('words.txt','r') as f:
    for line in f:
          for word in line.split(): 
                  
                  for i in word:
                      if( i == 'b' or i == 'd' or i == 'g' or i == 'h' or i == 'l' or i == 'm' or i == 'n' or i == 'p' or i == 'q' or i == 's' or i == 't' or i == 'v' or i == 'w' or i == 'x' or i == 'y' or  i == 'B' or  i == 'D' or  i == 'G' or  i == 'H' or  i == 'L' or  i == 'M' or  i == 'N' or  i == 'P' or  i == 'Q' or  i == 'S' or  i == 'T' or  i == 'V' or  i == 'W' or  i == 'X' or  i == 'Y' ):
                          c = c + 1
                      if( i == 'f' or i == 'c' or i == 'k' or i == 'r' or i == 'F' or i == 'C' or i == 'K' or i == 'R'): 
                          b = b + 1 
                  
                  if  (  b > c  and word != 'of' and word != 'for' and word != 'or' and word != 'are' and word != 'if'):
                     print ( "The word", word , "is bad" )
                  else:
                     print ( "The word", word , "is good" )                  
                  c = 0 
                  b = 0
          