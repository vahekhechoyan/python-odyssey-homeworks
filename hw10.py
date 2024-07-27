# 1
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# 2
user_data = []

while True:
    print("Enter user details:")
    ID = int(input("ID: "))
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = input("Password: ")
    phone = input("Phone: ")

    user_data.append({"ID": ID, "first_name": first_name, "last_name": last_name, "email": email, "password": password, "phone": phone})

    more_data = input("Do you want to add another user? (yes/no): ")
    if more_data.lower() != 'yes':
        break

user_dict = {}
user_list = []

for user in user_data:
    user_id = user["ID"]
    user_dict[user_id] = user
    user_list.append(user)

search_first_name = input("Enter the first name to search in the list: ")
search_last_name = input("Enter the last name to search in the list: ")
user_found = False

for user in user_list:
    if user["first_name"] == search_first_name and user["last_name"] == search_last_name:
        print("User found in list:")
        print(f"ID: {user['ID']}")
        print(f"First Name: {user['first_name']}")
        print(f"Last Name: {user['last_name']}")
        print(f"Email: {user['email']}")
        print(f"Password: {user['password']}")
        print(f"Phone: {user['phone']}")
        user_found = True
        break

if not user_found:
    print("Not found")

search_id = int(input("Enter the ID to search in the dictionary: "))

if search_id in user_dict:
    user = user_dict[search_id]
    print("User found in dictionary:")
    print(f"ID: {user['ID']}")
    print(f"First Name: {user['first_name']}")
    print(f"Last Name: {user['last_name']}")
    print(f"Email: {user['email']}")
    print(f"Password: {user['password']}")
    print(f"Phone: {user['phone']}")
else:
    print("Not found in dictionary")