"""Module for superclass cipher and all types of ciphers"""
import abc
from random import randint
from crypto_utils import modular_inverse, blocks_from_text, text_from_blocks, generate_random_prime



class Cipher:
    """abstract class with abstract classes encode and decode"""
    def __init__(self):
        self.alphabet = [chr(x) for x in range(32, 127)]

    @abc.abstractmethod
    def encode(self, text, key):
        """abstract method for encoding"""
        return

    @abc.abstractmethod
    def decode(self, text, key):
        """abstract method for decoding"""
        return

    def vertify(self, text, key):
        """method for verifying that the encoding and decoding is correct"""
        return text == self.decode(self.encode(text, key), key)


class Ceasar(Cipher):
    """clss using additon to encode"""
    def __init__(self):
        super().__init__()

    def encode(self, text, key):
        """method adding ASCII-values to encode"""
        text_list = [char for char in text]
        for i in range(0, len(text_list)):
            index_in_alphabet = self.alphabet.index(text_list[i])
            new_index_in_alphabet = (index_in_alphabet + key) % 95
            text_list[i] = self.alphabet[new_index_in_alphabet]
        return ''.join(str(e) for e in text_list)

    def decode(self, text, key):
        """method to find inverse key and decode"""
        return self.encode(text, 95-key)


class Multiplicative(Cipher):
    """Class using multiplying to encode"""
    def __init__(self):
        super().__init__()

    def encode(self, text, key):
        """method to encode using multiplying ASCII-values with key"""
        text_list = [char for char in text]
        for i in range(0, len(text_list)):
            index_in_alphabet = self.alphabet.index(text_list[i])
            new_index_in_alphabet = (index_in_alphabet * key) % 95
            text_list[i] = self.alphabet[new_index_in_alphabet]
        return ''.join(str(e) for e in text_list)

    def decode(self, text, key):
        """method to find inverse key and decode"""
        return self.encode(text, modular_inverse(key, 95))


class Affine(Cipher):
    """Class using both multiplying and addition to encode"""
    def __init__(self):
        super().__init__()

    def encode(self, text, key):
        return Ceasar().encode(Multiplicative().encode(text, key[0]), key[1])

    def decode(self, text, key):
        return Multiplicative().decode(Ceasar().decode(text, key[1]), key[0])


class Unbreakable(Cipher):
    """Class using word to encode"""
    def __init__(self):
        super().__init__()

    def encode(self, text, key):
        text_list = [char for char in text]
        counter = 0
        for i in range(0, len(text_list)):
            index_in_alphabet = self.alphabet.index(text_list[i])
            key_index_in_alphabet = self.alphabet.index(key[counter])
            new_index_in_alphabet = (index_in_alphabet + key_index_in_alphabet) % 95
            text_list[i] = self.alphabet[new_index_in_alphabet]
            counter += 1
            if counter == len(key):
                counter = 0
        return ''.join(str(e) for e in text_list)

    def decode(self, text, key):
        new_key_list = []
        for char in key:
            inverse_char = self.alphabet[95 - self.alphabet.index(char) % 95]
            new_key_list.append(inverse_char)
        new_key = ''.join(str(e) for e in new_key_list)
        return self.encode(text, new_key)


class RSA(Cipher):
    """Class using RSA method to encode and decode"""
    def encode(self, text, key):
        n, e = key
        block_list = blocks_from_text(text, 1)
        return [pow(t, e, n) for t in block_list]

    def decode(self, text, key):
        n, d = key
        blocks = [pow(t, d, n) for t in text]
        decoded_text = text_from_blocks(blocks, 1)
        return decoded_text

    @staticmethod
    def generate_keys():
        """genererer nøkler og returnerer [private-key, public-key]"""
        p_1 = 1
        q = 1
        while p_1 == q:
            p_1 = generate_random_prime(8)
            q = generate_random_prime(8)
        n = p_1 * q
        phi = (p_1-1)*(q-1)
        d = None
        while d is None:
            e = randint(3, phi - 1)
            anwser = modular_inverse(e, phi)
            if anwser:
                d = anwser
        public_key = (n, e)
        private_key = (n, d)
        return (public_key, private_key)
