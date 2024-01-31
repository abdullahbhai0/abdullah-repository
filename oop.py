class student:
    def __init__(self,name,phone):
        self.name = name
        self.phone_number = phone

    def speak(self,say):
        return f"{self.name}say{say}!"

abdullah=student(phone=3168071852,name="abdullah")
abdurrehman=student("abdurehman",3462373329)

name = abdullah.name
phone_number = abdullah.phone_number
print(phone_number)
