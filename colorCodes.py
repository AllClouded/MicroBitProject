import serial

# Color codes for terminal text
GREEN = "\033[1;32;40m"
GRAY = "\033[0;37;40m"

# Initialize the serial connection to the MicroBit
connection = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)

# List to store unseen messages
inbox = []

def send_message():
    user_input = input("Enter your message (type 'INBOX' to check messages): ")

    # If the user types 'INBOX', show all unseen messages
    if user_input.upper() == "INBOX":
        receive_messages()
        show_inbox()
    else:
        message = str(user_input)
        connection.write(message.encode())

def receive_messages():
    while connection.in_waiting > 0:
        message = connection.readline().decode().strip()
        inbox.append(message)

def show_inbox():
    if inbox:
        print(f"{GREEN}--- INBOX ---{GRAY}")
        for msg in inbox:
            print(f"{GREEN}{msg}{GRAY}")
            print("/n")
        inbox.clear()  # Clear the inbox after showing messages
        print(f"{GREEN}--- END OF INBOX ---{GRAY}")
    else:
        print(f"{GREEN}Your inbox is empty.{GRAY}")

def main():
    while True:
        # Check for incoming messages and buffer them
        receive_messages()

        # Allow the user to send a message or check their inbox
        send_message()

# Run the main function
main()