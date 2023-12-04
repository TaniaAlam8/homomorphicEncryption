import seal
from seal import Ciphertext, Plaintext, SEALContext, EncryptionParameters, Encryptor, Decryptor, IntegerEncoder, Evaluator, scheme_type

def homomorphic_encryption_example():
    # Set encryption parameters
    parms = EncryptionParameters(scheme_type.BFV)
    poly_modulus_degree = 4096
    parms.set_poly_modulus_degree(poly_modulus_degree)
    parms.set_coeff_modulus(seal.CoeffModulus.BFVDefault(poly_modulus_degree))
    parms.set_plain_modulus(1024)

    # Create a SEALContext
    context = SEALContext.Create(parms)

    # Key generation
    keygen = seal.KeyGenerator(context)
    public_key = keygen.public_key()
    secret_key = keygen.secret_key()

    # Encryptor and decryptor
    encryptor = Encryptor(context, public_key)
    decryptor = Decryptor(context, secret_key)

    # Evaluator for homomorphic operations
    evaluator = Evaluator(context)

    # Encoder for encoding integers
    encoder = IntegerEncoder(context)

    # Encrypt two numbers
    plain1 = Plaintext(encoder.encode(5))
    plain2 = Plaintext(encoder.encode(10))
    encrypted1, encrypted2 = Ciphertext(), Ciphertext()
    encryptor.encrypt(plain1, encrypted1)
    encryptor.encrypt(plain2, encrypted2)

    # Homomorphic addition
    encrypted_sum = Ciphertext()
    evaluator.add(encrypted1, encrypted2, encrypted_sum)

    # Decrypt the result
    plain_sum = Plaintext()
    decryptor.decrypt(encrypted_sum, plain_sum)
    sum = encoder.decode_int32(plain_sum)

    print(f"Sum: {sum}")

homomorphic_encryption_example()