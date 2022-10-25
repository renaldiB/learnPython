import time

def timer(count):
    while count:
        mins, secs = divmod(count, 60)
        formatTime = "{:02d} {:1s} {:02d} {:1s}".format(mins,"m",secs,"s")
        print(formatTime, end= "\r")
        
        time.sleep(1)
        count -= 1

    print("Times Up ")
        
inp = int(input("Set Timer (s): "))
timer(inp)