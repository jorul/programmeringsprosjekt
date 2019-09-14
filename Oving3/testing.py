from cipher import *
from person import *
from crypto_utils import *
import string


senderen = sender("cake", unbreakable())
mottaker = reciver("cake", unbreakable())
hackeren = Hacker()

senderen.send_encoded(mottaker, "I like to eat")
print(senderen)
print(mottaker)
print()

senderen.send_encoded_to_hacker(hackeren, "I like to eat")
