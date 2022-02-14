'''
`A class should have one, and only one reason to change.`

This means when we design our classes, we need to ensure that our class is responsible 
only for 1 task or functionality and when there is a change in that task/functionality, 
only then, that class should change.

https://www.geeksforgeeks.org/single-responsibility-principle-in-java-with-examples/

'''


#  This is the basic example of single responsibility class
from fileinput import filename


class Journal:
    def __init__(self) -> None:
        self.notes = []
        self.count = 0

    def add_note(self, note):
        self.count += 1
        self.notes.append(f'{self.count}. {note}')

    def __str__(self) -> str:
        return "\n".join(self.notes)


j = Journal()
j.add_note('I am eating')
j.add_note('I have to complete solid design pattern')
print(f" The notes are : \n {j}")

#  I want to add some other responsibility to this class but this is not the best practice
# uploading ,loading ,reading are the different responsibility


class Journal:
    def __init__(self) -> None:
        self.notes = []
        self.count = 0

    def add_note(self, note):
        self.count += 1
        self.notes.append(f'{self.count}. {note}')

    def __str__(self) -> str:
        return "\n".join(self.notes)

    def save(self, fine_name):
        file = open(fine_name, 'w')
        file.write(str("\n".join(self.notes)))
        file.close()

    def load(self, fine_name):
        with open(fine_name, 'r') as file:
            for line in file.readlines():
                print(line)

    def load_from_url(self, url):
        pass


j = Journal()
j.add_note('I am eating')
j.add_note('I have to complete solid design pattern')
print(f" The notes are : \n {j}")
j.save('notes.txt')
j.load('notes.txt')


# I want to develop single responsibility principle in this code, want to seperate the responsibility



class Journal:
    def __init__(self) -> None:
        self.notes = []
        self.count = 0

    def add_note(self, note):
        self.count += 1
        self.notes.append(f'{self.count}. {note}')

    def __str__(self) -> str:
        return "\n".join(self.notes)

class PersistanceManager:
    @staticmethod
    def save(self, fine_name):
        file = open(fine_name, 'w')
        file.write(str("\n".join(self.notes)))
        file.close()

    @staticmethod
    def load(self, fine_name):
        with open(fine_name, 'r') as file:
            for line in file.readlines():
                print(line)

    @staticmethod
    def load_from_url(self, url):
        pass


j = Journal()
j.add_note('I am eating')
j.add_note('I have to complete solid design pattern')
print(f" The notes are : \n {j}")
PersistanceManager.save(j,'notes.txt')
PersistanceManager.load(j,'notes.txt')
