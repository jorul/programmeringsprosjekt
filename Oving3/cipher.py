from crypto_utils import *
import abc


class cipher:
    def __init__(self):
        self.alphabet = [chr(x) for x in range(32, 127)]

    @abc.abstractmethod
    def encode(self, text, key):
        return

    @abc.abstractmethod
    def decode(self, text, key):
        return

    def vertify(self, text, key):
        return text == self.decode(self.encode(text, key), key)


class ceasar(cipher):
    def __init__(self):
        super().__init__()

    def encode(self, text, key):
        text_list = [char for char in text]
        for i in range(0, len(text_list)):
            index_in_alphabet = self.alphabet.index(text_list[i])
            new_index_in_alphabet = (index_in_alphabet + key) % 95
            text_list[i] = self.alphabet[new_index_in_alphabet]
        return ''.join(str(e) for e in text_list)

    def decode(self, text, key):
        return self.encode(text, 95-key)


class multiplicative(cipher):
    def __init__(self):
        super().__init__()

    def encode(self, text, key):
        text_list = [char for char in text]
        for i in range(0, len(text_list)):
            index_in_alphabet = self.alphabet.index(text_list[i])
            new_index_in_alphabet = (index_in_alphabet * key) % 95
            text_list[i] = self.alphabet[new_index_in_alphabet]
        return ''.join(str(e) for e in text_list)

    def decode(self, text, key):
        return self.encode(text, modular_inverse(key, 95))


class affine(cipher):
    def __init__(self):
        super().__init__()

    def encode(self, text, key):
        return ceasar().encode(multiplicative().encode(text, key[0]), key[1])

    def decode(self, text, key):
        return multiplicative().decode(ceasar().decode(text, key[1]), key[0])

class unbreakable(cipher):
    def __init__(self):
        super().__init__()
    
    def encode(slef,text, key):
        
