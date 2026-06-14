from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    #name: str
    age: Optional[int] = None  # default value for age field

    # default value for name field
    name: str = 'Rohit'

    # We can use the EmailStr type from Pydantic to specify that the email field must be a valid email address, and it will automatically validate the input and raise an error if the provided value is not a valid email address.
    email: EmailStr

    # Field allows us to specify additional validation rules for the fields, such as minimum and maximum values, regex patterns, and more. In this case, we are using Field to specify that the cgpa field must be a float between 0 and 10.
    cgpa: float = Field(gt=0, lt=10, description="The CGPA of the student, must be between 0 and 10")  # gt=0 means greater than 0, lt=10 means less than 10

# new_student = {'name':"John"}
# new_student = {'age':20}

new_student = {'age':'20'} #  pydantic is very smart and can handle type conversions like this, so it will successfully create a Student instance with the age field set to the integer value 20, even though we provided it as a string in the input dictionary.

#new_student = {'age':'20', 'email':'john'} # error because the email field is required and must be a valid email address, and 'john' does not meet these criteria. Pydantic will raise a validation error indicating that the email field is missing or invalid.

#new_student = {'age':'20', 'email':'john@example.com'} # this will work because the email field is provided and is a valid email address.

new_student = {'age':'20', 'email':'john@example.com', 'cgpa':8.5}

student = Student(**new_student)

# print(student)
# print(type(Student))

# student_dict = student.dict()  # convert the Student instance to a dictionary
# print(student_dict['name'])  # access the name field from the dictionary representation of the Student instance
# print(student_dict['age'])  # access the age field from the dictionary representation of the Student instance
# print(student_dict['email'])  # access the email field from the dictionary representation of the Student instance

student_json = student.model_dump_json()  # convert the Student instance to a JSON string
print(student_json)