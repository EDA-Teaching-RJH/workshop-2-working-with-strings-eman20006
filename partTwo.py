import math  

def main():
#TO DO  
 A = int(input("What does A equal?"))
 B = int(input("What does B equal?"))
 pythag(A,B)

def pythag(A,B):    
 AplusB = (A**2) + (B**2)
 input = math.sqrt(AplusB)
 print(input)

main()
