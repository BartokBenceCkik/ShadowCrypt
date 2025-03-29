# 💀ShadowCrypt💀

## 📜 Description
ShadowCrypt is a powerful and easy-to-use encryption tool that helps you protect your sensitive files and directories using **AES-256 encryption**. Whether you need to safeguard personal documents or secure confidential data, CryptShield ensures that your files remain private and tamper-proof.

## 🔑 Features
✅ **AES-256 Encryption** – Industry-standard encryption for maximum security.  
✅ **Interactive CLI** – No need for command-line arguments; just follow the prompts.  
✅ **Encrypt & Decrypt Files or Directories** – Protect multiple files at once with ease.  
✅ **Secure Key Input** – Uses a hashed key for enhanced security.  
✅ **Progress Bar** – Shows real-time encryption/decryption progress.  
✅ **Handles Large Files** – Reads and writes data in chunks to avoid memory issues.  
✅ **Optional Auto-Delete** – Allows users to securely remove original files after encryption.  

## 🚀Step-by-Step Guide in Linux Terminal !

Step 1: Update & upgrade your system  
>sudo apt update  

>sudo apt upgrade  

Step 2: install Dependencies  
>sudo apt install python3-tqdm  

>sudo apt install python3-cryptodome  

Step 3: Clone the repository  
>git clone https://github.com/The-Real-Virus/ShadowCrypt.git  

Step 4: Go to the Tool Directory where u clone it  
>cd ShadowCrypt  

Step 5: After Completing the process now u can run script  
>python3 shadow.py  

## 💡 Tips!
🔹 Use a **strong passphrase** to ensure maximum security. The script hashes your input to generate a secure 32-byte key.  
🔹 Keep a backup of your **encryption key** – Without it, decryption is impossible!  
🔹 Make sure you have the **required dependencies** installed before running the script (see below).  

## 🤝 Follow the Prompts!
1️⃣ Run the script:  

2️⃣ Choose an action:
   ```
   [1] Encrypt a file
   [2] Decrypt a file
   [3] Encrypt a directory
   [4] Decrypt a directory
   ```
3️⃣ Enter the file or directory path.  
4️⃣ Enter a **secure passphrase** (used for encryption & decryption).  
5️⃣ The script will process the files with a **progress bar**.  
6️⃣ You’ll be asked if you want to **delete the original files** after encryption.  

## ⚙️ Troubleshooting
**Q: I forgot my encryption key. Can I recover my files?**  
❌ **No.** The encryption key is never stored. If lost, decryption is impossible.  

**Q: The script is not recognized. What should I do?**  
✅ Make sure Python is installed and run it using `python3 script.py` if necessary.  

**Q: How do I install the required dependencies?**  
✅ Run the following command:  
   ```sh
   install the requirements (step 2 above).
   ```
## 🛠️MODIFICATION 

IF U WANT TO MODIFY OR USE THE SCRIPT IN UR PROJECTs , CONSIDER GIVING CREDITS !  

## 📂 Example Output
	**🔐 Encrypting a file:**
	```
	Choose an action: [1] Encrypt a file, [2] Decrypt a file, [3] Encrypt a directory, [4] Decrypt a directory: 1
	Enter the file or directory path: secret.txt
	Enter a secret key: ********
	🔐 Encrypting file...
	✅ File encrypted: secret.txt.enc
	❗ Do you want to delete original files? (y/n): y
	🗑️ Original files deleted.
	✅ Process complete!
	```

	**🔓 Decrypting a file:**
	```
	Choose an action: [1] Encrypt a file, [2] Decrypt a file, [3] Encrypt a directory, [4] Decrypt a directory: 2
	Enter the file or directory path: secret.txt.enc
	Enter a secret key: ********
	🔓 Decrypting file...
	✅ File decrypted: secret.txt
	```
# ⚠️Disclaimer !
This tool is intended for ethical and educational use only.  
Do not use it for illegal activities. The author is not responsible for any misuse.  
This script is intended for educational purposes and authorized testing only.  
Unauthorized use of this script is illegal and unethical.  
Ensure you have explicit permission before testing any system.  
- Obtain explicit permission before testing any system.  
- Adhere to all applicable laws and regulations.  
- Respect user privacy and data.  
- By using this script, you agree to take full responsibility for your actions.  
