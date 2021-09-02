string = input("Write a word/number: ")

rounds = len(list(string)) // 2        # 'for' iterations
letter_pos = 1                         # to move trought string
ok = 0                                 # verification
for x in range(0,rounds):

    if string[letter_pos-1] == string[-letter_pos]:       
        letter_pos += 1
        ok += 1       
    else:
        break

if ok == rounds:
    try:
        string = int(string)
        print("\nThe number '%s' is a palindrome." % string)
    except ValueError:
        print("\nThe word '%s' is a palindrome." % string)
else:
    try:
        string = int(string)
        print("\nThe number '%s' is not a palindrome." % string)
    except ValueError:
        print("\nThe word '%s' is not a palindrome." % string)

    
