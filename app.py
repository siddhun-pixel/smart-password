import string
import random

# Breached passwords list
breached_words = ["password", "123456", "admin", "qwerty", "letmein"]

def generate_password(length=12, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(pw):
    score = 0
    suggestions = []

    if len(pw) >= 8:
        score += 1
    else:
        suggestions.append("- Add more characters (minimum 8)")

    if any(c.islower() for c in pw):
        score += 1
    else:
        suggestions.append("- Include lowercase letters")

    if any(c.isupper() for c in pw):
        score += 1
    else:
        suggestions.append("- Include uppercase letters")

    if any(c.isdigit() for c in pw):
        score += 1
    else:
        suggestions.append("- Include digits (0-9)")

    if any(c in string.punctuation for c in pw):
        score += 1
    else:
        suggestions.append("- Include symbols like ! @ #")

    if any(b in pw.lower() for b in breached_words):
        suggestions.append("- Avoid using common passwords")
        score = 0

    if score <= 2:
        return "Weak", suggestions
    elif score <= 4:
        return "Moderate", suggestions
    else:
        return "Strong", suggestions

# --- CLI Interface ---
def main():
    while True:
        print("\n--- Smart Password Checker ---")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            length = int(input("Enter password length (8-20): "))
            use_digits = input("Include digits? (y/n): ").lower() == "y"
            use_symbols = input("Include symbols? (y/n): ").lower() == "y"
            pw = generate_password(length, use_digits, use_symbols)
            print("Generated Password:", pw)
        elif choice == "2":
            pw = input("Enter password to check: ")
            strength, suggestions = check_strength(pw)
            print("Strength:", strength)
            if suggestions:
                print("Suggestions:")
                for s in suggestions:
                    print(s)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
  main()
