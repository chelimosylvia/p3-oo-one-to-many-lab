class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type.lower() not in self.PET_TYPES:
            raise Exception(f"Invalid pet type. Allowed types are: {', '.join(self.PET_TYPES)}")
        self.name = name
        self.pet_type = pet_type.lower()
        self.owner = owner
        self.__class__.all_pets.append(self)

    @classmethod
    def all(cls):
        return cls.all_pets

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Only instances of Owner class can be set as owner.")
        self.owner = owner
pass

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet class can be added as pets.")
        self._pets.append(pet)
        pet.set_owner(self)

    def get_sorted_pets(self):
        sorted_pets = sorted(self._pets, key=lambda x: x.name)
        return sorted_pets
pass