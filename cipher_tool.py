#!/usr/bin/env python3
# cipher_tool.py — Caesar Cipher Tool (Metasploit-like banner)
import sys

# Try to import pretty-print libraries; if missing, we'll fall back gracefully.
try:
    import pyfiglet
except Exception:
    pyfiglet = None

try:
    from termcolor import colored
except Exception:
    # simple fallback if termcolor not installed
    def colored(text, color=None, attrs=None):
        return text

# ---------------- Banner ----------------
def print_banner():
    # main big title and author subtitle
    big_title = "Caesar Cipher Tool"
    subtitle = "by Harsh Chaudhary"

    if pyfiglet:
        try:
            art = pyfiglet.figlet_format(big_title, font="slant")
        except Exception:
            art = pyfiglet.figlet_format(big_title)
        print(colored(art, "cyan"))
        # subtitle printed centered-ish under the art
        print(colored(subtitle.center(60), "yellow", attrs=["bold"]))
    else:
        # fallback ASCII-art (small)
        print(colored("██████╗  █████╗ ███████╗ █████╗ ███████╗", "cyan"))
        print(colored("██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝", "cyan"))
        print(colored("██████╔╝███████║█████╗  ███████║███████╗", "cyan"))
        print(colored("██╔═══╝ ██╔══██║██╔══╝  ██╔══██║╚════██║", "cyan"))
        print(colored("██║     ██║  ██║███████╗██║  ██║███████║", "cyan"))
        print(colored("╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝\n", "cyan"))
        print(colored(subtitle.center(60), "yellow", attrs=["bold"]))

    # metadata box similar to metasploit style
    width = 60
    meta_lines = [
        "Simple Caesar cipher: shift letters by N",
        "Author  : Harsh Chaudhary",
        "Version : 1.0",
        "Usage   : Encrypt / Decrypt text from terminal"
    ]
    border = "+" + "-" * (width - 2) + "+"

    print(colored(border, "green"))
    for line in meta_lines:
        content = f"| {line}" + " " * (width - 3 - len(line)) + "|"
        print(colored(content, "green"))
    print(colored(border + "\n", "green"))

# ---------------- Caesar Cipher Logic ----------------
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(cipher_text, shift):
    return caesar_encrypt(cipher_text, -shift)

# ---------------- CLI ----------------
def main():
    print_banner()
    while True:
        try:
            choice = input(colored("Select (E)ncrypt / (D)ecrypt / (Q)uit: ", "yellow")).strip().upper()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            sys.exit(0)

        if choice == "Q":
            print(colored("Goodbye 👋", "magenta"))
            break
        if choice not in ("E", "D"):
            print(colored("Invalid option — choose E, D or Q.\n", "red"))
            continue

        text = input(colored("Enter your text: ", "yellow"))
        # validate shift
        while True:
            try:
                shift = int(input(colored("Enter shift value (1-25): ", "yellow")).strip())
                if 1 <= abs(shift) <= 25:
                    break
                else:
                    print(colored("Shift must be between 1 and 25.", "red"))
            except ValueError:
                print(colored("Please enter a valid integer.", "red"))

        if choice == 'E':
            encrypted = caesar_encrypt(text, shift)
            print(colored(f"\nEncrypted text: {encrypted}\n", "cyan"))
        else:
            decrypted = caesar_decrypt(text, shift)
            print(colored(f"\nDecrypted text: {decrypted}\n", "cyan"))

if __name__ == "__main__":
    main()
