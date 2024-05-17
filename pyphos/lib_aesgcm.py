import hashlib
import os
from binascii import hexlify, unhexlify
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

import lib_phos
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

def deriveKey(passphrase: str, salt: bytes=None) -> [str, bytes]:
    if salt is None:
        salt = os.urandom(8)
    return hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf8"), salt, 1000), salt


def encrypt(passphrase: str, plaintext: str) -> str:
    key, salt = deriveKey(passphrase)
    aes = AESGCM(key)
    iv = os.urandom(12)
    plaintext = plaintext.encode("utf8")
    ciphertext = aes.encrypt(iv, plaintext, None)
    return "%s-%s-%s" % (hexlify(salt).decode("utf8"), hexlify(iv).decode("utf8"), hexlify(ciphertext).decode("utf8"))


def decrypt(passphrase: str, ciphertext: str) -> str:
    salt, iv, ciphertext = map(unhexlify, ciphertext.split("-"))
    key, _ = deriveKey(passphrase, salt)
    aes = AESGCM(key)
    plaintext = aes.decrypt(iv, ciphertext, None)
    return plaintext.decode("utf8")

def f_dcr():
    # print( globals() )
    print( '  in dcr: ', lib_phos.S )
    S = lib_phos.S
    S.append( decrypt( S.pop(), S.pop() ) )

S = lib_phos.S

from Crypto.PublicKey import RSA

def f_imk():
  # recipient_key = RSA.import_key(open("receiver.pem").read())
  S.append( RSA.import_key( S.pop() ) )

def f_cipher(): # run imk: cipher: !! before recr: rdcr:
  # cipher_rsa = PKCS1_OAEP.new(recipient_key) 
  S.append( PKCS1_OAEP.new( S.pop() ) )

def f_recr(): # RSA encrypt
  # E=cipher_rsa.encrypt(data)
  C = S[-2] # no pop, reuse
  S.append( C.encrypt( S.pop() ) )

def f_u8():
  S.append( S.pop().encode("utf-8") )
  
def f_u8d():
  S.append( S.pop().decode("utf-8") )
  # b"abcde".decode("utf-8")   

def f_rdcr(): # RSA decrypt
  # E=cipher_rsa.encrypt(data)
  C = S[-2] # no pop, reuse
  S.append( C.decrypt( S.pop() ) )

from Crypto.Hash import SHA256
def f_oaep():
  S.append(PKCS1_OAEP.new( S.pop(), SHA256 ))


if __name__ == "__main__":
    ciphertext = encrypt("hello", "world")
    print(ciphertext)
    print(decrypt("hello", ciphertext))
    print(decrypt("hello", "6102677198e41d98-84c95e2d7caf6f2d4ccbfe3c-3093cef35d0dba7a24d37f7d4580b5ad83c154329c"))

    ENCRYPTED="7f93df718916b681-f91958d638e9c28cdb4ec0c7-c5d4966507365f35e40ccde3963ac5f782ed787e10"

    print(decrypt("hello", ENCRYPTED))

