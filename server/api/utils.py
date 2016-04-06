from bcrypt import hashpw, gensalt

def hash_password(password):
    return hashpw(password.encode("utf-8"), gensalt(6))

def check_password(candidate, hashed):
    return hashpw(candidate.encode("utf-8"), hashed.encode("utf-8")) == hashed
