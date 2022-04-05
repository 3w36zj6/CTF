from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Util.number import inverse, long_to_bytes
import Crypto.PublicKey.RSA as RSA

N = 1763350599372172240188600248087473321738860115540927328389207609428163138985769311
E = 65537
C = 33475248111421194902497742876885935310304862428980875522333303840565113662943528
p = 31415926535897932384626433832795028841
q = 56129192858827520816193436882886842322337671

d = inverse(E, (p-1)*(q-1))

rsa_key = RSA.construct((N, E, d))

print(long_to_bytes(rsa_key.decrypt(C)))  # shell{switchin_to_asymmetric}
