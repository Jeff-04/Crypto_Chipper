# pip install secure-smtplib
import smtplib
import smtplib
from email.message import EmailMessage

import string
import random
import sqlite3
import os
import time

import streamlit as st

# Function
def sender_email(type, email, password, to, subject, text, key):
    # Variables containing your email address and password
    EMAIL_ADDRESS = str(email)
    EMAIL_PASSWORD = str(password)

    # Create an instance of the EmailMessage class
    msg = EmailMessage()
    # Define the 'Subject' of the email
    msg['Subject'] = str(subject)
    # Define 'From' (your email address)
    msg['From'] = EMAIL_ADDRESS
    # Define 'To' (to whom is it addressed)
    msg['To'] = str(to)
    # The email content (your message)
    if key != '':
        content_text = str(f"===== {str(type)} Encryption Email =====\n")+ str(text) + str(f'\n Encryption Number : {key}') + str("\n===== Go To : https://streamlit/test")
    else:
        content_text = str(f"===== {str(type)} Encryption Email =====\n")+ str(text) + str("\n===== Go To : https://streamlit/test")

    msg.set_content(str(content_text))
    files = os.listdir('File/')
    if len(files) > 0:
        files = files[1]
        with open('File/' + str(files), 'rb') as attach:
            msg.add_attachment(attach.read(), maintype='application', subtype='octet-stream', filename=attach.name)

    # Establishing a secure connection (SSL), login to your email account and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
        smtp.send_message(msg)

    files = os.listdir('File/')
    if len(files) > 0:    
        path_file = os.path.join(os.getcwd(), 'File')
        files = os.listdir(path_file)[1]
        os.remove(os.path.join(path_file, files))
def caesar_encrypt(message):
    key = 3
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    beta = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for letter in message:
        if letter.isupper() == True:
            if letter in alpha: #if the letter is actually a letter
                #find the corresponding ciphertext letter in the alphabet
                letter_index = (alpha.find(letter) + key) % len(alpha)

                result = result + alpha[letter_index]
            else:
                result = result + letter
            
        else:
            if letter in beta: #if the letter is actually a letter
                #find the corresponding ciphertext letter in the alphabet
                letter_index = (beta.find(letter) + key) % len(beta)

                result = result + beta[letter_index]
            else:
                result = result + letter
        
    # return result
    # Generate Random Number and Symbol
    data_encrypt = list(result)
    data_final = []
    data_random = string.ascii_letters + string.printable
    data = int(len(data_encrypt)) + 10
    for i in range(data):
        random_choice = random.choice(data_random)
        data_final.append(random_choice)

    print(data_encrypt)
    print(data_final)

    data_index = 0
    for index, data in enumerate(data_final):
        get_data = str(random.choice(data_random))
        if str(data).isalpha():
            if int(data_index) < int(len(data_encrypt)):
                data_final[index] = data_encrypt[data_index]
                data_index += 1
            
            else:
                while get_data.isalpha() == True:
                    get_data = str(random.choice(data_random))

                data_final[index] = str(get_data)

        else:
            continue
    
    result = " ".join(i for i in data_final)
    return result

def caesar_decrypt(message):
    # Remove non alphabetic
    key = 3
    data = []

    for i in message:
        if str(i).isalpha() == True or str(i) == " ":
            data.append(str(i))
    
    data_final = " ".join(i for i in data)
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    beta = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for letter in data_final:
        if letter.isupper() == True:
            if letter in alpha: #if the letter is actually a letter
                #find the corresponding ciphertext letter in the alphabet
                letter_index = (alpha.find(letter) - key) % len(alpha)

                result = result + alpha[letter_index]
            else:
                result = result + letter
        
        else:
            if letter in beta: #if the letter is actually a letter
                #find the corresponding ciphertext letter in the alphabet
                letter_index = (beta.find(letter) - key) % len(beta)

                result = result + beta[letter_index]
            else:
                result = result + letter

    return result

def viginere_encrypt(plaintext, key):
    try:
        plain_new = plaintext.upper()
        key = key.upper()
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plain_new]
        ciphertext = []
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            if str(plain_new[i]) == " ":
                ciphertext.append(" ")
            else:
                ciphertext.append(chr(value + 65))
        for i in range(len(plaintext)):
            if str(plaintext[i]).islower() == True:
                ciphertext[i] = str(ciphertext[i]).lower()
        # Generate Random Number and Symbol
        result = "".join(i for i in ciphertext)

        data_encrypt = list(result)
        data_final = []
        data_random = string.ascii_letters + string.printable
        data = int(len(data_encrypt)) + 10
        for i in range(data):
            random_choice = random.choice(data_random)
            data_final.append(random_choice)

        data_index = 0
        for index, data in enumerate(data_final):
            get_data = str(random.choice(data_random))
            if str(data).isalpha():
                if int(data_index) < int(len(data_encrypt)):
                    data_final[index] = data_encrypt[data_index]
                    data_index += 1
                
                else:
                    while get_data.isalpha() == True:
                        get_data = str(random.choice(data_random))

                    data_final[index] = str(get_data)

            else:
                continue
        
        result = "".join(i for i in data_final)
        # print(f"Akhir : {result}")
        return result
    
    except Exception as eror:
        print(eror)


def viginere_decrypt(cipher, key):
    try:
        chiper_new = []
        for i in range(len(cipher)):
            if str(cipher[i]).isalpha() == True:
                chiper_new.append(cipher[i])
            elif str(cipher[i]) == " ":
                chiper_new.append(" ")
        
        cipher = "".join(i for i in chiper_new)
        cipher_new = cipher.upper()
        key = key.upper()
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        cipher_int = [ord(i) for i in cipher_new]
        plaintext = []
        for i in range(len(cipher_int)):
            value = (cipher_int[i] - key_as_int[i % key_length]) % 26
            if str(cipher[i]) == " ":
                plaintext.append(" ")
            else:
                plaintext.append(chr(value + 65))
        
        for i in range(len(plaintext)):
            if str(chiper_new[i]).isupper() == False:
                plaintext[i] = str(plaintext[i]).lower()

        plaintext = "".join(i for i in plaintext)
        return plaintext
    
    except Exception as eror:
        print(eror)

def encrypt_combined_chipper(message: str, key: str):
    print("===== Encrypt Combined Chipper =====")
    print("Data Awal : {}".format(message))
    # Encrypt Caesar Chipper
    key_caesar = 3
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    beta = "abcdefghijklmnopqrstuvwxyz"
    result = []

    for letter in message:
        if letter.isupper() == True:
            if letter in alpha: #if the letter is actually a letter
                #find the corresponding ciphertext letter in the alphabet
                letter_index = (alpha.find(letter) + key_caesar) % len(alpha)

                result.append(alpha[letter_index])
            else:
                result.append(letter)
            
        else:
            if letter in beta: #if the letter is actually a letter
                #find the corresponding ciphertext letter in the alphabet
                letter_index = (beta.find(letter) + key_caesar) % len(beta)

                result.append(beta[letter_index])
            else:
                result.append(letter)

    # Caesar Output  
    result_caesar = "".join(i for i in result)
    print("Hasil Caesar : {}".format(result_caesar))


    # Viginere Chippper
    plain_new = result_caesar.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plain_new]
    ciphertext = []
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        if str(plain_new[i]) == " ":
            ciphertext.append(" ")
        else:
            ciphertext.append(chr(value + 65))

    for i in range(len(result_caesar)):
        if str(result_caesar[i]).islower() == True:
            ciphertext[i] = str(ciphertext[i]).lower()

    result_viginere = "".join(i for i in ciphertext)
    print("Hasil Viginere : {}".format(result_viginere))

    # Final Encryption
    data_encrypt = list(result_viginere)
    data_final = []
    data_random = string.ascii_letters + string.printable
    data = int(len(data_encrypt)) + 10
    for i in range(data):
        random_choice = random.choice(data_random)
        data_final.append(random_choice)

    data_index = 0
    for index, data in enumerate(data_final):
        get_data = str(random.choice(data_random))
        if str(data).isalpha():
            if int(data_index) < int(len(data_encrypt)):
                data_final[index] = data_encrypt[data_index]
                data_index += 1
            
            else:
                while get_data.isalpha() == True:
                    get_data = str(random.choice(data_random))

                data_final[index] = str(get_data)

        else:
            continue
    
    result = "".join(i for i in data_final)
    print("Hasil Final : {}".format(result))
    # print(f"Akhir : {result}")
    return result


def decrypt_combined_chipper(cipher, key):
    print("===== Decrypt Combined Chipper =====")
    # Decrypy Viginere
    chiper_new = []
    for i in range(len(cipher)):
        if str(cipher[i]).isalpha() == True:
            chiper_new.append(cipher[i])
        elif str(cipher[i]) == " ":
            chiper_new.append(" ")
    
    cipher = "".join(i for i in chiper_new)
    cipher_new = cipher.upper()
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    cipher_int = [ord(i) for i in cipher_new]
    plaintext = []
    for i in range(len(cipher_int)):
        value = (cipher_int[i] - key_as_int[i % key_length]) % 26
        if str(cipher[i]) == " ":
            plaintext.append(" ")
        else:
            plaintext.append(chr(value + 65))
    
    for i in range(len(plaintext)):
        if str(chiper_new[i]).isupper() == False:
            plaintext[i] = str(plaintext[i]).lower()

    plaintext = "".join(i for i in plaintext)
    print("Decrypt Viginere : {}".format(plaintext))

    # Decrypt Caesar
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    beta = "abcdefghijklmnopqrstuvwxyz"
    result = []
    key_caesar = 3

    for letter in plaintext:
        if letter.isupper() == True:
            if letter in alpha: #if the letter is actually a letter
                #find the corresponding ciphertext letter in the alphabet
                letter_index = (alpha.find(letter) - key_caesar) % len(alpha)

                result.append(alpha[letter_index])
            else:
                result.append(letter)
        
        else:
            if letter in beta: #if the letter is actually a letter
                #find the corresponding ciphertext letter in the alphabet
                letter_index = (beta.find(letter) - key_caesar) % len(beta)

                result.append(beta[letter_index])
            else:
                result.append(letter)

    result = "".join(i for i in result)
    print("Decrypt Caesar : {}".format(result))
    return result

def signup(email_inp, nama_inp, password_inp):
    try:
        sqliteConnection = sqlite3.connect('enkripsi.db')
        cursor = sqliteConnection.cursor()
        
        sqlite_insert_query = """INSERT INTO akun
                               VALUES 
                              (?, ?, ?);
                              """
        data_tuple = (email_inp, nama_inp, password_inp)
            
        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        cursor.close()
        return True
        
    except sqlite3.Error as error:
        return False
    
    finally:
        if sqliteConnection:
            sqliteConnection.close()


def login(emai_inp, password_inp):
    try:
        sqliteConnection = sqlite3.connect('enkripsi.db')
        cursor = sqliteConnection.cursor()
        statement = f"SELECT Email FROM akun WHERE Email='{emai_inp}' AND Password = '{password_inp}';"
        row_count_admin = cursor.execute(statement)
        data_admin = cursor.fetchone()
        if not data_admin:
            cursor.close()
            return False
        else:
            cursor.close()
            return True
            
    except sqlite3.Error as error:
        return False
    
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def send_key(email_inp, key_inp):
    try:
        sqliteConnection = sqlite3.connect('enkripsi.db')
        cursor = sqliteConnection.cursor()
        
        sqlite_insert_query = """INSERT INTO key
                               VALUES 
                              (?, ?);
                              """
        data_tuple = (email_inp, key_inp)
            
        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        cursor.close()
        return True
        
    except sqlite3.Error as error:
        return False
    
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    

def check_key(email_inp):
    try:
        sqliteConnection = sqlite3.connect('enkripsi.db')
        cursor = sqliteConnection.cursor()
        statement = f"SELECT key FROM key WHERE Email='{email_inp}'"
        row_count_admin = cursor.execute(statement)
        data_admin = cursor.fetchone()
        if not data_admin:
            cursor.close()
            return False
        else:
            data_admin = data_admin[0]
            cursor.close()
            return [True, data_admin]
            
    except sqlite3.Error as error:
        return False
    
    finally:
        if sqliteConnection:
            sqliteConnection.close()
