from PIL import Image
import numpy as np 

def encrypt_image(image_path, key):
    original_image = Image.open(image_path)

    image_array = np.array(original_image)

    encrypted_array = np.bitwise_xor(image_array, key)

    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))

    encrypted_image.save("encrypted_image.png")
    print("Image encrypted Successfully!")


def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    
    encrypted_array = np.array(encrypted_image)

    decrypted_array = np.bitwise_xor(encrypted_array, key)

    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))

    # Save the decrypted image
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully!")


def main():
    image_path = "Moonlight.jpg"
    
    # Get the dimensions and channels of the image
    original_image = Image.open(image_path)
    height, width, channels = np.array(original_image).shape

    # Generate a random key based on the image dimensions and channels
    key = np.random.randint(0, 255, size=(height, width, channels), dtype=np.uint8)

    # Encrypt the image
    encrypt_image(image_path, key)

    # Decrypt the image
    decrypt_image("encrypted_image.png", key)


if __name__ == "__main__":
    main()

