NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3


HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2

def main():
    people_dict = {
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriages_dict = {
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    print_death_age(people_dict)

    print()

    count_genders(people_dict)

    print()

    print_marriages(marriages_dict, people_dict)


def print_death_age(people_dict):
    for i in people_dict:
        person = people_dict[i]
        name = person[NAME_INDEX]
        age = person[DEATH_YEAR_INDEX]- person[BIRTH_YEAR_INDEX]
        print(F"Name: {name}, Age of death: {age}")


def count_genders(people_dict):
    men = 0
    women = 0
    for i in people_dict:
        individual = people_dict[i]
        if individual[GENDER_INDEX] == "M":
            men += 1
        else:
            women += 1
    print("Number of men and women: ")
    print(f"Men: {men}")
    print(f"Women: {women}")
    

def print_marriages(marriages_dict, people_dict):
    for i in marriages_dict:
        wedding = marriages_dict[i]
        husband_key = wedding[HUSBAND_KEY_INDEX]
        wife_key = wedding[WIFE_KEY_INDEX]
        wedding_year = wedding[WEDDING_YEAR_INDEX]
        
        husband = people_dict[husband_key]
        wife = people_dict[wife_key]
        
        h_name = husband[NAME_INDEX]
        w_name = wife[NAME_INDEX]
        
        husband_age = wedding_year - husband[BIRTH_YEAR_INDEX]
        wife_age = wedding_year - wife[BIRTH_YEAR_INDEX]
        
        print(f"Husband's name: {h_name}, Age at wedding: {husband_age} , Wife's name: {w_name}, Age at wedding: {wife_age}, Year of wedding: {wedding_year}")


if __name__ == "__main__":
    main()