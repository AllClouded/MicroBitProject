import serial

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
        print("--- INBOX ---")
        for msg in inbox:
            print(f"{msg}")
            print("")
        inbox.clear()  
        print("--- END OF INBOX ---")
    else:
        print("Your inbox is empty")


def main():
    ## Loop to always send a message

    while True:
        receive_messages()
        send_message()

# Runs the main function
main()