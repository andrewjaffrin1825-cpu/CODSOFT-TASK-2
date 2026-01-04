"""
Password Generator
A tool to generate strong and random passwords with customizable options
"""

import random
import string


class PasswordGenerator:
    """A password generator class for creating secure passwords"""
    
    def __init__(self):
        """Initialize the password generator"""
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special = string.punctuation
    
    def generate_simple(self, length):
        """Generate a simple password with letters and numbers only"""
        if length < 1:
            return "❌ Error: Password length must be at least 1!"
        
        characters = self.lowercase + self.uppercase + self.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def generate_strong(self, length):
        """Generate a strong password with letters, numbers, and special characters"""
        if length < 4:
            return "❌ Error: Strong password must be at least 4 characters!"
        
        characters = self.lowercase + self.uppercase + self.digits + self.special
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def generate_custom(self, length, use_lowercase=True, use_uppercase=True, 
                       use_digits=True, use_special=False):
        """Generate a custom password based on specified criteria"""
        if length < 1:
            return "❌ Error: Password length must be at least 1!"
        
        characters = ""
        
        if use_lowercase:
            characters += self.lowercase
        if use_uppercase:
            characters += self.uppercase
        if use_digits:
            characters += self.digits
        if use_special:
            characters += self.special
        
        if not characters:
            return "❌ Error: Select at least one character type!"
        
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def check_password_strength(self, password):
        """Check the strength of a password"""
        strength = 0
        feedback = []
        
        if len(password) >= 8:
            strength += 1
        else:
            feedback.append("- Increase length to at least 8 characters")
        
        if any(c.islower() for c in password):
            strength += 1
        else:
            feedback.append("- Add lowercase letters")
        
        if any(c.isupper() for c in password):
            strength += 1
        else:
            feedback.append("- Add uppercase letters")
        
        if any(c.isdigit() for c in password):
            strength += 1
        else:
            feedback.append("- Add numbers")
        
        if any(c in self.special for c in password):
            strength += 1
        else:
            feedback.append("- Add special characters")
        
        if strength == 5:
            return "🔒 Very Strong", feedback
        elif strength >= 4:
            return "💪 Strong", feedback
        elif strength >= 3:
            return "👍 Medium", feedback
        elif strength >= 2:
            return "⚠️  Weak", feedback
        else:
            return "❌ Very Weak", feedback


def display_menu():
    """Display the password generator menu"""
    print("\n" + "="*70)
    print("🔐 PASSWORD GENERATOR 🔐")
    print("="*70)
    print("\nGeneration Options:")
    print("1️⃣  Simple Password (Letters + Numbers)")
    print("2️⃣  Strong Password (Letters + Numbers + Special Characters)")
    print("3️⃣  Custom Password (Choose what to include)")
    print("4️⃣  Check Password Strength")
    print("5️⃣  Exit")
    print("="*70)


def get_password_length():
    """Get password length from user"""
    try:
        length = int(input("\n📏 Enter desired password length: "))
        if length < 1:
            print("❌ Password length must be at least 1!")
            return None
        return length
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return None


def generate_simple_password():
    """Generate a simple password"""
    generator = PasswordGenerator()
    length = get_password_length()
    
    if length is None:
        return
    
    password = generator.generate_simple(length)
    
    print("\n" + "-"*70)
    print(f"✅ Generated Simple Password:")
    print(f"   🔑 {password}")
    print(f"   📏 Length: {len(password)} characters")
    print("-"*70)


def generate_strong_password():
    """Generate a strong password"""
    generator = PasswordGenerator()
    length = get_password_length()
    
    if length is None:
        return
    
    password = generator.generate_strong(length)
    
    if isinstance(password, str) and password.startswith("❌"):
        print(password)
        return
    
    strength, feedback = generator.check_password_strength(password)
    
    print("\n" + "-"*70)
    print(f"✅ Generated Strong Password:")
    print(f"   🔑 {password}")
    print(f"   📏 Length: {len(password)} characters")
    print(f"   💪 Strength: {strength}")
    print("-"*70)


def generate_custom_password():
    """Generate a custom password with user preferences"""
    generator = PasswordGenerator()
    
    print("\n" + "-"*70)
    print("📋 Custom Password Options:")
    print("-"*70)
    
    length = get_password_length()
    if length is None:
        return
    
    print("\nSelect character types to include:")
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generator.generate_custom(length, use_lowercase, use_uppercase, 
                                         use_digits, use_special)
    
    if isinstance(password, str) and password.startswith("❌"):
        print(f"\n{password}")
        return
    
    strength, feedback = generator.check_password_strength(password)
    
    print("\n" + "-"*70)
    print(f"✅ Generated Custom Password:")
    print(f"   🔑 {password}")
    print(f"   📏 Length: {len(password)} characters")
    print(f"   💪 Strength: {strength}")
    if feedback:
        print(f"   📝 Suggestions to improve:")
        for suggestion in feedback:
            print(f"      {suggestion}")
    print("-"*70)


def check_password_strength():
    """Check the strength of a user-provided password"""
    generator = PasswordGenerator()
    
    print("\n" + "-"*70)
    password = input("🔑 Enter password to check: ")
    
    if not password:
        print("❌ Password cannot be empty!")
        return
    
    strength, feedback = generator.check_password_strength(password)
    
    print("\n" + "-"*70)
    print(f"Password Analysis:")
    print(f"   🔐 {password}")
    print(f"   📏 Length: {len(password)} characters")
    print(f"   💪 Strength: {strength}")
    
    if feedback:
        print(f"\n   📝 Suggestions to improve:")
        for suggestion in feedback:
            print(f"      {suggestion}")
    print("-"*70)


def main():
    """Main password generator loop"""
    print("\n" + "="*70)
    print("Welcome to Password Generator!")
    print("Create strong and secure passwords easily")
    print("="*70)
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            generate_simple_password()
        
        elif choice == '2':
            generate_strong_password()
        
        elif choice == '3':
            generate_custom_password()
        
        elif choice == '4':
            check_password_strength()
        
        elif choice == '5':
            print("\n👋 Thank you for using Password Generator! Stay secure!\n")
            break
        
        else:
            print("\n❌ Invalid choice! Please select 1-5.\n")


if __name__ == "__main__":
    main()
