class Student:
    def __init__(self, jmeno, prijmeni, hodnoceni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.hodnoceni = hodnoceni


class Teacher:
    def __init__(self, jmeno, predmet):
        self.jmeno = jmeno
        self.predmet = predmet
        self.hodnoceni = []

    def pridat_hodnoceni(self, hodnoceni):
        self.hodnoceni.append(hodnoceni)

class Student:
    def __init__(self, jmeno, prijmeni, hodnoceni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.hodnoceni = hodnoceni
        self.predmet = None  # Přidáme atribut předmět, inicializovaný na None

    def pridat_predmet(self, predmet):
        self.predmet = predmet


class Teacher:
    def __init__(self, jmeno, predmet):
        self.jmeno = jmeno
        self.predmet = predmet
        self.hodnoceni = []

    def pridat_hodnoceni(self, hodnoceni):
        self.hodnoceni.append(hodnoceni)


student1 = Student("Jan", "Novák", [90, 85, 88])
student1.pridat_predmet("Matematika")

ucitel = Teacher("Pan Ucitel", "Matematika")
ucitel.pridat_hodnoceni(92)
ucitel.pridat_hodnoceni(87)

print(f"Student {student1.jmeno} {student1.prijmeni} studuje předmět {student1.predmet} a má hodnocení {student1.hodnoceni}.")
print(f"Učitel {ucitel.jmeno} vyučuje předmět {ucitel.predmet} a udělil hodnocení {ucitel.hodnoceni}.")
