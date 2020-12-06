#RANDOM PASSWORD GENERATOR
import random
from string import digits, punctuation, ascii_letters
length = int(input())   #LENGTH OF PASSWORD NEEDED
symbols = ascii_letters + digits + punctuation # WHAT PASSWORD MAY CONTAIN
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(symbols) for i in range(length))
print(password)
