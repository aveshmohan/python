class Father():
    def __init__(self,name,year):
        self.name=name
        self.year=year
        print(self.name,self.year)
class Mother():
    def __init__(self,location):
        self.location=location

        print(self.location)

class Son(Father,Mother):
    def __init__(self,name,year,location,district):
        Father.__init__(self,name, year)
        Mother.__init__(self,location)
        self.district = district
        print(self.district)
obj= Son('futura',2024,'calicut','kozhikode')








