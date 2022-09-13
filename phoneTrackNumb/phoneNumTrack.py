import phonenumbers

from phonenumbers import geocoder

inp = input("Tulis Nomor Telepon (example: +62xxxxxxxxxxx): ")
hpNum = phonenumbers.parse(inp)

print(geocoder.description_for_number(hpNum,'en'))