class User:
    def __init__(self, id, name, lastname, age, email, phone, garden, password):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email
        self.phone = phone
        self.garden = garden
        self.password = password  # Almacenar la contraseña en texto plano

    def check_password(self, password):
        return self.password == password  # Comparar en texto plano