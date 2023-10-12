'''You are developing a program to generate personalized email invitations for an event. Each invitation
should include the recipient's name, the event name, and the date. Explain how you would use string
formatting techniques to create these email invitations, and provide an example code snippet to
demonstrate the formatting.'''

invitation_name = input("What is the guest's name? ")
event_name = input("What is the event's name? ")
event_date = input("What is the date of the event? ")

# After taking in the information of the invitee from the user we use string formatting to apply
# that information to a single print statement for everyone. This way everyone receives the same wording 
# without having to worry about one of them being wrong, the only thing the user has to input is the
# person's name and the event name/date.

print(f'Dear {invitation_name}, you are cordially invited to {event_name}. \nThe {event_name} will take place on {event_date}. We hope you can attend.')

