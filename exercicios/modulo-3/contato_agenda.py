class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def display_contacts(self):
        if not self.contacts:
            print("Lista de Contatos vazia.")
        else:
            for contact in self.contacts:
                print(contact)
                print("----------------------")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return contact
        print("Contato não encontrado.")
