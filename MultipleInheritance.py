from ContactsApp.contacts import Contact

class MailSender:
    def send_mail(self, message = None):
        print("Sending email to: " + self.email)
        #Add email logix here

class EmailableContact(Contact, MailSender):
    pass


#test
# ec = EmailableContact("Jhon Doe", "jdoe@example.net")
# ec.send_mail("Hello World")
# -> Sending email to: jdoe@example.net