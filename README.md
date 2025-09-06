# Image Steganography Tool

A **Python-based interactive console application** that allows you to **hide secret messages inside images** and **decode hidden messages** from encoded images. The tool uses **Least Significant Bit (LSB) steganography** to embed data into images without noticeable changes.

---

## Features

* **Interactive Menu** – easily encode or decode messages through a console interface.
* **Automatic storage** – encoded images are saved in a dedicated `encoded_images/` folder with auto-generated filenames (`encoded_1.png`, `encoded_2.png`, etc.).
* **Fast decoding** – stops reading the image as soon as the secret message is fully retrieved.
* **Error handling** – warns when images are missing, corrupted, or when the secret message is too large for the chosen image.

---

## Technologies Used

* **Python 3** – programming language for the application logic.
* **OpenCV (cv2)** – for image reading, writing, and pixel manipulation.
* **NumPy** – for efficient pixel and array operations.

---

## Concept

This project implements **LSB (Least Significant Bit) steganography**, a widely used technique to hide information inside digital media:

* Each pixel of an image has three color channels: **Red, Green, and Blue** (RGB).
* Each channel value is an integer between 0–255, which can be represented in **8-bit binary**.
* LSB steganography replaces the **least significant bit of each color channel** with the secret data bits.
* This allows embedding information without visibly altering the image.

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/bachiriy/secret-in-image.git
cd secret-in-image
```

2. **Install dependencies**:

```bash
pip3 install opencv-python numpy
```

---

## Usage

Run the interactive console app:

```bash
python3 main.py
```

### Menu Options:

1. **Encode data into an image**

   * Enter the path to your input image (PNG recommended).
   * Enter the secret message to hide.
   * The encoded image will be saved automatically in the `encoded_images/` folder.

2. **Decode data from an image**

   * Enter the path to the encoded image.
   * The hidden message will be displayed in the console.

3. **Exit** – closes the application.

---

## Folder Structure

```
image-steganography/
├── main.py                 # Interactive steganography script
├── encoded_images/         # Folder for storing encoded images
├── README.md               # Project documentation
└── requirements.txt        # Optional: dependencies list
```

---

## Example

**Encoding a message**:

```
--- Steganography Menu ---
1. Encode data into an image
2. Decode data from an image
3. Exit
Enter your choice (1/2/3): 1
Enter input image path: input.png
Enter secret data to hide: This is a secret!
[+] Data encoded successfully! Saved as 'encoded_images/encoded_1.png'.
```

**Decoding a message**:

```
--- Steganography Menu ---
1. Encode data into an image
2. Decode data from an image
3. Exit
Enter your choice (1/2/3): 2
Enter encoded image path: encoded_images/encoded_1.png
[+] Decoded data: This is a secret!
```

---

## License

This project is **MIT licensed** – feel free to use, modify, and share.

---
© 2025 Bachiriy.
