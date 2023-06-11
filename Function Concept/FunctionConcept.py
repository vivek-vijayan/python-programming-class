# Function conceptsc
# without parameter
def call_me_hello():
    print("Hello!!")


call_me_hello()

# with paramter


def call_my_name(name):
    print("Hello !!" + name)


call_my_name("Vivek")

# Multiple parameter


def upload_aadhar_details(name, address, phone):
    print("Name : " + name)
    print("Address : " + address)
    print("Phone : " + phone)


upload_aadhar_details(phone="987654321", name="Vivek", address="TMVoyal")


# Default value
def aadhar_card(name, phone, voterid="voter123"):
    print(name)
    print(voterid)
    print(phone)


aadhar_card(name="Vivek", phone="987654", voterid="vijai")
aadhar_card()


# Data type in parameter

def add(a: int, b: int):
    return a + b

