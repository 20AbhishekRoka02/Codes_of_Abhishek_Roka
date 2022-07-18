"""
Code to encode the string given by user.

It will accept string of length more than or equal to 10.

Implementation:

Testcase 1:

Input:
"aaabbbcccd"
Output:
"a3b3c3d1"

Testcase 2:

Input:
"abcd"
Output:
"String should contain characters more than or equal to 10."

"""




def encoder(size,string):
    
    encoded = ""
    count = 1
    keeper = {}
    for i in range(size):
        if i==0:
            keeper[string[i]] = count
        
        else:
            if string[i] not in keeper.keys():
                keeper[string[i]] = count
            
            else:
                keeper[string[i]] += 1

    for i in keeper.keys():
        encoded = encoded + i + str(keeper[i])
    
    return encoded


user_string = input("Enter String: ")

if len(user_string) < 10:
    print("Given string should be 10 characters long.")

else:
    print(encoder(len(user_string),user_string))
