
# Program
# Class for Aadhar card
class Aadhar:

    # Dictionary
    user = {
        'name': '',
        'phone': '',
        'PAN': '',
        'VoterID': ''
    }

    relatives = []
    # Constructor

    def __init__(self, username):
        self.user['name'] = username

    def addPhoneNumber(self, phonenumber: int):
        str_phone = str(phonenumber)
        if (len(str_phone) == 10):
            self.user['phone'] = phonenumber
            print("[SUCCESS] - Phone number recorded for " + self.user['name'])
        else:
            print("[FAIL] - Phone number exceed")

    def addVoterID(self, voterid: str):
        self.user['VoterID'] = voterid
        print("[SUCCESS] - Voter ID recorded for " + self.user['name'])

    def addRelative(self):
        # Do while
        run = True    # Boolean value
        while (run):
            name = str(input("Enter your relative name : "))
            self.relatives.append(name)
            print("[SUCCESS - Relative Added for " + self.user['name'])
            option = str(input("Do you want to add more relative : (Y/N)"))
            if option == 'y':
                run = True
            else:
                run = False

    def showUserDetail(self):
        print(" User Name   : " + str(self.user['name']))
        print(" Voter ID    : " + str(self.user['VoterID']))
        print(" Phone number: " + str(self.user['phone']))
        print(" Relatives   : " + str(self.relatives))


# Main program
person1 = Aadhar("Vivek")
person1.addPhoneNumber(int(input("Enter the Phone number : ")))
person1.addVoterID(str(input("Enter the voter ID : ")))
person1.addRelative()

person1.showUserDetail()
