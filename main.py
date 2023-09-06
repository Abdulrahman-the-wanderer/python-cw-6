# write your code here
person = {
    "name" : "adi",
    "age" : 16,
    "hobbies" : ["reading","swimming","judo"]
}
print(person["name"])
print(person["age"])
person["age"] = 17
person["country"] = "syria"
print(len(person))
person ["hobbies"].append("mma") 
print(person)
def check_hobbies(person) :
    if len(person["hobbies"]) > 3 :
        print("you are AMAZING")
check_hobbies(person)