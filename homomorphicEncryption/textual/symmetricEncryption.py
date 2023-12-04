from cryptography.fernet import Fernet

def generate_file():
   # generate key
   key = Fernet.generate_key()
   print("encrypted key : ", key)

   # WRITE key to file to save and use later
   fkey = open("file_key.text", 'wb')
   fkey.write(key)

def encrypt_file(file):
   # READ key from "file_key"
   fkey=open("file_key.text", 'rb') #read byte
   key=fkey.read()

   # symmetric encryption
   cipher=Fernet(key)

   file_name=file
   with open(file_name,'rb') as f:
       e_file=f.read()

   # encrypt file
   encrypted_file=cipher.encrypt(e_file)

   # save encrypted (write to file )
   with open("encrypted_"+file_name+".text",'wb') as ef:
       ef.write(encrypted_file)

def decrypt_file(file):
   fkey = open("file_key.text", 'rb')
   key=fkey.read()
   # use fernet scheme
   cipher=Fernet(key)
   # read saved encrypted_data
   with open('encrypted_'+file+'.text','rb') as df:
       encrypted_data=df.read()
   # Decrypt the encrypted_data to obtain the original data.
   decrypted_file=cipher.decrypt(encrypted_data)
   # make a new file showing the decrypted file
   with open('decrypted_'+file,'wb') as df:
       df.write(decrypted_file)


# would use the library and the functions as below
# from textual_encryption.encryption import generate_file, encrypt_file, decrypt_file

# generate_file()
# encrypt_file('excel_test_file.xlsx')
# decrypt_file('excel_test_file.xlsx')