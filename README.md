# Caesar Cipher — Encryption & Decryption

A Python program that encrypts and decrypts text using the Caesar Cipher, a classic substitution cipher. Built as **Project 2** of the DecodeLabs Cybersecurity Industrial Training Kit (2026 batch).

## Overview

Before implementing advanced security protocols, an analyst needs to understand the fundamental mechanics of confidentiality: turning readable text (plaintext) into unreadable text (ciphertext), and reversing that process exactly. This project implements that using the Caesar Cipher — one of the oldest known encryption techniques, based on shifting each letter a fixed number of places through the alphabet.

## How it works

Every letter in the alphabet has a position (A=0, B=1, ... Z=25). The cipher shifts that position by a chosen key `n`:

**Encryption:**
```
E(x) = (x + n) mod 26
```

**Decryption (the reverse):**
```
D(x) = (x - n) mod 26
```

The modulo (`% 26`) is what makes the alphabet "wrap around" — for example, with a shift of 3, `Z` doesn't break the cipher, it just wraps back to `C`.

### Example

| Step | Value |
|---|---|
| Character | `A` |
| ASCII value | 65 |
| Subtract base (65) | 0 |
| Add shift key (+3) | 3 |
| Apply modulo (%26) | 3 |
| Add base back (+65) | 68 |
| Result character | `D` |

## Features

- **Encrypt or decrypt** any text with a user-chosen shift key (not hardcoded)
- **Case-preserving** — uppercase letters stay uppercase, lowercase stays lowercase
- **Non-letter characters pass through untouched** — spaces, numbers, and punctuation are not altered, avoiding garbled output
- **Round-trip verification** — after encrypting, the program automatically decrypts the result and shows it matches the original
- **Frequency analysis demo** — displays a simple letter-frequency chart of the ciphertext, illustrating why the Caesar Cipher is considered weak by modern standards (it preserves the statistical shape of the underlying language, making it breakable through frequency analysis alone)

## Usage

Requires Python 3.6+ (no external dependencies).

```bash
python3 caesar_cipher.py
```

You'll see a menu:
```
Choose an option:
  1. Encrypt text
  2. Decrypt text
  3. Quit
Enter choice (1/2/3):
```

Enter your text and a shift key (e.g. `3`) when prompted.

### Example run

```
Enter choice (1/2/3): 1
Enter your text: Attack at Dawn!
Enter shift key (e.g. 3): 5

Original Text : Attack at Dawn!
Encrypted Text: Fyyfhp fy Ifbs!
Decrypted Back: Attack at Dawn!

Letter frequency in ciphertext:
  F: ## (2)
  Y: ## (2)
  ...
```

## Test Cases Verified

| Input | Shift | Output | Round-trip |
|---|---|---|---|
| `HELLO` | 3 | `KHOOR` | Pass |
| `Attack at Dawn!` | 5 | `Fyyfhp fy Ifbs!` | Pass |
| `xyz` | 5 | `cde` (alphabet wraparound) | Pass |
| `DecodeLabs 2026` | 7 | Digits/spaces unchanged | Pass |
| `""` (empty string) | 3 | `""` (no crash) | Pass |

## Why the Caesar Cipher Is Weak

This project intentionally includes a frequency analysis feature to demonstrate a key security lesson: shifting every letter by the same fixed amount preserves the *shape* of the letter-frequency distribution — only its position on the chart changes. Combined with a tiny key space (only 25 possible shifts), this makes the cipher trivial to break, which is why modern cryptography (like AES) relies on far more complex transformations (confusion, diffusion, much larger keys).

## Project Structure

```
caesar-cipher-project/
├── caesar_cipher.py   # Main program
└── README.md          # This file
```

## Key Skills Demonstrated

- ASCII/character manipulation (`ord()`, `chr()`)
- Modular arithmetic for alphabet wraparound
- Reversible (symmetric) algorithm design
- Basic cryptanalysis awareness (frequency analysis)

## Author

Shreya C N — DecodeLabs Industrial Training Kit, 2026 Batch
