# Caesar Cipher Toolkit

A lightweight Python implementation of the classic **Caesar Cipher** algorithm. This script allows you to easily encrypt and decrypt text using a substitution method based on a fixed alphabet shift.

## Features
* **Full Case Support:** Handles both uppercase and lowercase letters while preserving their casing.
* **Punctuation Safe:** Non-alphabetic characters (like spaces, periods, and exclamation marks) remain unchanged.
* **Input Validation:** Built-in guards ensure the shift key is a valid integer between 1 and 25.

---

## How It Works

The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet. 

This implementation utilizes Python's efficient `str.maketrans()` and `translate()` methods to handle character mapping dynamically. 

* **`caesar(text, shift, encrypt=True)`**: The core function that handles both encryption and decryption logic by slicing and reassembling the alphabet string based on the `shift` value.
* **`encrypt(text, shift)`**: A helper function that calls `caesar()` with `encrypt=True`.
* **`decrypt(text, shift)`**: A helper function that inverts the shift logic (`encrypt=False`) to reverse an encrypted message.

---

## How to Run

### Prerequisites
Make sure you have **Python 3.x** installed on your system. You can check your version by running:
```bash
python --version