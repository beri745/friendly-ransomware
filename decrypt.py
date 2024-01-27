from cryptography.fernet import Fernet
from utility_functions import UtilityFunctions


class Decrypt(UtilityFunctions):
    
    @staticmethod
    def decrypt_files(files, key):
        for file in files:
           encrypted_content = UtilityFunctions.read_file(file)
           decrypted_content = Fernet(key).decrypt(encrypted_content)
           UtilityFunctions.write_file(file, decrypted_content)
    