from contextlib import redirect_stdout

with open('love2.txt', 'w') as f:
    with redirect_stdout(f):
        print('\n'.join(
            [''.join(
                [('Dhea'[(x-y) % 4]
                  if((x*0.05)**2 + (y*0.1)**2-1)**3 - (x*0.05)**2 * (y*0.1)**3<=0
                    else' ')
                        for x in range(-30, 30)])
                        for y in range(15, -15, -1)]))