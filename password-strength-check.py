import re

def check_password_strength(password):
    # Define the criteria for the password
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])

    # Provide feedback based on how many criteria were met
    if criteria_met == 5:
        strength = "Strong"
    elif 3 <= criteria_met < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Detailed feedback for the user
    feedback = f"Password Strength: {strength}\n"
    feedback += f"- Length >= 8 characters: {'✓' if length_criteria else '✗'}\n"
    feedback += f"- Contains lowercase letter: {'✓' if lowercase_criteria else '✗'}\n"
    feedback += f"- Contains uppercase letter: {'✓' if uppercase_criteria else '✗'}\n"
    feedback += f"- Contains number: {'✓' if number_criteria else '✗'}\n"
    feedback += f"- Contains special character: {'✓' if special_char_criteria else '✗'}\n"
    
    return feedback

# Example usage
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
