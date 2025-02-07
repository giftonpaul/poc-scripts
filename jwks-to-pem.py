import base64
import json
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# JWKS Response (Replace with actual values)
jwks = {
  "keys": [
    {
      "kty": "RSA",
      "e": "AQAB",
      "use": "sig",
      "kid": "xxx",
      "alg": "RS256",
      "n": "xxx"
    }
  ]
}
# Extract the modulus (n) and exponent (e)
n_b64 = jwks["keys"][0]["n"]
e_b64 = jwks["keys"][0]["e"]

# Decode Base64URL
n_bytes = base64.urlsafe_b64decode(n_b64 + '==')
e_bytes = base64.urlsafe_b64decode(e_b64 + '==')

# Convert exponent to integer
e_int = int.from_bytes(e_bytes, byteorder="big")
n_int = int.from_bytes(n_bytes, byteorder="big")

# Create the RSA public key
public_key = rsa.RSAPublicNumbers(e_int, n_int).public_key(default_backend())

# Convert to PEM format
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save to file
with open("public.pem", "wb") as f:
    f.write(pem)

print("PEM Public Key:\n", pem.decode())
