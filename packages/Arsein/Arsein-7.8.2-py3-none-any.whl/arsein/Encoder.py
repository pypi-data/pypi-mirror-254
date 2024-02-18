import re
import io
import json
import base64
from base64 import b64decode
from PIL import Image
import string
import secrets
from json import JSONDecoder, loads
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from string import ascii_lowercase, ascii_uppercase
from Crypto.Util.Padding import pad, unpad


class encoderjson:
    def __init__(self, auth: str, private_key: str = None):
        self.auth = auth
        self.key = bytearray(self.secret(auth), "UTF-8")
        self.iv = bytearray.fromhex("0" * 32)
        if private_key:
            self.keypair = RSA.import_key(private_key.encode("utf-8"))

    def replaceCharAt(self, e, t, i):
        return e[0:t] + i + e[t + len(i) :]

    def changeAuthType(auth_enc):
        n = ""
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = lowercase.upper()
        digits = "0123456789"
        for s in auth_enc:
            if s in lowercase:
                n += chr(((32 - (ord(s) - 97)) % 26) + 97)
            elif s in uppercase:
                n += chr(((29 - (ord(s) - 65)) % 26) + 65)
            elif s in digits:
                n += chr(((13 - (ord(s) - 48)) % 10) + 48)
            else:
                n += s
        return n

    def secret(self, e):
        t = e[0:8]
        i = e[8:16]
        n = e[16:24] + t + e[24:32] + i
        s = 0
        while s < len(n):
            e = n[s]
            if e >= "0" and e <= "9":
                t = chr((ord(e[0]) - ord("0") + 5) % 10 + ord("0"))
                n = self.replaceCharAt(n, s, t)
            else:
                t = chr((ord(e[0]) - ord("a") + 9) % 26 + ord("a"))
                n = self.replaceCharAt(n, s, t)
            s += 1
        return n

    def encrypt(self, text):
        raw = pad(text.encode("UTF-8"), AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = aes.encrypt(raw)
        result = base64.b64encode(enc).decode("UTF-8")
        return result

    def decrypt(self, text):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec = aes.decrypt(base64.urlsafe_b64decode(text.encode("UTF-8")))
        result = unpad(dec, AES.block_size).decode("UTF-8")
        return result

    def makeSignFromData(self, data_enc: str):
        sha_data = SHA256.new(data_enc.encode("utf-8"))
        signature = pkcs1_15.new(self.keypair).sign(sha_data)
        return base64.b64encode(signature).decode("utf-8")

    def decryptRsaOaep(private: str, data_enc: str):
        keyPair = RSA.import_key(private.encode("utf-8"))
        return (
            PKCS1_OAEP.new(keyPair).decrypt(base64.b64decode(data_enc)).decode("utf-8")
        )

    def encryptRsaOaep(private: str, data_enc: str):
        keyPair = RSA.import_key(private.encode("utf-8"))
        return (
            PKCS1_OAEP.new(keyPair).decrypt(base64.b64encode(data_enc)).decode("utf-8")
        )

    def rsaKeyGenerate():
        keyPair = RSA.generate(1024)
        public = encoderjson.changeAuthType(
            base64.b64encode(keyPair.publickey().export_key()).decode("utf-8")
        )
        private = keyPair.export_key().decode("utf-8")
        return [public, private]


def getThumbInline(image_bytes: bytes):
    im = Image.open(io.BytesIO(image_bytes))
    width, height = im.size
    if height > width:
        new_height = 40
        new_width = round(new_height * width / height)
    else:
        new_width = 40
        new_height = round(new_width * height / width)
    im = im.resize((new_width, new_height), Image.ANTIALIAS)
    changed_image = io.BytesIO()
    im.save(changed_image, format="PNG")
    changed_image = changed_image.getvalue()
    return base64.b64encode(changed_image)
