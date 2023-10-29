people = [
{"name" : "balu", "collage" : "sreenidhi"},
{"name" : "sam", "collage" : "idk"},
{"name" : "akhil", "collage" : "nitk"}
]
def f(person):
    return person["collage"]
people.sort(key=f)
print(people)
# // or
people.sort(key=lambda person: person["name"])
print(people)