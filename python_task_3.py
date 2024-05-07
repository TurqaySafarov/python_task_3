class Person:
    def __init__(self, name, age, occupation, birth_year):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.birth_year = birth_year

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Occupation:", self.occupation)
        print("Birth Year:", self.birth_year)


class AgeClassifier:
    @staticmethod
    def classify_age(age):
        if age < 18:
            return "Child"
        elif 18 <= age < 65:
            return "Adult"
        else:
            return "Senior"


person1 = Person("Alice", 25, "Software Engineer", 1999)
person2 = Person("Bob", 45, "Doctor", 1979)
person3 = Person("Charlie", 70, "Retired", 1954)

print("Person Information: ")
person1.display()
print("\nPerson Information:")
person2.display()
print("\nPerson Information:")
person3.display()

print(f"\n{person1.name} is {person1.age} years old and is classified as {AgeClassifier.classify_age(person1.age)}")
print(f"{person2.name} is {person2.age} years old and is classified as {AgeClassifier.classify_age(person2.age)}")
print(f"{person3.name} is {person3.age} years old and is classified as {AgeClassifier.classify_age(person3.age)}")
