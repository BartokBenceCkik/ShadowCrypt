import os
import sys
import hashlib
from tqdm import tqdm
from Cryptodome.Cipher import AES
from Cryptodome import Random

# Function to display banner
def show_banner():
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  ShadowCrypt
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

# Show banner at script startup
show_banner()

# Ask user for input
choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()

if choice == 'n':
    print("\nExiting the script. Goodbye!")
    exit()
elif choice == 'y':
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen on Linux/Mac ('clear') or Windows ('cls')
else:
    print("\nInvalid choice. Exiting the script.")
    exit()

def logo():
    logo = r"""
███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ 
                                                                                                                       
"""
    print(logo)

# Define chunk size for large file processing
CHUNK_SIZE = 64 * 1024  # 64KB

def get_secure_key():
    """Prompt user for a password and derive a secure 32-byte AES key."""
    password = input("Enter a secret key (it will be hashed for security): ")
    key = hashlib.sha256(password.encode()).digest()  # Generates a 32-byte key
    return key

def pad(data):
    """Pads data to be a multiple of AES block size (16 bytes)."""
    padding_length = AES.block_size - (len(data) % AES.block_size)
    return data + (b'\0' * padding_length)  # Using null bytes for padding

def unpad(data):
    """Removes padding from decrypted data."""
    return data.rstrip(b'\0')

def encrypt_file(file_path, key):
    """Encrypts a file using AES and saves it with a .enc extension."""
    iv = Random.new().read(AES.block_size)  # Generate a random IV
    cipher = AES.new(key, AES.MODE_CBC, iv)  # AES in CBC mode

    output_file = file_path + ".enc"
    
    with open(file_path, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.write(iv)  # Store IV at the beginning
        while chunk := f_in.read(CHUNK_SIZE):
            if len(chunk) % AES.block_size != 0:
                chunk = pad(chunk)  # Ensure data is AES block size
            f_out.write(cipher.encrypt(chunk))  # Encrypt and write

    return output_file

def decrypt_file(file_path, key):
    """Decrypts a file and restores its original content."""
    output_file = file_path.replace(".enc", "")

    with open(file_path, 'rb') as f_in:
        iv = f_in.read(AES.block_size)  # Read the IV
        cipher = AES.new(key, AES.MODE_CBC, iv)

        with open(output_file, 'wb') as f_out:
            while chunk := f_in.read(CHUNK_SIZE):
                decrypted_chunk = cipher.decrypt(chunk)
                f_out.write(decrypted_chunk)

    # Remove padding
    with open(output_file, 'rb') as f:
        data = unpad(f.read())

    with open(output_file, 'wb') as f:
        f.write(data)  # Save the unpadded content

    return output_file

def process_directory(directory, key, encrypt=True):
    """Encrypts or decrypts all files in a directory with a progress bar."""
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    action = "Encrypting" if encrypt else "Decrypting"
    for file in tqdm(files, desc=f"{action} files", unit="file"):
        if encrypt:
            encrypt_file(file, key)
        else:
            if file.endswith(".enc"):
                decrypt_file(file, key)

def main():
    print("🔒 Welcome to AES File Encryptor & Decryptor")
    
    # Ask user what they want to do
    while True:
        choice = input("\nChoose an action: [1] Encrypt a file, [2] Decrypt a file, [3] Encrypt a directory, [4] Decrypt a directory: ")
        if choice in ['1', '2', '3', '4']:
            break
        print("❌ Invalid choice. Please enter a number from 1 to 4.")

    # Get path from user
    path = input("\nEnter the file or directory path: ")
    if not os.path.exists(path):
        print("❌ Error: Path does not exist.")
        sys.exit(1)

    # Get encryption key from user
    key = get_secure_key()

    # Process based on user's choice
    if choice == '1':
        print("\n🔐 Encrypting file...")
        encrypted_file = encrypt_file(path, key)
        print(f"✅ File encrypted: {encrypted_file}")
    elif choice == '2':
        print("\n🔓 Decrypting file...")
        decrypted_file = decrypt_file(path, key)
        print(f"✅ File decrypted: {decrypted_file}")
    elif choice == '3':
        print("\n🔐 Encrypting all files in directory...")
        process_directory(path, key, encrypt=True)
        print("✅ Directory encryption complete!")
    elif choice == '4':
        print("\n🔓 Decrypting all files in directory...")
        process_directory(path, key, encrypt=False)
        print("✅ Directory decryption complete!")

    # Ask if user wants to delete original files
    if input("\n❗ Do you want to delete original files? (y/n): ").lower() == 'y':
        if os.path.isdir(path):
            for file in os.listdir(path):
                full_path = os.path.join(path, file)
                if os.path.isfile(full_path):
                    os.remove(full_path)
        else:
            os.remove(path)
        print("🗑️ Original files deleted.")

    print("\n✅ Process complete!")

if __name__ == "__main__":
    logo()
    main()
