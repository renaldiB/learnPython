import random

lowCaps = "abcdefghijklmnopqrstuvwxyz"
bigCaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char = "!@#$%^&*_-=+()}][{;:|,./<>?"

mix = lowCaps + bigCaps + char
length = 12
randGen = "".join(random.sample(mix, length))

print("Passwords: " + randGen)