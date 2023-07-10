class Student:

    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, favourite_language):
        return f"My favourite language is {favourite_language}!"
        # This can also be written as: return "I love " + language



