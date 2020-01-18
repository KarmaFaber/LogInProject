

#----------------------------------------------------------
import hashlib

#--------------------------------#encript password#---------------------------------
#sha1------------------------------------------------------
def encrypt_password_sha1(password):
    encrypt=hashlib.sha1(password.encode())
    return encrypt.hexdigest()

#sha224-----------------------------------------------------
def encrypt_password_sha224(password):
    encrypt=hashlib.sha224(password.encode())
    return encrypt.hexdigest()

#sha384------------------------------------------------------
def encrypt_password_sha384(password):
    encrypt=hashlib.sha384(password.encode())
    return encrypt.hexdigest()

#sha256-------------------------------------------------------
def encrypt_password_sha256(password):
    encrypt=hashlib.sha256(password.encode())
    return encrypt.hexdigest()

#sha512-------------------------------------------------------
def encrypt_password_sha512(password):
    encrypt=hashlib.sha512(password.encode())
    return encrypt.hexdigest()

#md5----------------------------------------------------------
def encrypt_password_md5(password):
    encrypt=hashlib.md5(password.encode())
    return encrypt.hexdigest()

