






import time
def newsection():
    print("\n--------------\n")
print('WELCOME...\nIf you have not alreadry, look in the pictures for\n your cards.  On the back are letters that\n correspond to the questions. Answer them correctly.')
time.sleep(2)
newsection()
one=input("What did you get for riddle c? ").upper()
if one=="TOY":
    print("Correct")
else:
    print("Close, but no cigar...")
    quit()
time.sleep(1)
newsection()
two=input("What did you get for riddle a? ").upper()
if two=="ACE":
    print("Correct")
else:
    print("Close, but no cigar...")
    quit()
    
time.sleep(1)
newsection()
thr=input("What did you get for riddle r? ").upper()
if thr=="JUICE":
    print("Correct")
else:
    print("Close, but no cigar...")
    quit()
    
time.sleep(1)
newsection()
fou=input("What did you get for riddle d? ").upper()
if fou=="TURK":
    print("Correct")
else:
    print("Almost, but no cigar...")
    quit()
    
time.sleep(1)
newsection()
fiv=input("What did you get for riddle s? ").upper()
if fiv=="SIN":
    print("Correct\nPress ENTER to continue")
    end=input()
else:
    print("Really Close, but no cigar...")
    quit()
newsection()
print("Now use the blanks on the card to solve the problem, \nGood luck.")
end=input()