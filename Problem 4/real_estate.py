
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here

    estmorg = (current_price * 0.051) / 12
    change = current_price - last_month_price

    print('This house is $' + str(current_price) + '. The change is $' + str(change) +  ' since last month.')
    print('The estimated monthly mortgage is $' + f'{estmorg:.2f}' + '.')

if __name__ == "__main__":
    real_estate()