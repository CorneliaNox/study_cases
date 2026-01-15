# Domain Model

class User:
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def __str__(self):
    return f"User(name={self.name}, email={self.email}, password={self.password})"

  def get_first_name(self):
    return self.name.split()[0]

  def get_last_name(self):
    return self.name.split()[1]

class FriendList:
  def __init__(self, friends: list[User]):
    self.friends = friends

  def __str__(self):
    return f"FriendList(friends={self.friends})"

  def add_friend(self, friend):
    self.friends.append(friend)

  def remove_friend(self, friend):
    self.friends.remove(friend)

def main():
  friend_list = FriendList([User("Jane Doe", "jane.doe@example.com", "password")])

  friend_list.add_friend(User("John Doe", "john.doe@example.com", "password"))
  friend_list.remove_friend(User("Jane Doe", "jane.doe@example.com", "password"))

  print(friend_list)

if __name__ == "__main__":
  main()


# Anemic Domain Model

class AnemicUser:
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def __str__(self):
    return f"AnemicUser(name={self.name}, email={self.email}, password={self.password})"

class AnemicFriendList:
  def __init__(self, friends: list[AnemicUser]):
    self.friends = friends

  def __str__(self):
    return f"AnemicFriendList(friends={self.friends})"

def get_user_first_name(user: AnemicUser):
  return user.name.split()[0]

def get_user_last_name(user: AnemicUser):
  return user.name.split()[1]

def add_friend(friend_list: AnemicFriendList, friend: AnemicUser):
  friend_list.friends.append(friend)

def remove_friend(friend_list: AnemicFriendList, friend: AnemicUser):
  friend_list.friends.remove(friend)

def anemic_main():
  friend_list = AnemicFriendList([AnemicUser("Jane Doe", "jane.doe@example.com", "password")])

  add_friend(friend_list, AnemicUser("John Doe", "john.doe@example.com", "password"))
  remove_friend(friend_list, AnemicUser("Jane Doe", "jane.doe@example.com", "password"))

  print(friend_list)

if __name__ == "__main__":
  anemic_main()