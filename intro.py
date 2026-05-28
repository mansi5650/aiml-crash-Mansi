#Q1: extented intro

name = "mansi" 
city = "jaipur"
favorite_subject = "c"
target_role = "web developer"

student = {
    "name" : name,
    "city" : city,
    "favorite_subject" : favorite_subject,
    "target_role" : target_role

}
print(f"my name is {student['name'].title()}")
print(f"i live in {student['city'].upper()}")
print(f"my favorite_subject is {student['favorite_subject'].lower()}")
print(f"my target_role is {student['target_role'].upper()}")
