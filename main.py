import cv2
import numpy as np
import os

ENCODED_FOLDER = "encoded_images"

def to_bin(data):
    if isinstance(data, str):
        return ''.join([format(ord(i), "08b") for i in data])
    elif isinstance(data, bytes):
        return ''.join([format(i, "08b") for i in data])
    elif isinstance(data, np.ndarray):
        return [format(i, "08b") for i in data]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")

def generate_output_filename():
    """Generate a default filename like encoded_1.png, encoded_2.png ..."""
    if not os.path.exists(ENCODED_FOLDER):
        os.makedirs(ENCODED_FOLDER)
    i = 1
    while True:
        filename = f"encoded_{i}.png"
        full_path = os.path.join(ENCODED_FOLDER, filename)
        if not os.path.exists(full_path):
            return full_path
        i += 1

def encode(image_name, secret_data, output_image=None):
    image = cv2.imread(image_name)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_name}")

    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    if len(secret_data) > n_bytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or less data.")

    secret_data += "====="
    data_index = 0
    binary_secret_data = to_bin(secret_data)
    data_len = len(binary_secret_data)

    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)
            if data_index < data_len:
                pixel[0] = int(r[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index >= data_len:
                break
        if data_index >= data_len:
            break

    if output_image is None:
        output_image = generate_output_filename()
    cv2.imwrite(output_image, image)
    print(f"[+] Data encoded successfully! Saved as '{output_image}'.")

def decode(image_name):
    image = cv2.imread(image_name)
    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_name}")

    binary_data = ""
    decoded_data = ""
    stop_marker = "====="

    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)
            binary_data += r[-1] + g[-1] + b[-1]

            while len(binary_data) >= 8:
                byte = binary_data[:8]
                binary_data = binary_data[8:]
                decoded_data += chr(int(byte, 2))
                if decoded_data[-len(stop_marker):] == stop_marker:
                    print("[+] Decoded data:", decoded_data[:-len(stop_marker)])
                    return

    print("[!] Stop marker not found in image.")

def main():
    while True:
        print("\n--- Steganography Menu ---")
        print("1. Encode data into an image")
        print("2. Decode data from an image")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            input_image = input("Enter input image path: ").strip()
            secret_data = input("Enter secret data to hide: ").strip()
            try:
                encode(input_image, secret_data)  # Auto filename
            except Exception as e:
                print("[!] Error:", e)

        elif choice == "2":
            encoded_image = input("Enter encoded image path: ").strip()
            try:
                decode(encoded_image)
            except Exception as e:
                print("[!] Error:", e)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("[!] Invalid choice, please try again.")

if __name__ == "__main__":
    main()
