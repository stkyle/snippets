
# http://stackoverflow.com/questions/6345786/python-reading-a-pkcs12-certificate-with-pyopenssl-crypto
# load everything. Probably not the best idea in production...
from OpenSSL.crypto import *

# open it, using password. Supply/read your own from stdin.
p12 = load_pkcs12(file("/path/to/cert.p12", 'rb').read(), passwd)

# get various properties of said file.
# note these are PyOpenSSL objects, not strings although you
# can convert them to PEM-encoded strings.
p12.get_certificate()     # (signed) certificate object
p12.get_privatekey()      # private key.
p12.get_ca_certificates() # ca chain.
