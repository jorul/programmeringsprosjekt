from cipher import affine
from person import *
from crypto_utils import *

senderen = sender((2, 1), affine())
mottaker = reciver((2, 1), affine())

senderen.send_encoded(mottaker, "abc, it's easy like 123")
print(senderen)
print(mottaker)
