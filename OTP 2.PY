import random

# Function to generate a random 6-digit OTP
def generate_otp():
    return random.randint(100000, 999999)  # 6-digit OTP

# Function to send the OTP via a message
def send_otp_message(phone_number, otp):
    message = f"Your OTP is: {otp}"  # Create the OTP message
    print(f"Sending message to {phone_number}: {message}")
    return message  # Return the OTP message

# Function to verify the OTP
def verify_otp(entered_otp, generated_otp):
    return entered_otp == generated_otp

# Main program
if __name__== "__main__":
    user_phone_number = "1234567890"  # Replace with the user's phone number or email
    generated_otp = generate_otp()
    message = send_otp_message(user_phone_number, generated_otp)
    entered_otp = int(input("Enter the 6-digit OTP you received: "))
    
    if verify_otp(entered_otp, generated_otp):
        print("OTP Verified. Access granted.")
    else:
        print("OTP Verification failed. Access denied.")
    
    print("Message sent:", message)
