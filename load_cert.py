


# Reading a pkcs12 certificate with pyOpenSSL.crypto
# http://stackoverflow.com/questions/6345786/python-reading-a-pkcs12-certificate-with-pyopenssl-crypto

from OpenSSL import crypto

# open it, using password. Supply/read your own from stdin.
p12 = crypto.load_pkcs12(file("/path/to/cert.p12", 'rb').read(), passwd)

# get various properties of said file.
# note these are PyOpenSSL objects, not strings although you
# can convert them to PEM-encoded strings.
p12.get_certificate()     # (signed) certificate object
p12.get_privatekey()      # private key.
p12.get_ca_certificates() # ca chain.
