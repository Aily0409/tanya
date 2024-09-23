#Homo list

integers = [1,2,3,8,33]

animals = ["dog", "cat", "goat"]

names = ["Artemis", "Bucky", "Sebastian"]

floats = [2.2, 4.9, 5.5, 9.8, 18.7]

#Hetero list

numbers_animals_names = [2, "cat", 34.33, "Aily"]

list_of_lists = [[1,2,3,], ["Cats", "dog", "cow"]]

#How to acces an element in a list

list = [3, 3, 30, 5.3, 28]

print (list[3])

random_words = [ "apple", "bicycle", "cloud", "dolphin", "echo",
    "forest", "guitar", "honey", "iceberg", "jelly",
    "kite", "lemon", "mountain", "notebook", "ocean",
    "panda", "quokka", "rainbow", "snowflake", "tiger",
    "umbrella", "violin", "whale", "xylophone", "yacht",
    "zipper", "almond", "basket", "candle", "dream",
    "ember", "feather", "galaxy", "harmony", "island",
    "journey", "key", "lantern", "mirror", "nest",
    "olive", "pomegranate", "quilt", "rose", "starfish",
    "treasure", "unicorn", "vase", "windmill", "zucchini",
    "acorn", "breeze", "castle", "dragon", "emerald",
    "firefly", "grapes", "hedgehog", "icicle", "jungle",
    "kaleidoscope", "lighthouse", "meadow", "noodle", "octopus",
    "pumpkin", "quasar", "river", "sandcastle", "tapestry",
    "umbra", "volcano", "waffle", "yawn", "zest",
    "almond", "biscuit", "cactus", "daisy", "echo",
    "fable", "goblet", "harmony", "igloo", "jigsaw",
    "kingdom", "lantern", "mosaic", "nectar", "oasis",
    "petal", "quartz", "riddle", "saffron", "tundra",
    "utensil", "velvet", "whisper", "zenith", "acorn",
    "blueberry", "cinnamon", "dandelion", "eclipse", "fern",
    "glimmer", "horizon", "inkling", "jubilee", "kale",
    "lullaby", "mirth", "nymph", "opal", "palette",
    "quiver", "raccoon", "silhouette", "tonic", "utopia",
    "vortex", "willow", "x-ray", "yarn", "zephyr",
    "amethyst", "blossom", "cloudberry", "dewdrop", "enigma",
    "firework", "grapefruit", "honeycomb", "ibis", "jackal",
    "kettle", "locket", "mirage", "nautilus", "oasis",
    "pineapple", "quinoa", "rhapsody", "stargazer", "tidal",
    "ukulele", "vanilla", "whisk", "xenon", "yonder",
    "zinnia", "apricot", "breeze", "chipmunk", "dusk",
    "echo", "fig", "glade", "hummingbird", "iris",
    "joyful", "kaleidoscope", "lantern", "meadow", "nightingale",
    "oregano", "petunia", "quokka", "rivulet", "seashell",
    "tapestry", "umbrella", "violette", "whimsy", "xylophone",
    "yucca", "zucchini", "atlas", "blossom", "chameleon",
    "driftwood", "ember", "fern", "glint", "harbor",
    "indigo", "joy", "kestrel", "lantern", "meadowlark",
    "nimbus", "opalescent", "pansy", "quasar", "ripple",
    "saffron", "twilight", "umami", "velvet", "wanderlust"]

print (random_words[-1])

#List slicing

list = [3, 3, 30, 5.3, 28]

print(list[:])

print(list[1:3])

print(list[1:4])

print(list[2:-1])

#Update a list

science = ["art", "chemistry", "math"]

science [0] = "biology"

print(science)

print(science[0])

science [-1] = "geology"

print (science)

print(science[-1])

integers=[2,3,4,6,7]

integers [3] = 5

print(integers)

integers [4] = 6

print(integers)

#How to delete an element from the list

integers.remove(4)

print(integers)

integers.pop()

print(integers)

fruit_list = ["strawberry", "grapes", "peach"]

del fruit_list[1]

print(fruit_list)

list_of_names= ["Adonis", "Lyra", "Alexis", "Orion"]

list_of_names.append("Artemis")

print(list_of_names)