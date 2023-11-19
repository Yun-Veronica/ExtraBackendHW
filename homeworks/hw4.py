user_dict = {}


# Email: {Name:Name, Surname:Surname, Age:Age, Address:Address, Username:Username, Password:Password}
def check_email(user_dict, email):
    if email in user_dict:
        return False
    return True


def check_password(password):
    if len(password) < 8:
        return False
    return True


def create_user(user_dict: dict):
    user_params = ['Name', 'Surname', 'Age', 'Address', 'Username', 'Password', 'Email']
    user = {}

    for i in user_params:
        param = input(f"Input {i}: ")
        if i == "Password" and not check_password(param):
            while not check_password(param):
                print("Password should be longer.")
                param = input(f"Input {i} (at least 8 symbols): ")

        elif i == "Email" and not check_email(user_dict, param):
            while not check_email(user_dict, param):
                print('Email should be unique.')
                param = input(f"Input {i}. Must be unique: ")

        if i != "Email":
            user.setdefault(i, param)
        else:
            email = param
            user.setdefault(i, param)
            user_dict.setdefault(email, user)
    return "Success"


def show_users(user_dict: dict):
    for i in user_dict:
        user_params = ['Name', 'Surname', 'Age', 'Address', 'Username', 'Password', 'Email']
        for k in user_params:
            print(f"{k}: {user_dict[i][k]}")

    return user_dict


def change_params(user_dict: dict):
    email = input("Input Email: ")
    if user_dict.get(email) == None:
        return "Invalid Email"
    user_params = ['Name', 'Surname', 'Age', 'Address', 'Username', 'Password', 'Email']
    param_index = input("Input index (from 1 to 5): ")
    if param_index.isdigit() and (param_index < "6" and param_index >= "1"):
        index = int(param_index)
        opt = user_params[index - 1]
        input_ = input(f"Input desired value of {opt}: ")
        user_dict[email][opt] = input_
    else:
        return "Invalid Data. Start again"


def delete_user(user_dict: dict):
    email = input("Input Email: ")
    if user_dict.get(email) != None:
        del user_dict[email]
    else:
        return "Start Again"
    return "Successful"


def login(user_dict: dict):
    email = input("Input Email: ")
    password = input("Input Password:")
    if user_dict.get(email) != None and user_dict[email]["Password"] == password:
        return "Successful Authorization"
    return "Invalid password or Email. Start Again"


def user_options(user_dict):
    options = ["Cretae User", "Show list of all Users", "Delete User", "Login", "Exit"]
    print("Choose one option from list. Input ony one num from 1 to 5: ")
    for i in range(1, 6):
        print(f"{i}.{options[i - 1]}")

    user_opt = input()
    if user_opt.isdigit() and (user_opt < "6" and user_opt >= "1"):
        user_opt = int(user_opt)
        match user_opt:
            case 1:
                return create_user(user_dict)

            case 2:
                show_users(user_dict)
                return True

            case 3:
                return delete_user(user_dict)

            case 4:
                return login(user_dict)

            case 5:
                return False


while True:
    x = user_options(user_dict)
    if not x:
        print("Bye!")
        break

    print(x)
