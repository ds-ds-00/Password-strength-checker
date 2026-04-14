import math
import re

def check_strength(password):
    length = len(password)

    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"[0-9]", password)
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = 0

    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    return score

def strength_label(score):
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"
    

def estimate_crack_time(password, guesses_per_second=1e12):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    length = len(password)

    # Guard against empty password or no charset
    if charset == 0 or length == 0:
        return 0

    # Total possible combinations
    combinations = charset ** length

    # Estimated crack time in seconds
    seconds = combinations / guesses_per_second

    return seconds




def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"


def is_common(password, filepath="rockyou.txt"):
    try:
        with open(filepath, "r", encoding="latin-1") as f:
            for line in f:
                if line.strip() == password:
                    return True
        return False
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    password = input("Enter password: ")
    if password.strip() == "":
        print("Please enter a valid password.")
        exit(1)

    score = check_strength(password)
    label = strength_label(score)
    time_sec = estimate_crack_time(password)

    print(f"\nStrength: {label}")
    print(f"Crack Time: {format_time(time_sec)}")

    if is_common(password):
        print("This is a COMMON password! Extremely unsafe.")
    
