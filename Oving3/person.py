import abc


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
        reciver.recive_encoded(self.operate_cipher(text))


class reciver(person):
    def __init__(self, key, cipher):
        super().__init__(key, cipher)

    def operate_cipher(self, text):
        self.encoded_text = text
        self.decoded_text = self.cipher.decode(text, self.key)
        return self.decoded_text

    def recive_encoded(self, text):
        self.operate_cipher(text)
