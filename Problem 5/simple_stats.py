
# Riley Pollard
# Eng Appl Prog Thursday Lab

def simple_stats():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    ''' Type your code here. '''

    result1 = num1*num2*num3*num4
    avg = (num1+num2+num3+num4)/4
    print(f'{result1:.0f}' + ' ' + f'{avg:.0f}')
    print(f'{result1:.3f}' + ' ' + f'{avg:.3f}')

if __name__ == "__main__":
    simple_stats()