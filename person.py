# Base class: Person
class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.person_id}")


# Derived class: CrewMember
class CrewMember(Person):
    def __init__(self, name, person_id, role):
        super().__init__(name, person_id)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")


# Further derived class: Pilot
class Pilot(CrewMember):
    def __init__(self, name, person_id, license_number, rank):
        super().__init__(name, person_id, role="Pilot")
        self.license_number = license_number
        self.rank = rank

    def display_info(self):
        super().display_info()
        print(f"License Number: {self.license_number}")
        print(f"Rank: {self.rank}")


# Create a Pilot object and display info
pilot = Pilot("Tanmay", "EMP12345", "LIC987654321", "Captain")
pilot.display_info()
