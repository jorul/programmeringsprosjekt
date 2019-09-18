from cipher import *
from person import *
from crypto_utils import *
import string


senderen = sender("cake", Unbreakable())
mottaker = reciver("cake", Unbreakable())
hackeren = Hacker()

senderen.send_encoded(mottaker, "eating is nice")
print(senderen)
print(mottaker)
print()

senderen.send_encoded_to_hacker(hackeren, "eating is nice")
