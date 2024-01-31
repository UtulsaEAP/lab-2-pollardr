def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    right = phone_number % 10000
    phone_number = phone_number//10000
    middle = phone_number % 1000
    phone_number = phone_number//1000
    print('(' + str(phone_number) + ') '+ str(middle) + '-' + str(right))
    
if __name__ == "__main__":
    telephone()