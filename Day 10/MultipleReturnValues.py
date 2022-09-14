def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    f_name.title()
    l_name.title()
    return f"{f_name} {l_name}"


f_name = input("What is your first name? ")
l_name = input("What is your last name? ")
print(format_name(f_name, l_name))