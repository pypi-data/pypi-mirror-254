#!/usr/bin/env python3

about = """
---------------------------------------------------------------
Author: Fredmark Ivan D. Dizon && John Russel L. Escote
GitHub: https://github.com/veilwr4ith && https://github.com/icode3rror

Project: MIRA(Lite) - GiraSec Solutions's CLI Password Manager
GitHub Repository: https://github.com/GiraSec/MIRA_lite
License: EULA

Version: 2.1.13
Release Date: 2024-02-03

Go Premium for Lifetime Access – No Monthly Expenses!
Unlock a world of possibilities with our Premium membership:
- Debit/Credit Card PINs are supported
- API Keys are supported
- SSH(RSA) Keys are supported
- No storage limit for Passwords/PINs/SSH(RSA) Keys/API Keys
- 2-Factor Authentication
- User can change the Master Password anytime
- Password Generator
- Password Strength Checker
- Password/PIN Expiry Checker
- Password/PIN Expiry Alerts
- Account Lockout
- Mnemonic Option for encryption key
- Reset Option
Upgrade today for lifetime access and experience the robustness of GiraSec's MIRA for only $5 (250 PHP)!

For Premium Access, Concerns, and Issues please email us here:
girasesolutions@gmail.com
fredmarkivand@gmail.com
johnrussel205@gmail.com
---------------------------------------------------------------
"""
banner = """
                   ___   ___
    /|    //| |       / /    //   ) )  // | |
   //|   // | |      / /    //___/ /  //__| |
  // |  //  | |     / /    / ___ (   / ___  |
 //  | //   | |    / /    //   | |  //    | |
//   |//    | | __/ /___ //    | | //     | |
                                      Lite
             Girasec Solutions
"""
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from mnemonic import Mnemonic
import base64
import os
import getpass
import argon2
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from secrets import token_bytes
from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import readline
import time
from password_strength import PasswordPolicy
from datetime import datetime, timedelta
from threading import Thread
from termcolor import colored
from functools import wraps
import string
import random
import json
import platform
import sys
import io
import validators
import uuid
import phonenumbers
def clear_terminal():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
def get_os_distribution():
    system_info = platform.system()
    if system_info == 'Linux':
        try:
            with open('/etc/os-release', 'r') as f:
                lines = f.readlines()
                distribution_info = {}
                for line in lines:
                    key, value = line.strip().split('=')
                    distribution_info[key] = value.replace('"', '')
                distribution = distribution_info.get('PRETTY_NAME', 'Unknown Distribution')
                version = distribution_info.get('VERSION_ID', 'Unknown Version')
                codename = distribution_info.get('VERSION_CODENAME', 'Unknown Codename')
                base = distribution_info.get('ID_LIKE', 'Unknown Base')
                return f"Linux Distribution: {distribution}\nVersion: {version}\nCodename: {codename}\nBase: {base}\nArchitecture: {platform.architecture()[0]}"
        except FileNotFoundError:
            return "Unable to determine distribution. /etc/os-release file not found."
    elif system_info == 'Darwin':
        version, _, _ = platform.mac_ver()
        return f"macOS Version: {version}\nArchitecture: {platform.architecture()[0]}"
    elif system_info == 'Windows':
        version = platform.version()
        return f"Windows Version: {version}\nArchitecture: {platform.architecture()[0]}"
    else:
        return f"Operating System: {system_info}"
def get_python_version():
    return f"Python Version: {platform.python_version()}"
def check_linux_privileges():
    if 'SUDO_UID' in os.environ.keys() or os.getenv('USER') == 'root':
        return True
    return False
def is_admin():
    if platform.system() == 'Windows':
        try:
            from ctypes import windll
            return windll.shell32.IsUserAnAdmin()
        except Exception:
            return colored("[-] Mira requires elevated privileges on Windows. QUITTING!", "red")
    else:
        return False
def check_windows_privileges():
    return is_admin()
def get_current_datetime():
    current_datetime = datetime.now()
    date_str = current_datetime.strftime("%Y-%m-%d")
    time_str = current_datetime.strftime("%H:%M:%S")
    return f"Current Time: {time_str}\nDate: {date_str}"
class PasswordManager:
    if os.name == "posix":
        USER_DATA_FILE = os.environ.get('USER_DATA_FILE', '/etc/.freeuser')
        PASSFILE = os.environ.get('PASSFILE', '/etc/.freepass')
    elif os.name == "nt":
        program_files_dir = os.environ.get('ProgramFiles', 'C:\\Program Files')
        app_folder_name = 'liteMira'
        app_folder_path = os.path.join(program_files_dir, app_folder_name)
        os.makedirs(app_folder_path, exist_ok=True)
        USER_DATA_FILE = os.path.join(app_folder_path, 'free_user_data')
        PASSFILE = os.path.join(app_folder_path, 'freepass')
    def __init__(self):
        self.history = InMemoryHistory()
        self.session = PromptSession(history=self.history, auto_suggest=AutoSuggestFromHistory())
        self.master_password = None
        self.cipher = None
        self.ph = PasswordHasher()
    def load_encryption_key(self, encryption_key):
        self.cipher = self.initialize_cipher(encryption_key)
    def initialize_cipher(self, key):
        return Fernet(key)
    def check_master_password_strength(self, password):
        policy = PasswordPolicy.from_names(
            length=20,
            uppercase=3,
            numbers=3,
            special=4,
        )
        result = policy.test(password)
        if result:
            print(colored("[-] Master password is not strong enough (Not Added). Please follow our password policy for master password:", "red"))
            for violation in result:
                print(colored(f"    {violation}", "red"))
            return False
        return True
    def check_password_strength(self, password):
        policy = PasswordPolicy.from_names(
            length=10,
            uppercase=1,
            numbers=1,
            special=1,
        )
        result = policy.test(password)

        if result:
            print(colored("[-] Password is not strong enough:", "red"))
            for violation in result:
                print(colored(f"    {violation}", "red"))
            user_choice = input(colored("[*] Do you want to use this password anyway? (y/N): ", "yellow"))
            if user_choice.lower() == 'y':
                return True
            else:
                return False
        return True
    def register(self, username, master_password):
        if not self.check_master_password_strength(master_password):
            return
        if os.path.exists(self.USER_DATA_FILE) and os.path.getsize(self.USER_DATA_FILE) != 0:
            print(colored("[-] Master user already exists!!", "red"))
        else:
            self.master_password = master_password
            salt = token_bytes(100)
            salt_hex = salt.hex()
            hashed_master_password = self.ph.hash(master_password + salt_hex)
            encryption_key = Fernet.generate_key()
            ph = argon2.PasswordHasher()
            hashed_encryption_key = ph.hash(encryption_key.decode())
            user_data = {
                'username': username,
                'salt': salt_hex,
                'master_password': hashed_master_password,
                'encryption_key': hashed_encryption_key
            }
            with open(self.USER_DATA_FILE, 'w') as file:
                json.dump(user_data, file)
                clear_terminal()
                print(colored(banner, "blue"))
                print(colored("\n[+] Registration complete!!", "green"))
                print(colored(f"[+] Encryption key: {encryption_key.decode()}", "green"))
                print(colored("\n[*] Caution: Save your encryption key and store it somewhere safe Mira will never recover your encryption key once you forgot it!!! So please don't be stupid:)", "yellow"))
    def login(self, username, entered_password, encryption_key):
        if not os.path.exists(self.USER_DATA_FILE):
            print(colored("\n[-] You have not registered. Do that first!", "red"))
        else:
            with open(self.USER_DATA_FILE, 'r') as file:
                user_data = json.load(file)
            try:
                self.ph.verify(user_data['master_password'], entered_password + user_data['salt'])
            except VerifyMismatchError:
                print(colored("[-] Invalid Login credentials. Login failed!", "red"))
                if self.increment_failed_attempts():
                    return
                else:
                    return
            if username == user_data['username']:
                stored_encryption_key = user_data['encryption_key']
                ph = argon2.PasswordHasher()
                try:
                    ph.verify(stored_encryption_key, encryption_key)
                except argon2.exceptions.VerifyMismatchError:
                    print(colored("[-] Invalid encryption key. Login failed!", "red"))
                    if self.increment_failed_attempts():
                        return
                    else:
                        return
                self.load_encryption_key(encryption_key.encode())
                if '2fa_enabled' in user_data and user_data['2fa_enabled']:
                    key = self.decrypt_information(user_data['key'])
                    code = getpass.getpass(colored("[*] 6-Digit Code (2FA): ", "yellow"))
                    if not self.verify_2fa(key, code):
                        print(colored("[-] Invalid 2FA code. Login failed!", "red"))
                        if self.increment_failed_attempts():
                            return
                        else:
                            return
                print(colored("[+] Login Successful..", "green"))
                time.sleep(3)
                clear_terminal()
                print(colored(banner, "blue"))
                self.master_password = entered_password
                self.main_menu()
            else:
                print(colored("[-] Invalid Login credentials. Login failed!", "red"))
                if self.increment_failed_attempts():
                    clear_terminal()
                    return
                else:
                    return
    def show_expiry_status(self):
        try:
            with open(self.PASSFILE, 'r') as file:
                data = json.load(file)
            usernames = []
            for entry in data:
                username = self.decrypt_information(entry['username'])
                usernames.append({
                    'account_id': entry['account_id'],
                    'website': entry['website'],
                    'username': username
                })
            if usernames:
                print(colored("[+] All Available Platforms:", "green"))
                print(colored("\nAccount ID".ljust(20) + "Platform".ljust(31) + "Username".ljust(30), "cyan"))
                print(colored("----------".ljust(19) + "--------------------".ljust(31) + "--------------------".ljust(30), "cyan"))
                for user_info in usernames:
                    print(f"{colored(str(user_info['account_id']).ljust(19), 'cyan')}{colored(str(user_info['website']).ljust(31), 'cyan')}{colored(str(user_info['username']).ljust(30), 'cyan')}")
            else:
                print(colored("[-] No passwords saved. Show expiry status failed!", "red"))
        except FileNotFoundError:
            print(colored("[-] No passwords saved. Show expiry status failed!", "red"))
    def main_menu(self):
        with open(self.USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        prompt = True
        while prompt:
            prompt = HTML(f"<ansiblue>{user_data.get('username')}@MIRA ~> </ansiblue>")
            choice = self.session.prompt(prompt)
            if choice == "":
                continue
            elif choice == 'add_platform_passwd':
                website = input(colored("[*] Platform: ", "yellow"))
                if not validators.url(website):
                    print(colored("[-] The Platform you've entered is Invalid! Please make sure that it's in URL form.", "red"))
                    continue
                email_or_phone = input(colored("[*] Email Address/Phone(CC): ", "yellow"))
                if not (validators.email(email_or_phone) or self.validate_phone_number(email_or_phone)):
                    print(colored("[-] The Email/Phone you've entered is Invalid!", "red"))
                    continue
                username = input(colored("[*] Username: ", "yellow"))
                password = getpass.getpass(colored("[*] Password: ", "yellow"))
                re_enter = getpass.getpass(colored("[*] Re-Enter Password: ", "yellow"))                             
                if re_enter != password:
                    print(colored("[-] Password did not match! QUITTING!", "red"))
                else:
                    self.add_password(website, email_or_phone, username, password)
            elif choice == 'get_platform_passwd':
                try:
                    acc_id = int(input(colored("[*] Account ID: ", "yellow")))
                except ValueError:
                    print(colored("[-] Invalid account ID.", "red"))
                    continue
                decrypted_password = self.get_password(acc_id)
                try:
                    with open(self.PASSFILE, 'r') as file:
                        data = json.load(file)
                    if acc_id not in [entry['account_id'] for entry in data]:
                        print(colored(f"[-] This ID {acc_id} doesn't exist", "red"))
                    for entry in data:
                        if entry['account_id'] == acc_id and 'expiry_at' in entry and entry['expiry_at']:
                            expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S")
                            if datetime.now() > expiry_date:
                                response = input(colored("[*] Password has expired. Do you want to update the password or delete the account for this platform? (U/D): ", "yellow")).lower()
                                if response == 'u':
                                    new_password = getpass.getpass(colored("[*] New Password: ", "yellow"))
                                    re_enter = getpass.getpass(colored("[*] Re-Enter New Password: ", "yellow"))
                                    if any(self.decrypt_password(entry['password']) == new_password for entry in data):
                                        print(colored("[-] Password has been used, avoid reusing passwords. QUITTING!!", "red"))
                                        continue
                                    if re_enter != new_password:
                                        print(colored("[-] Password did not match! QUITTING!", "red"))
                                        continue
                                    if self.check_password_reuse(new_password, data):
                                        print(colored("[-] Password has been used on other platforms. Avoid using the same password on other platforms!!", "red"))
                                        continue
                                    if not self.check_password_strength(new_password):                                                      
                                        continue
                                    entry['password'] = self.encrypt_password(new_password)
                                    entry['expiry_at'] = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
                                    with open(self.PASSFILE, 'w') as file:
                                        json.dump(data, file, indent=4)
                                    decrypted_password = self.decrypt_password(entry['password'])
                                    if decrypted_password:
                                        print(colored(f"[+] Password updated successfully.", "green"))
                                        continue
                                    else:
                                        print(colored("[-] Password has expired. Please update your password.", "red"))
                                    continue
                                elif response == 'd':
                                    caution = input(colored("[*] Caution: Once you remove it, it will be permanently deleted from your system. Are you sure you want to proceed? (y/N): ", "yellow"))
                                    if caution == 'n':
                                        print(colored("[-] Abort.", "red"))
                                        continue
                                    elif caution == 'y':
                                        data = [e for e in data if not (e['account_id'] == acc_id)]
                                        with open(self.PASSFILE, 'w') as file:
                                            json.dump(data, file, indent=4)
                                        print(colored("[-] Website permanently deleted.", "red"))                                        
                                        continue
                            else:
                                if decrypted_password is not None:
                                    print(colored(f"[+] Platform: {entry.get('website')}\n[+] Email/Phone: {self.decrypt_information(entry['email_address/phone'])}\n[+] Username: {self.decrypt_information(entry['username'])}\n[+] Key Content: {decrypted_password}", "green"))
                                else:
                                    print(colored("[-] Password not found! Did you save the password?", "red"))
                except FileNotFoundError:
                    print(colored("[-] No passwords have been saved yet. Retrieve passwords failed!", "red"))
            elif choice == 'del_platform_passwd':
                self.delete_password()
            elif choice == 'ch_platform_passwd':
                try:
                    acc_id = int(input(colored("[*] Account ID: ", "yellow")))
                except ValueError:
                    print(colored("[-] Invalid Account ID", "red"))
                    continue
                self.change_password(acc_id)
            elif choice == 'list_platform_passwd':
                self.show_expiry_status()
            elif choice == 'lout':
                self.logout()
                break
            elif choice == 'exit':
                print(colored("[*] MIRA Terminated!", "red"))
                sys.exit()
            elif choice == 'clear':
                clear_terminal()
            elif choice == 'about':
                clear_terminal()
                print(colored(banner, "blue"))
                print(colored(about, "cyan"))
            elif choice == 'h' or choice == 'help':
                print(colored("""[**] Available Commands:
- 'add_platform_passwd' - Add a new password for the desired account ID
- 'get_platform_passwd' - Display the plaintext version of the password for the desired account ID
- 'del_platform_passwd' - Delete a saved password according to your desired account ID
- 'ch_platform_passwd' - Change the password for the desired account ID
- 'list_passwd' - List all the stored passwords on your vault with their ID
- 'lout' - Log out to MIRA and go back to login prompt
- 'exit' - Terminate MIRA

FOR MORE ADVANCED AND ADDITIONAL FEATURES, UPGRADE TO PREMIUM!! Type 'about' for the features of MIRA Premium!!
""", "cyan"))
            else:
                print(colored("[-] Invalid Option!", "red"))
    def check_username_reuse(self, new_website, new_username, existing_data):
        for entry in existing_data:
            existing_website = entry['website']
            existing_username = self.decrypt_information(entry['username'])
            if existing_website == new_website and existing_username == new_username:
                return True
            return False
    def check_email_reuse(self, new_email, existing_data):
        for entry in existing_data:
            decrypted_email = self.decrypt_information(entry['email_address'])
            if decrypted_email == new_email:
                user_input = input(colored(f"[*] The email '{new_email}' already exists. Do you want to proceed? (y/N): ", "yellow"))
                if user_input.lower() == 'y':
                    return True
                else:
                    return False
                return False
    def check_password_reuse(self, new_password, existing_data):
        for entry in existing_data:
            decrypted_password = self.decrypt_password(entry['password'])
            if decrypted_password == new_password:
                return True
        return False
    def validate_phone_number(self, phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number)
            return phonenumbers.is_valid_number(parsed_number)
        except phonenumbers.phonenumberutil.NumberParseException:
            return False
    def add_password(self, website, email_address, username, password):
        if not os.path.exists(self.PASSFILE):
            data = []
        else:
            try:
                with open(self.PASSFILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            except FileNotFoundError:
                pass
        if len(data) >= 5:
            print(colored("[-] Maximum number of accounts reached! Cannot add more accounts. Upgrade to premium for unlimited storing of accounts.", "red"))
            return
        for entry in data:
            decrypted_email = self.decrypt_information(entry['email_address/phone'])
            if decrypted_email == email_address:
                user_input = input(colored(f"[*] The email/phone {email_address} already exists. Do you want to proceed? (y/N): ", "yellow")).lower()
                if user_input == 'y':
                    print(colored("[**] It's advisable not to use the same email/phone for another account.", "cyan"))
                    pass
                else:
                    return
        if self.check_username_reuse(website, username, data):
            print(colored(f"[-] The username {username} already exists for this platform!", "red"))              
            return
        if self.check_password_reuse(password, data):
            print(colored("[-] Password has been used to other platforms. (Password not added) Avoid using the same password on other platforms!!", "red"))
            return
        salt = token_bytes(16)
        if self.check_password_strength(password):
            unique_id = int(uuid.uuid4().hex[:4],  16)
            encrypted_password = self.encrypt_password(password)
            encrypted_email = self.encrypt_information(email_address)
            encrypted_username = self.encrypt_information(username)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            password_entry = {
                'account_id': unique_id,
                'website': website,
                'email_address/phone': encrypted_email,
                'username': encrypted_username,
                'password': encrypted_password,
                'added_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'expiry_at': (datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S') + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
            }
            data.append(password_entry)
            with open(self.PASSFILE, 'w') as file:
                json.dump(data, file, indent=4)
                print(colored(f"[+] Password added! Account ID for this account: {unique_id}", "green"))
        else:
            print(colored("[-] Password not added. Please choose a stronger password.", "red"))
    def get_password(self, i_d):
        if not os.path.exists(self.PASSFILE):
            return None
        try:
            with open(self.PASSFILE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
        for entry in data:
            if entry['account_id'] == i_d and entry.get('email_address/phone') and entry.get('username'):
                website = entry.get('website')
                decrypted_email = self.decrypt_information(entry['email_address/phone'])
                decrypted_username = self.decrypt_information(entry['username'])
                if 'expiry_at' in entry and entry['expiry_at']:
                    expiry_date = datetime.strptime(entry['expiry_at'], "%Y-%m-%d %H:%M:%S")
                    if datetime.now() > expiry_date:
                        return None
                decrypted_password = self.decrypt_password(entry['password'])
                return decrypted_password
        return None
    def delete_password(self):
        try:
            acc_id = int(input(colored("[*] Account ID: ", "yellow")))
        except ValueError:
            print(colored("[-] Invalid Account ID", "red"))
            return
        master_pass = getpass.getpass(colored("[*] Master Password: ", "yellow"))
        if not os.path.exists(self.PASSFILE):
            print(colored("[-] No passwords saved. Deletion failed!", "red"))
            return
        with open(self.USER_DATA_FILE, 'r') as file:
            user_data = json.load(file)
        stored_master_password = user_data['master_password']
        salt = user_data['salt']
        try:
            self.ph.verify(stored_master_password, master_pass + salt)
        except VerifyMismatchError:
            print(colored("[-] Incorrect current master password. Delete password failed!", "red"))
            return
        try:
            with open(self.PASSFILE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
        deleted_entry = next((entry for entry in data if entry['account_id'] == acc_id and entry.get('email_address/phone') and entry.get('username')), None)
        if deleted_entry:
            data.remove(deleted_entry)
            with open(self.PASSFILE, 'w') as file:
                json.dump(data, file, indent=4)
            print(colored("[+] Password deleted successfully!", "green"))
            if not data:
                os.remove(self.PASSFILE)
                return
        else:
            print(colored("[-] Password not found! Deletion failed!", "red"))
    def change_password(self, acc_id):
        data = []
        if not os.path.exists(self.PASSFILE):
            print(colored("[-] No passwords saved!", "red"))
            return
        try:
            with open(self.PASSFILE, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            pass
        for entry in data:
            current_password = getpass.getpass(colored(f"[*] Current password for the given account ID (Usn: {self.decrypt_information(entry.get('username'))}): ", "yellow"))
        decrypted_password = self.get_password(acc_id)
        if decrypted_password is not None and current_password == decrypted_password:
            new_password = getpass.getpass(colored("[*] New Password: ", "yellow"))
            re_enter = getpass.getpass(colored("[*] Re-Enter New Password: ", "yellow"))
            if not self.check_password_strength(new_password):
                return
            if new_password != re_enter:
                print(colored("[-] New Passwords Did Not Match! Change password failed!", "red"))
                return
            encrypted_new_password = self.encrypt_password(new_password)
            if any(self.decrypt_password(entry['password']) == new_password for entry in data):
                print(colored("[-] Password has been used. (Change password failed) Avoid reusing passwords!", "red"))
                return
            try:
                with open(self.PASSFILE, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
            for entry in data:
                if entry['account_id'] == acc_id:
                    entry['password'] = encrypted_new_password
                    entry['expiry_at'] = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
                    with open(self.PASSFILE, 'w') as file:
                        json.dump(data, file, indent=4)
                    decrypted_password = self.decrypt_password(entry['password'])
                    if decrypted_password:
                        print(colored("[+] Password updated successfully!", "green"))
                    else:
                        print(colored("[-] Password update failed.", "red"))
                    return
        elif acc_id not in [entry['account_id'] for entry in data]:
            print(colored("[-] This account ID is not available in your vault.", "red"))
        else:
            print(colored("[-] Incorrect current password. Change password failed!", "red"))
    def encrypt_password(self, password):
        return self.cipher.encrypt(password.encode()).decode()
    def decrypt_password(self, encrypted_password):
        return self.cipher.decrypt(encrypted_password.encode()).decode()
    def encrypt_information(self, information):
        return self.cipher.encrypt(information.encode()).decode()
    def decrypt_information(self, encrypted_information):
        return self.cipher.decrypt(encrypted_information.encode()).decode()
    def logout(self):
        self.master_password = None
        self.cipher = None
        print(colored("[+] Logged out!", "cyan"))

def main():
    if platform.system() == 'Linux':
        if not check_linux_privileges():
            print(colored("[-] Mira requires elevated privileges on Linux. QUITTING!", "red"))
            exit()
        else:
            try:
                clear_terminal()
                current_datetime_info = get_current_datetime()
                os_distribution_info = get_os_distribution()
                print(colored(os_distribution_info, "blue"))
                time.sleep(2)
                print(colored(get_python_version(), "blue"))
                time.sleep(2)
                print(colored(current_datetime_info, "blue"))
                time.sleep(2)
                print(colored("[+] Starting Mira Password Manager.....", "blue"))
                password_manager = PasswordManager()
                time.sleep(20)
                clear_terminal()
                print(colored(banner, "blue"))
                while True:
                    prompt = HTML("<ansiblue>MIRA ~> </ansiblue>")
                    choice = password_manager.session.prompt(prompt)
                    if choice == "":
                        continue
                    elif choice == 'regis':
                        if os.path.exists(password_manager.USER_DATA_FILE) and os.path.getsize(password_manager.USER_DATA_FILE) != 0:
                            print(colored("[-] Master user already exists!!", "red"))
                        else:
                            username = input(colored("[*] New Username: ", "yellow"))
                            registration_successful = False
                            registration_failed = False
                            while not registration_successful and not registration_failed:
                                master_password = getpass.getpass(colored("[*] New Master Password: ", "yellow"))                                                                                                                                                               
                                re_enter = getpass.getpass(colored("[*] Re-Enter Master Password: ", "yellow"))
                                if re_enter != master_password:
                                    print(colored("[-] Master Password Did Not Match! Please try again!", "red"))
                                    continue
                                else:
                                    show_password_option = input(colored("[*] Do you want to show the master password? (y/N): ", "yellow"))
                                    if show_password_option.lower() == 'y':
                                        print(colored(f"[**] Master Password: {master_password}", "magenta"))
                                        confirm_password_option = input(colored("[*] Is the shown master password correct? (y/N): ", "yellow"))
                                        if confirm_password_option.lower() == 'n':
                                            print(colored("[**] Please enter a new master password.", "magenta"))
                                            continue
                                        elif confirm_password_option.lower() == 'y':
                                            password_manager.register(username, master_password)
                                            registration_successful = True
                                        else:
                                            print(colored("[-] Invalid Option!", "red"))
                                            registration_failed = True
                                    elif show_password_option.lower() == 'n':
                                        password_manager.register(username, master_password)
                                        registration_successful = True
                                    else:
                                        print(colored("[-] Invalid Option!", "red"))
                                        registration_failed = True
                    elif choice == 'log':
                        if os.path.exists(password_manager.USER_DATA_FILE):
                            username = input(colored("[*] Username: ", "yellow"))
                            master_password = getpass.getpass(colored("[*] Master password: ", "yellow"))
                            encryption_key = getpass.getpass(colored("[*] Encryption key: ", "yellow"))
                            password_manager.login(username, master_password, encryption_key)
                        else:
                            print(colored("[-] You have not registered. Please do that.", "red"))
                    elif choice == 'help' or choice == 'h':
                        print(colored(""""[**] Available Commands:
'log' - Login (Make sure you're registered before attempt to login)
'regis' - Register for new user (Only one user!)
'quit' - Terminate MIRA
'about' - More information about MIRA
'h' - Help""", "cyan"))
                    elif choice == 'quit':
                        print(colored("\n[-] Exiting Mira.....", "red"))
                        time.sleep(3)
                        clear_terminal()
                        print(colored(banner, "cyan"))
                        sys.exit()
                    elif choice == 'about':
                        clear_terminal()
                        print(colored(banner, "cyan"))
                        print(colored(about, "cyan"))
                    elif choice == 'clear':
                        clear_terminal()
                    else:
                        print(colored("[-] Invalid Option", "red"))
            except (KeyboardInterrupt, EOFError):
                print(colored("[-] Exiting Mira.....", "red"))
                time.sleep(3)
                clear_terminal()
                print(colored(banner, "cyan"))
                sys.exit()
    elif platform.system() == 'Windows':
        if not check_windows_privileges():
            print(colored("[-] Mira requires elevated privileges on Windows. QUITTING!", "red"))
            exit()
        else:
            try:
                clear_terminal()
                current_datetime_info = get_current_datetime()
                os_distribution_info = get_os_distribution()
                print(colored(os_distribution_info, "blue"))
                time.sleep(2)
                print(colored(get_python_version(), "blue"))
                time.sleep(2)
                print(colored(current_datetime_info, "blue"))
                time.sleep(2)
                print(colored("[+] Starting Mira Password Manager.....", "blue"))
                password_manager = PasswordManager()
                time.sleep(20)
                clear_terminal()
                print(colored(banner, "blue"))
                while True:
                    prompt = HTML("<ansiblue>MIRA ~> </ansiblue>")
                    choice = password_manager.session.prompt(prompt)
                    if choice == "":
                        continue
                    elif choice == 'regis':
                        if os.path.exists(password_manager.USER_DATA_FILE) and os.path.getsize(password_manager.USER_DATA_FILE) != 0:
                            print(colored("[-] Master user already exists!!", "red"))
                        else:
                            username = input(colored("[*] New Username: ", "yellow"))
                            registration_successful = False
                            registration_failed = False
                            while not registration_successful and not registration_failed:
                                master_password = getpass.getpass(colored("[*] New Master Password: ", "yellow"))
                                re_enter = getpass.getpass(colored("[*] Re-Enter Master Password: ", "yellow"))
                                if re_enter != master_password:
                                    print(colored("[-] Master Password Did Not Match! Please try again!", "red"))
                                    continue
                                else:
                                    show_password_option = input(colored("[*] Do you want to show the master password? (y/N): ", "yellow"))
                                    if show_password_option.lower() == 'y':
                                        print(colored(f"[**] Master Password: {master_password}", "magenta"))
                                        confirm_password_option = input(colored("[*] Is the shown master password correct? (y/N): ", "yellow"))
                                        if confirm_password_option.lower() == 'n':
                                            print(colored("[**] Please enter a new master password.", "magenta"))
                                            continue
                                        elif confirm_password_option.lower() == 'y':
                                            password_manager.register(username, master_password)                                                                                                                                                                                
                                            registration_successful = True
                                        else:
                                            print(colored("[-] Invalid Option!", "red"))
                                            registration_failed = True
                                    elif show_password_option.lower() == 'n':
                                        password_manager.register(username, master_password)
                                        registration_successful = True
                                    else:
                                        print(colored("[-] Invalid Option!", "red"))
                                        registration_failed = True
                    elif choice == 'log':
                        if os.path.exists(password_manager.USER_DATA_FILE):
                            username = input(colored("[*] Username: ", "yellow"))
                            master_password = getpass.getpass(colored("[*] Master password: ", "yellow"))
                            encryption_key = getpass.getpass(colored("[*] Encryption key: ", "yellow"))
                            password_manager.login(username, master_password, encryption_key)
                        else:
                            print(colored("[-] You have not registered. Please do that.", "red"))
                    elif choice == 'help' or choice == 'h':
                        print(colored(""""[**] Available Commands:
'log' - Login (Make sure you're registered before attempt to login)
'regis' - Register for new user (Only one user!)
'about' - More information about MIRA
'quit' - Terminate MIRA
'h' - Help""", "cyan"))
                    elif choice == 'quit':
                        print(colored("[-] Exiting Mira.....", "red"))
                        time.sleep(3)
                        clear_terminal()
                        print(colored(banner, "cyan"))
                        sys.exit()
                    elif choice == 'about':
                        clear_terminal()
                        print(colored(banner, "blue"))
                        print(colored(about, "cyan"))
                    else:
                        print(colored("[-] Invalid Option", "red"))
            except (KeyboardInterrupt, EOFError):
                print(colored("[-] Exiting Mira.....", "red"))
                time.sleep(3)
                clear_terminal()
                print(colored(banner, "cyan"))
                sys.exit()

if __name__ == '__main__':
    main()


