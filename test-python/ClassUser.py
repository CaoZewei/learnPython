class User:
    def __init__(self, fname, lname, *describe) -> None:
        """初始化user"""
        self.fname = fname
        self.lname = lname
        self.describe = describe

    def describe_user(self):
        print('let me introduce', self.fname, self.lname)
        for info in self.describe:
            print(info)

    def greet_user(self):
        print("greeting my greatest master", self.fname.title(), self.lname.title())


master = User('jack', 'william', 'The most powerful magician', 'The guardian of the world', 'Master of Islam')
master.describe_user()
master.greet_user()
