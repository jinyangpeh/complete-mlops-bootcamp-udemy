from pydantic import BaseModel

'''
Pydantic:
- Is a parsing library
- Guarantees the types and constraints of the output model
- Can also be used fo custom validation as well
'''

data = {
    "name": "Murthy",
    "age": "28",
    "course": "MLOps BootCamp",
    "ratings": [4, 4, "4", "5", 4]
}

class Instructor(BaseModel):
    name: str
    age: int
    course: str
    ratings: list[int] = []


user = Instructor(**data)

print(f"Found a Instructor: {user}")