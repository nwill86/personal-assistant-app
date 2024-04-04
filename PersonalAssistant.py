class PersonalAssistant:

  def __init__(self, todos, birthdays, contacts):
    self.todos = todos
    self.birthdays = birthdays
    self.contacts = contacts

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
     
      index = self.todos.index(todo_item)
     
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todos(self):
    return self.todos

  def get_birthdays(self):
    return self.birthdays

  def get_birthday(self, name):
    return f"{name}'s birthday is on {self.birthdays[name]}."

  def add_birthday(self, name, date):
    if name in self.birthdays:
      print(f"{name}'s birthday already exists!")
    else:
      self.birthdays[name] = date
      print(f"Added {name}'s birthday.")
    
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name!"

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      return f"{name}'s birthday was removed."
    else:
      return "Sorry, that person does not exist and couldn't be removed."

  def add_contact(self, name, title):
    if name in self.contacts:
      print(f"{name}'s contact already exists!")
    else:
      self.contacts[name] = title
      print(f"Added {name}'s contact.")

  def get_contacts(self):
    return self.contacts

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name)
      return f"{name}'s contact was removed."
    else:
      return "Sorry, that person does not exist and couldn't be removed."

