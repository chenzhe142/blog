import hmac

#instead of doing: visits=1
#				   visits=1|md5(1)
#
#we hash cookie with a secret string:
#				   visits=1|hmac(secret,1)
#
#bad guys can't trace back to modify the cookie

# Implement the hash_str function to use HMAC and our SECRET instead of md5
SECRET = 'imsosecret'
def hash_str(s):
	#hash string, using hmac and SECRET
	return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
	#put string and hashed value into a proper format
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    val = h.split('|')[0]
    #check if hash value is the corresponding string
    if h == make_secure_val(val):
        return val