import hashlib

from django.core import signing


class Token(object):
    HEADER = {
        'type': 'JWT',
        'alg': 'HS256'
    }

    def encrypt(self, value):
        data = signing.dumps(value)
        data = signing.b64_encode(data.encode()).decode()
        return data

    def decrypt(self, value):
        data = signing.b64_decode(value.encode()).decode()
        data = signing.loads(data)
        return data

    def get_token(self, headers, payloads):
        header = self.encrypt(headers)
        payload = self.encrypt(payloads)
        md5 = hashlib.md5()
        md5.update(("%s.%s" % (header, payload)).encode())
        signature = md5.hexdigest()
        token = "%s.%s.%s" % (header, payload, signature)
        return token
