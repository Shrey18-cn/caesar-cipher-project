"""
==================================================================
 DecodeLabs Industrial Training Kit — Project 2
 BASIC ENCRYPTION & DECRYPTION (CAESAR CIPHER)
==================================================================

Goal:
    Implement a simple, reversible encryption technique that
    protects text "in transit" by shifting each letter by a
    fixed key (the Caesar Cipher), and a matching decryption
    function that reverses the process exactly.

Core math (from the DecodeLabs "IPO Model" and "Reverse
Engineering" slides):

    Encryption:  E(x) = (x + shift) % 26
    Decryption:  D(x) = (x - shift) % 26

Where x is a letter's position in the alphabet (A=0 ... Z=25),
NOT its raw ASCII value. We convert to that position first,
do the math, then convert back.

Extra features added (recommended in the project brief):
        - User-selectable shift key (not hardcoded)
        - Case-preserving (uppercase stays uppercase, etc.)
        - Non-letter characters (spaces, digits, punctuation)
          pass through unchanged instead of breaking
        - A simple frequency-analysis demo, showing why Caesar
          Cipher is a "lockbox, not a vault" (per the slides)

Author: Shrey
==================================================================
"""


def encrypt(text: str, shift: int) -> str:
    """
    Encrypts `text` using a Caesar Cipher with the given shift.
    Letters are shifted forward through the alphabet; everything
    else (spaces, numbers, punctuation) is left untouched.
    """
    result = []

    for char in text:
        if char.isupper():
            # 'A' = 65 in ASCII. Subtract 65 to get position 0-25,
            # shift, wrap with %26, then add 65 back.
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(shifted))

        elif char.islower():
            # Same idea, but base is 'a' = 97.
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            result.append(chr(shifted))

        else:
            # Not a letter (space, digit, punctuation, emoji, etc.)
            # -> leave it exactly as it is.
            result.append(char)

    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    """
    Decrypts `text` that was encrypted with the given shift.
    This is symmetric encryption: the same key that locked the
    text also unlocks it — we just shift in the opposite direction.
    """
    # Reusing encrypt() with a negative shift saves us from
    # duplicating the same logic twice.
    return encrypt(text, -shift)


def frequency_analysis_demo(ciphertext: str) -> None:
    """
    Small bonus demo referenced in the slides: shows why the
    Caesar Cipher is weak — letter frequency patterns survive
    the shift untouched, so the shape of the histogram doesn't
    change, only its position. This is what lets an attacker
    break it with basic statistics, no brute force needed.
    """
    from collections import Counter

    counts = Counter(char.upper() for char in ciphertext if char.isalpha())
    if not counts:
        print("No letters to analyze.")
        return

    print("\nLetter frequency in ciphertext:")
    for letter, count in sorted(counts.items(), key=lambda x: -x[1]):
        bar = "#" * count
        print(f"  {letter}: {bar} ({count})")


# ------------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("DecodeLabs Cybersecurity Analyst Toolkit")
    print("Project 2: Basic Encryption & Decryption (Caesar Cipher)\n")

    while True:
        choice = input(
            "Choose an option:\n"
            "  1. Encrypt text\n"
            "  2. Decrypt text\n"
            "  3. Quit\n"
            "Enter choice (1/2/3): "
        ).strip()

        if choice == "3" or choice.lower() == "quit":
            print("Goodbye! Stay secure.")
            break

        if choice not in ("1", "2"):
            print("Invalid choice. Please enter 1, 2, or 3.\n")
            continue

        message = input("Enter your text: ")

        try:
            shift_key = int(input("Enter shift key (e.g. 3): "))
        except ValueError:
            print("Shift key must be a whole number.\n")
            continue

        if choice == "1":
            ciphertext = encrypt(message, shift_key)
            print(f"\nOriginal Text : {message}")
            print(f"Encrypted Text: {ciphertext}")

            # Round-trip check: decrypt it right back to prove
            # the process is fully reversible.
            recovered = decrypt(ciphertext, shift_key)
            print(f"Decrypted Back: {recovered}")

            frequency_analysis_demo(ciphertext)

        else:  # choice == "2"
            plaintext = decrypt(message, shift_key)
            print(f"\nEncrypted Text: {message}")
            print(f"Decrypted Text: {plaintext}")

        print()  # spacing before next loop
