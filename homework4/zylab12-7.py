# Basim Siddiqui
# PSID: 1517778

def get_age():
    user_age = int(input())
    if user_age <= 18 or user_age >= 75:
        raise ValueError("Invalid age.")
    else:
        return user_age

def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * .7
    return heart_rate

if __name__ == "__main__":
    try:
        check_age = get_age()
        burning_rate = fat_burning_heart_rate(check_age)
        print("Fat burning heart rate for a", check_age, "year-old:", burning_rate, 'bpm')
    except ValueError as excpt:
        print(excpt)
        print("Could not calculate heart rate info.\n")

