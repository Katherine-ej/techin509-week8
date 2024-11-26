# Object
# -> Specific intance of a class
# Class
# -> General definition
class iPhone:
    def __init__(self, name, version, phone_number, color, model): #constructor
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.files = []
        self.messages = []

    def check_messages(self):
        pass

    def call(self, number):
        pass

    def airdrop(self, filename, recipient):
        print("Dropping %s" % filename)
        pass

    def airreceive(self):
        pass

    def set_name(self, new_name):
        if len(new_name) < 3:
            print("Name must be longer than 3 character")
        self.name = new_name
    
    def send_messages(self, messages, recipient):
        #print(messages)
        return messages

#Create an instance of iPhone class
ians_iphone = iPhone(
    name="Ian's iPhone",
    version="18",
    phone_number="123-123-1232",
    color="grey",
    model="iPhone 16 Pro",
)
print(ians_iphone.name)

# ians_iphone.name = "Ian's second iPhone"
ians_iphone.set_name("Ian's second iPhone")
print("after name changed:", ians_iphone.name)
#ians_iphone.airdrop("notes.pdf", "")

#Create the second instance of iPhone class
ejs_iphone = iPhone(
    name="EJ's iPhone",
    version="20",
    phone_number="425-123-1111",
    color="white",
    model="iPhone 11",
)
print(ejs_iphone.name)

#change the name
ejs_iphone.set_name("EJ's new iPhone")
print("after name changed:", ejs_iphone.name)
#ejs_iphone.airdrop("notes.pdf", "")

#send messages from ians_phone to ejs_phone
msg = ians_iphone.send_messages("Hi", "EJ's new iPhone")
print("message received:", msg)
