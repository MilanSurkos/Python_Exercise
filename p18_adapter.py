class Student:
    def __init__(self, full_name, contact, is_adult, results):
        self.full_name = full_name
        self.contact = contact
        self.is_adult_ = is_adult
        self.results = results

    def get_full_name(self):
        return self.full_name

    def get_contact_details(self):
        return self.contact

    def is_adult(self):
        return self.is_adult_

    def get_results(self):
        return self.results


class Favorite:
    def __init__(self, first_name, last_name, email, age, grades):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._age = age
        self._grades = grades

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_age(self):
        return self._age

    def get_grades(self):
        return self._grades


class FavoriteAdapter(Student):
    def __init__(self, favorite):
        self._Favorite = favorite

    def get_full_name(self):
        return self._Favorite.get_first_name() + " " + self._Favorite.get_last_name()

    def get_contact_details(self):
        return self._Favorite.get_email()

    def is_adult(self):
        return self._Favorite.get_age() >= 18

    def get_results(self):
        return self._Favorite.get_grades()


def main():
    student1 = Student("Adam Bernau", "adam@bernau.cz", False, [1, 2, 2])
    print(f"Students full name: {student1.get_full_name()}")
    print(f"Students contact:   {student1.get_contact_details()}")
    print(f"Student is adult:   {student1.is_adult()}")
    print(f"Students results:   {student1.get_results()}")

    print('-'*80)
    favorite1 = Favorite("Bedřich", "Novák", "bedrich@novak.cz", 25, [1, 3, 2])
    print(f"Favorites first name: {favorite1.get_first_name()}")
    print(f"Favorites last name:  {favorite1.get_last_name()}")
    print(f"Favorites email:      {favorite1.get_email()}")
    print(f"Favorites age:        {favorite1.get_age()}")
    print(f"Favorites grades:     {favorite1.get_grades()}")


    print("-"*80)
    student2 = FavoriteAdapter(favorite1)
    print(f"Students full name: {student2.get_full_name()}")
    print(f"Students contact:   {student2.get_contact_details()}")
    print(f"Student is adult:   {student2.is_adult()}")
    print(f"Students results:   {student2.get_results()}")

    print("-"*80)
    student3 = FavoriteAdapter(Favorite("Cyril","novotny", "novothny@gmail.com", 17, [1, 2, 3, 4, 5, 5] ))

    print(f"Students full name: {student3.get_full_name()}")
    print(f"Students contact:   {student3.get_contact_details()}")
    print(f"Student is adult:   {student3.is_adult()}")
    print(f"Students results:   {student3.get_results()}")
    """student1 = FavoriteAdapter(Favorite("Martin", "Novák", "martin@novak.cz", 19, [1, 2, 3, 1]))
    student2 = FavoriteAdapter(Favorite("Petr", "Svoboda", "petr@svoboda.cz", 17, [2, 2, 2]))

    print(f"{'Adult' if student1.is_adult() else 'Child'}")
    print(f"Full name: {student1.get_full_name()}")
    print(f"Contact: {student1.get_contact_details()}")
    print(f"Results: {student1.get_results()}")"""


if __name__ == '__main__':
    main()