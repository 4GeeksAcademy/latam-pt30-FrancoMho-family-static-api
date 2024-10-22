
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self.next_id = 1
        # example list of members
        self._members = [
            {"id": self._generateId(), "first_name": "Tommy", "age": 30, "lucky_numbers": [7, 13, 22], "last_name": self.last_name},
            {"id": self._generateId(), "first_name": "Michael", "age": 50, "lucky_numbers": [1, 9, 34], "last_name": self.last_name},
            {"id": self._generateId(), "first_name": "Janet", "age": 54, "lucky_numbers": [9, 21, 33], "last_name": self.last_name}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Verificar si el miembro ya tiene un ID, si no, generar uno
        if "id" not in member:
            member["id"] = self._generateId()

            # Añadir el apellido automáticamente
        member["last_name"] = self.last_name    

            # Añadir el miembro a la lista
        self._members.append(member)

        # member["first_name"] = self.first_name
        # member["age"] = self.age
        # member["lucky_numbers"] = self.lucky_numbers
        # self._members.append(member)

    def delete_member(self, id):
        member_to_delete = self.get_member(id)
        if member_to_delete:
            self._members = [m for m in self._members if m["id"] != id]
            return {"done": True}
        return {"done": False}
        

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None
      
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    

    # family_jackson = FamilyStructure("Jackson")

    # # Agregamos un miembro
    # family_jackson.add_member({
    #     "first_name": "Michael",
    #     "age": 50,
    #     "lucky_numbers": [7, 13, 22]
    # })

    # # Agregamos otro miembro
    # family_jackson.add_member({
    #     "first_name": "Janet",
    #     "age": 54,
    #     "lucky_numbers": [9, 21, 33]
    # })

    # # Ver todos los miembros
    # print(family_jackson.get_all_members())

    # # Buscar un miembro por ID
    # print(family_jackson.get_member(1))

    # # Eliminar un miembro
    # family_jackson.delete_member(1)

    # # Ver la lista actualizada de miembros
    # print(family_jackson.get_all_members())

