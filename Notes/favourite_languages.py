""" favouriteLanguages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Ruby',
    'phil': 'Python',
    'ssmtpd': 'C',
}

friends = ['edward', 'ssmtpd']
for name in favouriteLanguages.keys():
    print(name.title())
    if name in friends:
        print(" Hello " + name.title() + ". I see your favorite language is " + favouriteLanguages[name].title() + ".")

if 'erin' not in favouriteLanguages.keys():
    print("Erin, please take our poll!\n\n")

for name in sorted(favouriteLanguages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in sorted(set(favouriteLanguages.values())): # or for language in set(sorted(favouriteLanguages.values())):
    print(language.title())

# print("Sarah's favorite language is " +
#     favouriteLanguages['sarah'].title() +
#     ".")

for name, language in favouriteLanguages.items():
    print(name.title() + "'s favourite language programming is " + language.title() + ".")

for name1 in favouriteLanguages.keys(): # or for name1 in favouriteLanguages:
    print(name1.title())

for language1 in favouriteLanguages.values():
    print(language1.title()) """

favouriteLanguages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    'ssmtpd': ['c', 'c++'],
}

for name, languages in favouriteLanguages.items():
    print("\n" + name.title() + "'s favourite language programming are:")
    for x in languages:
        print("\t" + x.title())
