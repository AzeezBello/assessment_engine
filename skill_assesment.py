# def get_input():
#     print("Enter your age :")
#     age = int(input())

#     print("Enter your CGPA :")
#     grade = int(input())

#     print("Enter your Education level :--->[postgrad, undergrad, olevel]")
#     education_level = input()

#     print("Enter your enrollment_status  :")
#     enrollment_status = input()

#     return age, grade, education_level, enrollment_status

def assessment_score():
    score = 0
    print("Enter your age :")
    age = int(input())

    print("Enter your CGPA :--->[1, 2, 3, 4, 5]")
    grade = int(input())

    print("Enter your Education level :--->[postgrad, undergrad, olevel]")
    education_level = input()

    print("Enter your enrollment_status  :--->[enrolled, not-enrolled]")
    enrollment_status = input()

    if age <= 18:
        score += 10
    elif age <= 28:
        score += 5
    else:
        score += 1
    
    

    if education_level == "postgrad":
        score += 10
    elif education_level == "undergrad":
        score += 8
    elif education_level == "olevel":
        score += 5
    else:
        score += 1

    if enrollment_status == "enrolled":
        score += 10
    else:
        score += 1


    if grade >= 4:
        score += 10
    elif grade >= 2:
        score += 5
    else:
        score += 1


    print(f"Your assessment score is {score}/100")

assessment_score()

# print("Enter your name :")
# name = input()

# print("Enter your age :")
# age = input()

# print("Enter your CGPA :")
# cgpa = input()

# print("Enter your Education  :")
# education_level =input()

# print("Enter your enrollment_status  :")
# enrollment_status = input()

