from passlib.hash import pbkdf2_sha256

def create_hash_password(password:str):
    hashed_password = pbkdf2_sha256.hash(password)
    return hashed_password

def verify_password_from_hash(password:str):
    login = pbkdf2_sha256.verify(password)
    return login