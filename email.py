# ### --- OOP Email Simulator --- ###

# # --- Email Class --- #
# # Create the class, constructor and methods to create a new Email object.

#     # Declare the class variable, with default value, for emails. 
 
#     # Initialise the instance variables for emails.

#     # Create the method to change 'has_been_read' emails from False to True.

# # --- Lists --- #
# # Initialise an empty list to store the email objects.

# # --- Functions --- #
# # Build out the required functions for your program.

# def populate_inbox():
    
#     # Create 3 sample emails and add it to the Inbox list. 

# def list_emails():
    
#     # Create a function which prints the email’s subject_line, along with a corresponding number.

# def read_email(index):

#     # Create a function which displays a selected email. 
#     # Once displayed, call the class method to set its 'has_been_read' variable to True.

# # --- Email Program --- #

# # Call the function to populate the Inbox for further use in your program.

# # Fill in the logic for the various menu operations.
# menu = True

# while True:
#     user_choice = int(input('''\nWould you like to:
#     1. Read an email
#     2. View unread emails
#     3. Quit application

#     Enter selection: '''))
       
#     if user_choice == 1:
#         # add logic here to read an email
        
#     elif user_choice == 2:
#         # add logic here to view unread emails
            
#     elif user_choice == 3:
#         # add logic here to quit appplication

#     else:
#         print("Oops - incorrect input.")



class Email:
    
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
        
    def mark_as_read(self):
        self.has_been_read = True
      
        
inbox = []


def populate_inbox():
    samples = [
        ("ivan@wbd.com", "Help for 3.30 zoom call", "I have enabled automatic recording for meeting"),
        ("holly@wbd.com", "Vaisakhi Pizza & Prosecco Takeover", "We will be holding an event for Pizza & Prosecco this week in Warner House"),
        ("chagger@wbd.com", "Meeting room for Legal Call", " I have the booking made for the meeting room"),
    ]
    
    for email_data in samples:
        email_address, subject_line, email_content = email_data
        email = Email(email_address, subject_line, email_content)
        inbox.append(email)
        
populate_inbox()


def list_emails():
    print("inbox:")
    for index, email in enumerate(inbox):
        print(f"{index}. {email.subject_line}")

list_emails()


def read_email():
    mail_index = input("please insert the number of the email that you want to read: ")
    
    try:
        mail_index = int(mail_index)
        

        
        if 0 <= mail_index <= len(inbox):
            selected_email = inbox[mail_index]
            
            print(f"Email Address: {selected_email.email_address}")
            print(f"sunbject: {selected_email.subject_line}")
            print(f"content: {selected_email.email_content}")
            
            selected_email.mark_as_read()
            
        else:
            print("invalid number. you only have three emials in you inbox")
    
    except ValueError:
        print("invalid input. Please entre another number")
        

read_email()