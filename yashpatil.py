import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
symbols="!@#$%^&*()"
numbers="0123456789"
length=10
string=upper+lower+symbols+numbers
passward="".join(random.sample(string,length))
print(passward)