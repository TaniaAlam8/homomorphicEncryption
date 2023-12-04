from cryptography.fernet import Fernet

"""
FUNCTIONS 

generate_key function
1- generate key
2- save generated key to "file_key.text"

Encryption function
3- read key form "file_key.text"
4- use key for the cipher algorithm using Fernet/ ex: cipher=Fernet(key)
5- open the file you want to encypt .Encrypt said file using the cipher algorithm
summary - encrypts file given and produces cipher text file ("encrypted_excel_test_file.xlsx.text")

Decryption function
7- read key from file "file_key_text" 
8- use key with Fernet('key') for the cipher algorithm
9- read encrypted file then decrypted using cipher.dercypt('file')
10- write decrypted data to a file for visualization.

"""


"""Generate file to hold key"""
def generate_key():
    # generate key
    key = Fernet.generate_key()
    print("encripted key : ", key)

    # WRITE key to file to save and use later
    fkey = open("file_key.text", 'wb')
    fkey.write(key)

"""ENCRYPT FILE / Symmtric Encryption"""
def encrypt_file(file,key_file):
    # READ key from "file_key"
    fkey=open(key_file, 'rb') #read byte
    key=fkey.read()

    # symetric encryption
    cipher=Fernet(key)
    # print(key) #TEST

    file_name=file
    with open(file_name,'rb') as f:
        e_file=f.read()

    # encrypt file
    encrypted_file=cipher.encrypt(e_file)

    # save encrypted (write to file )
    with open("encrypted_"+file_name+".text",'wb') as ef:
        ef.write(encrypted_file)

""" Decrypt file /symmetric decryption """
def decrypt_file(file,key_file):
    # open saved key file
    fkey = open(key_file, 'rb')
    key=fkey.read()
    # use fernet scheme
    cipher=Fernet(key)
    # read saved encrypted_data
    with open(file,'rb') as df:
        encrypted_data=df.read()
    # Decrypt the encrypted_data to obtain the original data.
    decrypted_file=cipher.decrypt(encrypted_data)
    # make a new file showing the decrypted file
    with open('decrypted_excel_test_file.xlsx','wb') as df:
        df.write(decrypted_file)


def main():
    print("Main function")
    if (input('generate key ? enter y/n ').lower())=='y':
        generate_key()

    encrypt_file('excel_test_file.xlsx' , 'file_key.text')
    decrypt_file('encrypted_excel_test_file.xlsx.text' , 'file_key.text')


if __name__ == '__main__':
    main()


# would use the library and the functions as below
# from textual_encryption.encryption import generate_file, encrypt_file, decrypt_file

# generate_file()
# encrypt_file('excel_test_file.xlsx')
# decrypt_file('excel_test_file.xlsx')