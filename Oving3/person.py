import abc
from crypto_utils import generate_random_prime
from crypto_utils import modular_inverse
from random import randint
from cipher import *
import string

class person():
    def __init__(self, key, cipher):
        self.key = key
        self.cipher = cipher
        self.encoded_text = None
        self.decoded_text = None

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    @abc.abstractmethod
    def operate_cypher(self):
        return

    def __str__(self):
        return f'{type(self).__name__}: encoded = {self.encoded_text}, decoded = {self.decoded_text}'


class sender(person):
    def __init__(self, key, cipher):
        super().__init__(key, cipher)

    def operate_cipher(self, text):
        self.decoded_text = text
        self.encoded_text = self.cipher.encode(text, self.key)
        return self.encoded_text

    def send_encoded(self, reciver, text):
        if isinstance(self.cipher, RSA):
            self.key = reciver.get_public_key()
        reciver.recive_encoded(self.operate_cipher(text))
    
    def send_encoded_to_hacker(self, hacker, text):
        hacker.recive_encoded(self.cipher, self.operate_cipher(text))


class reciver(person):
    def __init__(self, key, cipher):
        super().__init__(key, cipher)
        if isinstance(cipher, RSA):
            self.public_key, self.key = cipher.generate_keys()

    def operate_cipher(self, text):
        self.encoded_text = text
        self.decoded_text = self.cipher.decode(text, self.key)
        return self.decoded_text

    def recive_encoded(self, text):
        self.operate_cipher(text)

    def get_public_key(self):
        return self.public_key


class Hacker(person):
    def __init__(self,):
        self.libary = open('/Users/jorunn/Documents/fragithub/programmeringsprosjekt/Oving3/english_words.txt').read().split()

    def text_to_word_list(self, text):
        liste = text.split()
        for i in range(0, len(liste)):
            liste[i] = liste[i].translate(str.maketrans('', '', string.punctuation))
            liste[i] = liste[i].lower()
        return liste

    def decode_text(self, cipher, encoded_text):
        if isinstance(cipher, ceasar):
            keys = [x for x in range(0, 95)]
            return self.find_the_decoded(cipher, encoded_text, keys)
        
        elif isinstance(cipher, multiplicative):
            keys = []
            for i in range(95):
                if modular_inverse(i, 95):
                    keys.append(i)
            return self.find_the_decoded(cipher, encoded_text, keys)

        elif isinstance(cipher, affine):
            keys = []
            for i in range(95):
                for j in range(95):
                    if modular_inverse(j, 95):
                        this_key = (j, i)
                        keys.append(this_key)
            return self.find_the_decoded(cipher, encoded_text, keys)
        
        elif isinstance(cipher, unbreakable):
            keys = self.libary
            return self.find_the_decoded(cipher, encoded_text, keys)
    
    def find_the_decoded(self, cipher, encoded_text, keys):
        words_pr_key = self.check_key(cipher, encoded_text, keys)
        if len(words_pr_key) == 0:
            return None
        the_key = self.most_likely_key(cipher, words_pr_key)
        return cipher.decode(encoded_text, the_key)
    
    def check_key(self, cipher, encoded_text, keys):
        words_pr_key = {}
        for possible_key in keys:
            decoded = cipher.decode(encoded_text, possible_key)
            decoded_listed = self.text_to_word_list(decoded)
            counter = 0
            for word in decoded_listed:
                if word in self.libary:
                    counter += 1
            if counter != 0:
                words_pr_key[possible_key] = counter
        return words_pr_key
    
    def most_likely_key(self, cipher, words_pr_key):
        the_key = 0
        nr_of_words = 0
        for key in words_pr_key:
            if words_pr_key[key] > nr_of_words:
                the_key = key
                nr_of_words = words_pr_key[key]
        return the_key

    def recive_encoded(self, cipher, text):
        result = self.decode_text(cipher, text)
        print(f'Hacker result = {result}')




