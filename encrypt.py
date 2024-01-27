from cryptography.fernet import Fernet
from utility_functions import UtilityFunctions

class Encrypt(UtilityFunctions):

    @staticmethod
    def encrypt_files(files, key):
        for file in files:
            content = UtilityFunctions.read_file(file)
            encrypted_content = Fernet(key).encrypt(content)
            UtilityFunctions.write_file(file, encrypted_content)