password = input("Enter your password: ")

# Flags
has_upper = False
has_lower = False
has_digit = False
has_symbol = False

symbols = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/`~"

# Check each character
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in symbols:
        has_symbol = True

length = len(password)

# Determine password strength
if length < 6:
    strength = "Weak"
elif length >= 8 and has_upper and has_lower and has_digit and has_symbol:
    strength = "Strong"
else:
    strength = "Medium"

# Display results
print("\nPassword Analysis")
print("Length:", length)
print("Contains Uppercase:", has_upper)
print("Contains Lowercase:", has_lower)
print("Contains Number:", has_digit)
print("Contains Symbol:", has_symbol)

print("\nPassword Strength:", strength)