def encrypt(text,s):
    result = ""

    for i in range (len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        else:
            result += chr((ord(char) + s-97) % 26 + 97)

    return result

def decrypt(en_text, s):
    de_result = ""

    for i in range(len(en_text)):
        en_char = en_text[i] 

        if (en_char.isupper()):
            de_result += chr((ord(en_char) - s-65) % 26 + 65)
        
        else:
            de_result += chr((ord(en_char) - s-97) % 26 + 97)
    
    return de_result 


while True:
    print("1.Encrypt")
    print("2.Decrypt")
    print("3.Exit")

    choice = int(input("Enter your choice(1/2/3): "))

    if choice == 1:
        text = str(input("Enter text to encrypt: "))
        shift = int(input("Enter shift value: "))
        en_text = encrypt(text,shift)

        print(f"Encrypted Text:{en_text}")
    
    elif choice == 2:
        text = input("Enter the text to decrypt: ")
        shift = int(input("Enter shift value: "))
        de_text = decrypt(text,shift)

        print(f"Decrypted Text: {de_text}")
    
    elif choice == 3:
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")
