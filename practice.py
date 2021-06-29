class Student():
    def __init__(self, name, age, **address):
        self.name = name
        self.age = age
        self.address = address

    def get_message(self):
        print("{}{}{}{}".format(self.address["city"], self.address["street"], self.address["floor"],
                                self.address["number"]))


s = Student("陈某某", 18, city="成都市", street="天府广场一街", floor="3楼", number="1号")
s.get_message()
