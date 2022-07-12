from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

plt.grid(True)

def createAxis(ax):
    ax.axhline(y=0, color='k')   
    ax.axvline(x=0, color='k')
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

n = {1}
def programmsLogic(i):
    global n
    new_n = set()
    for num in n:
        if num % 3 != 0:
            number = int(num*2)
            if number % 3 != 0:
                color = 'r'
            else:
                color = 'b'
            new_n.add(number)
            plt.annotate(number, xy=(float(i),float(number)))
            plt.plot([i-1, i], [num, number], 'ro-', color = color)
        if (num-1) % 3 == 0 and not (num-1)/3 % 2 == 0 and not num in [1,4]:
            number = int((num-1)/3)
            if number % 3 != 0:
                color = 'r'
            else:
                color = 'b'
            new_n.add(number)
            if number % 3 == 0:
                plt.annotate(f'{number}*2^n', xy=(float(i),float(number)))
            else:
                plt.annotate(number, xy=(float(i),float(number)))
            plt.plot([i-1, i], [num, number], color)
    n = new_n

command = input('1. Build Graph.\n2. Count of iterations\n')
if command == '1':
    print('Enter count of iterations')
    count = int(input())
    for i in range(count):
        ax = plt.gca()
        createAxis(ax)
        ax.set_ylim(0, 100)
        ax.set_xlim(0, count)

        programmsLogic(i+1)
        
        plt.title('The Collatz hypothesis')
        ax.set_xlabel('x', horizontalalignment='right', x=1)
        ax.set_ylabel('n', verticalalignment='top', y=1)
        
        red_patch = mpatches.Patch(color='red', label='Branching exponent')
        blue_patch = mpatches.Patch(color='blue', label='Non-branching exponent')
        ax.legend(handles=[red_patch, blue_patch])
    plt.show()
elif command == '2':
    num = int(input('Number: '))
    dels = 0
    i = 0
    if num > 0:
        while num != 1:
            if num % 2 == 0:
                num /= 2
                dels += 1
            else:
                num = num*3 + 1
            i += 1
        print(f'Count of iterations: {i}\nCount of n / 2: {dels}\nCount of 3n + 1: {i-dels}')
        
    
