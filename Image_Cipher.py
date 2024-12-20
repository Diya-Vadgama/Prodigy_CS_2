from PIL import Image
import numpy as np


def encrypt_image(image_path, key, output_path):
    """
    Encrypts an image by modifying pixel values using a key.

    Args:
    - image_path (str): Path to the input image.
    - key (int): Encryption key (integer).
    - output_path (str): Path to save the encrypted image.
    """
    image = Image.open(image_path)
    image_array = np.array(image, dtype=np.int16)  # Use int16 to prevent overflow
    
    # Apply encryption: Add key to pixel values
    encrypted_array = (image_array + key) % 256  # Ensure values remain in range [0, 255]
    encrypted_array = encrypted_array.astype(np.uint8)  # Convert back to uint8
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")


def decrypt_image(image_path, key, output_path):
    """
    Decrypts an image by reversing the encryption process.

    Args:
    - image_path (str): Path to the encrypted image.
    - key (int): Encryption key (integer).
    - output_path (str): Path to save the decrypted image.
    """
    image = Image.open(image_path)
    image_array = np.array(image, dtype=np.int16)  # Use int16 to prevent overflow
    
    # Apply decryption: Subtract key from pixel values
    decrypted_array = (image_array - key) % 256  # Ensure values remain in range [0, 255]
    decrypted_array = decrypted_array.astype(np.uint8)  # Convert back to uint8
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")


def main():
    print("Simple Image Encryption Tool")
    
    while True:
        print("\nOptions:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            image_path = input("Enter the path to the image to encrypt: ").strip()
            key = int(input("Enter the encryption key (integer): "))
            output_path = input("Enter the output path for the encrypted image: ").strip()
            encrypt_image(image_path, key, output_path)
        elif choice == '2':
            image_path = input("Enter the path to the image to decrypt: ").strip()
            key = int(input("Enter the decryption key (integer): "))
            output_path = input("Enter the output path for the decrypted image: ").strip()
            decrypt_image(image_path, key, output_path)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
