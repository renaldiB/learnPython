import time, tqdm

bar = 0

for i in tqdm.tqdm(range(100)):
    bar += 1
    time.sleep(0.1)

if bar == 100:
    print(f'{bar}% Fully Loaded')
else:
    print(f'Not Fully Loaded, Just {bar}%')
