import string
#If you do not want to use inbuilt function, you can define your digits, i.e 0 to 9

def is_Nigeria(number):
    """This program checks whether a number is Nigerian number or not"""
    y = string.digits 
    for i in number:
        assert (i in y), "Enter a valid phone number"  #This ensures that the number contains digits only.
    
    status = True
    if number[:3]=="234" and len(number) == 13: #This checks for length
        status = True
    elif (number[:2] == "07" or number[:2] == "08" or number[:2] == "09") and len(number) == 11: #This checks for length
        status = True
    else:
        status = False
        
    return status

user = str(input('Enter phone number here: '))
print(is_Nigeria(user))