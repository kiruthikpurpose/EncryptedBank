from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt data
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Decrypt data
def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")
    
    def encrypt_balance(self, key):
        self.balance = encrypt_data(str(self.balance), key)
    
    def decrypt_balance(self, key):
        self.balance = decrypt_data(self.balance, key)

# Example usage:
if __name__ == "__main__":
    # Generate encryption key
    key = generate_key()
    
    # Create a bank account
    account = BankAccount("123456789", 1000)
    
    # Encrypt the balance
    account.encrypt_balance(key)
    
    # Display encrypted balance (just for demonstration)
    print(f"Encrypted Balance: {account.balance}")
    
    # Decrypt the balance
    account.decrypt_balance(key)
    
    # Display decrypted balance
    account.display_balance()
