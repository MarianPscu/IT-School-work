class FullTimeEmployee:
    
    def __init__(self, first_name, last_name, email, gross_salary) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gross_salary = gross_salary
        self.ssm = False

    def sign_ssm(self):
        self.ssm = True

    def sign_presence(self):
        pass

    def get_net_salary(self):
        return self.gross_salary

    def pay(self):
        print(f"Amount to transfer: {self.first_name}{self.last_name}{self.get_net_salary}")

class Contractor:
    def __init__(self, first_name) -> None:
        pass

class NoTaxEmployee:
    def __init__(self, first_name) -> None:
        pass

class PartTimeEmployee:
    def __init__(self, first_name) -> None:
        pass

employes = [FullTimeEmployee("Icsulescu", "cineva", "mail@mai.com", 3000),
            Contractor("ghevcescu", "cineva", "mail@mai.com", 3000),
            PartTimeEmployee("predescu", "cineva", "mail@mai.com", 3000),
            NoTaxEmployee("maiorescu", "cineva", "mail@mai.com", 3000)

            ]