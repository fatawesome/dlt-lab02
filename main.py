import math

def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
    return gcd, x, y


def rsa_kek(p, q):
    e = 3

    n = p * q  # product of primes
    phi = (p - 1) * (q - 1)  # modular multiplicative inverse
    gcd, a, b = egcd(e, phi)  # calling extended euclidean algorithm
    d = a + phi  # a is decryption key

    return n, e, d


n, e, d = rsa_kek(53, 59)
print(n, e, d)

def encrypt(e, n, data_as_number):
    return (data_as_number ** e) % n

def decrypt(d, n, msg):
    return (msg ** d) % n


plaintext = 1234
ciphertext = encrypt(e, n, plaintext)
decrypted_plaintext = decrypt(d, n, ciphertext)

print('Ciphertext: ', ciphertext)
print('Decrypted ciphertext: ', decrypted_plaintext)