# Liskov substitution principle

# BAD solution
"""
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f"Send '{message}' to {email}")


class SMS(Notification):
    def notify(self, message, phone):
        print(f"Send '{message}' to {phone}")


if __name__ == '__main__':
    notification = Email()
    notification.notify(message="Ahoj", email="john@smith.com")
"""
from abc import ABC, abstractmethod


# GOOD solution with Liskov substitute principle

class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f"Send '{message}' to {self.email}")


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"Send '{message}' to {self.phone}")


class WhatsApp(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"Send '{message}' to WhatsApp {self.phone}")


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


if __name__ == '__main__':
    contact = Contact(name="John", email="john@wick.com", phone="123456789")

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    sms_notification.notify("Posílám SMS")
    email_notification.notify("Posílám email")

    user_selection = input("Select notification E=email, S=SMS, W=WhatsApp: ")
    if user_selection == "E":
        my_notification = Email(contact.email)
    elif user_selection == "S":
        my_notification = SMS(contact.phone)
    elif user_selection == "W":
        my_notification = WhatsApp(contact.phone)
    else:
        my_notification = Email(contact.email)
    my_notification.notify("New message 1")
    my_notification.notify("New message 2")
    my_notification.notify("New message 3")
    my_notification.notify("New message 4")
    my_notification.notify("New message 5")
    my_notification.notify("New message 6")