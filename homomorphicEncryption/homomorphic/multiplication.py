import seal
from seal import Ciphertext, Plaintext, SEALContext, EncryptionParameters, Encryptor, Decryptor, IntegerEncoder, Evaluator, scheme_type

def homomorphic_multiplication_example():
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
    plain2 = Plaintext(encoder.encode(2))
    plain3 = Plaintext(encoder.encode(3))
    encrypted2, encrypted3 = Ciphertext(), Ciphertext()
    encryptor.encrypt(plain2, encrypted2)
    encryptor.encrypt(plain3, encrypted3)

    # Homomorphic multiplication
    encrypted_product = Ciphertext()
    evaluator.multiply(encrypted2, encrypted3, encrypted_product)

    # Decrypt the result
    plain_product = Plaintext()
    decryptor.decrypt(encrypted_product, plain_product)
    product = encoder.decode_int32(plain_product)

    print(f"Product: {product}")

homomorphic_multiplication_example()