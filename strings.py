userfname= input("Fname")
userlname= input("Lname")

longstr = len(userfname + userlname)

initias = userfname[0] + userlname[0]

double_fname = ""
for letter in userfname:
    double_fname += letter + letter

revered_name = userlname[::-1]
print(revered_name)
print(f"Hello {userlname}, {userfname}! Your name has {longstr} letters, and your initials are {initias}. {double_fname}, your name spelled backwards is {revered_name}.")