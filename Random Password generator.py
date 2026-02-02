# Import required modules
import secrets
import string

# Ask the user to enter their password
password = input("Enter your password to validate: ")

# Check password length
if len(password) < 8:
    print("❌ Password is too short. Minimum 8 characters required.")
    generate_new = True
else:
    # Check for different character types
    has_lowercase = any(c in string.ascii_lowercase for c in password)
    has_uppercase = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    # Display results
    print("\n--- Password Strength Analysis ---")
    print("✓ Password length:" if len(password) >= 8 else "❌ Password length:", len(password), "characters")
    print("✓ Contains lowercase" if has_lowercase else "❌ Missing lowercase")
    print("✓ Contains uppercase" if has_uppercase else "❌ Missing uppercase")
    print("✓ Contains numbers" if has_digit else "❌ Missing numbers")
    print("✓ Contains special characters" if has_special else "❌ Missing special characters")
    
    # Overall strength
    if all([has_lowercase, has_uppercase, has_digit, has_special]):
        print("\n✅ Strong password! Your password is secure.")
        generate_new = False
    else:
        print("\n Password is not strong enough.")
        generate_new = True

# Generate a strong password if needed
if generate_new:
    print("\n Generating a strong password for you...\n")
    
    # Ask for desired length
    try:
        length = int(input("Enter desired password length (minimum 8): "))
        if length < 8:
            print("Length too short. Using minimum length of 12.")
            length = 12
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Ensure at least one of each character type
    new_password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]
    
    # Fill the rest randomly
    all_characters = lowercase + uppercase + digits + symbols
    new_password += [secrets.choice(all_characters) for _ in range(length - 4)]
    
    # Shuffle to avoid predictable pattern
    secrets.SystemRandom().shuffle(new_password)
    
    # Convert list to string
    new_password = ''.join(new_password)
    
    print("\n✅ Generated Strong Password:", new_password)
    print("\n💡 Tip: Save this password in a secure password manager!")





