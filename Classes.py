# this is the etablishment of all the class that are used

# main thing we pull from mySQL so the plan is to be able to have functionality to change different
# get should be used to put the data on the database

class Customer ():
    def __init__ (self):
        self.First_name = ""
        self.Last_name = ""
        self.Phone = ""
        self.Email = ""
        self.ID = 000000
        self.password = ""
        self.Category = "Customer"

    # this is so when we pull data from the database
    def setALL(self,firstname,lastname,phone,Email,password,category):
        self.ChangePassword(password)
        self.ChangeFName(firstname)
        self.ChangeLName(lastname)
        self.ChangePhone(phone)
        self.ChangeEmail(Email)
        self.Category = category

    # this and next one is to keep passwords secured
    def Hashed(self,password):
        return (",").join([str(ord(char)) for char in password ])

    def unHashed(self):
        return ("").join([chr(int(item)) for item in password.split(",")])

    # this is to put all the data in the database

    def getALL(self):
        return self.First_name,self.Last_name,\
               self.Phone,self.Email ,self.ID,self.unHashed(),self.Category

    # this is for the account info page
    def GetPassword(self):
        self.__temp_password = unHashed(self.password)
        Length = len(self.__temp_password)
        if Length <= 3 :
            return "*"*Length
        
       return ("*"*(len(self.__temp_password)-3) + self.__temp_password[-3:])

    # for set all and if you wana just change a specific version
    def ChangePassword(self,password):
        self.password = self.Hashed(password)

    def ChangeFName(self,firstname):
        self.First_name = firstname

    def ChangeLName(self,lastname):
        self.Last_name = lastname

    def ChangeEmail(self,email):
        self.Email = email

    def ChangePhone(self,phone):
        self.Phone = phone

    def setID(self,ID):
        self.ID = ID

# need to plan how the tkinter gonna look to continue

    
        
        
        
