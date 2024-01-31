
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    caffeine_mg /= 2
    print('After 6 hours: ' + f'{caffeine_mg:.2f}' + ' mg')
    caffeine_mg /= 2
    print('After 12 hours: ' + f'{caffeine_mg:.2f}' + ' mg')
    caffeine_mg /= 4
    print('After 24 hours: ' + f'{caffeine_mg:.2f}' + ' mg')
if __name__ == "__main__":
    caffeine()