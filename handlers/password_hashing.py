import random
import string
import hashlib

# implement the function make_salt() that returns a string of 5 random
# letters use python's random module.
# Note: The string package might be useful here.

def make_salt():
    ###Your code here
    a = "".join(random.choice(string.ascii_letters) for x in range(5))
    return a

###########
#test code#
###########
# a = make_salt();
# print a

########################################

# implement the function make_pw_hash(name, pw) that returns a hashed password 
# of the format: 
# HASH(name + pw + salt),salt
# use sha256

def make_pw_hash(name, pw):
    ###Your code here
    salt = make_salt();
    put = name + pw + salt
    hash_value = hashlib.sha256(put).hexdigest()
    return "%s,%s" % (hash_value, salt)

###########
#test code#
###########
# a = make_pw_hash("aa","123")
# print a

########################################

# Implement the function valid_pw() that returns True if a user's password 
# matches its hash. You will need to modify make_pw_hash.

def valid_pw(name, pw, h):
    ###Your code here
    salt = h.split(",")[1]
    prev_hash_value = h.split(",")[0]
    hash_value = hashlib.sha256(name + pw + salt).hexdigest()
    if prev_hash_value == hash_value:
        return True
    else:
        return False

###########
#test code#
###########
# h = make_pw_hash('spez', 'hunter2')
# print valid_pw('spez', 'hunter2', h)

