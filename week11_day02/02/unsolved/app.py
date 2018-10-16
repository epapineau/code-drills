from flask import Flask, jsonify

## Create a dictionary that holds a list of students at Hogwarts and what house they belong to

hogwarts_students = [
    {"student": "Harry Potter", "house": "Gryffindor"},
    {"student": "Ron Weasley", "house": "Gryffindor"},
    {"student": "Hermione Granger", "house": "Gryffindor"},
    {"student": "Draco Malfoy", "house": "Slytherin"},
    {"student": "Luna Lovegood", "house": "Ravenclaw"},
    {"student": "Neville Longbottom", "house": "Gryffndor"},
    {"student": "Cho Chang", "house": "Ravenclaw"}
]

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Create a root route that welcomes the user with all available routes. Create an API route for each house.
## BONUS - look into HTML <a> tags and display the houses as a clickable link
@app.route("/")
def home():
    return (
        f"<h1>Welcome!</h1>"
        f"<a href = '/all'> /all </a><br/>"
        f"<a href = '/house/Gryffindor'> /house/Gryffindor </a><br/>"
        f"<a href = '/house/Slytherin'> /house/Slytherin </a><br/>"
        f"<a href = '/house/Ravenclaw'> /house/Ravenclaw </a><br/>"
        f"<a href = '/house/Hufflepuff'> /house/Hufflepuff </a><br/>"
        f"<a href = '/student/Harry Potter'> /student/Harry Potter </a><br/>"
        f"<a href = '/student/Ron Weasley'> /student/Ron Weasley </a><br/>"
        f"<a href = '/student/Hermione Granger'> /student/Hermione Granger </a><br/>"
        f"<a href = '/student/Draco Malfoy'> /student/Draco Malfoy </a><br/>"
        f"<a href = '/student/Luna Lovegood'> /student/Luna Lovegood </a><br/>"
        f"<a href = '/student/Neville Longbottom'> /student/Neville Longbottom </a><br/>"
        f"<a href = '/student/Cho Chang'> /student/Cho Chang </a><br/>")

# Create an API route that displays all students in the dictionary
@app.route("/all")
def all():
    return jsonify(hogwarts_students)

# Handle API route with a variable path that will allow getting all students from a specific house
@app.route("/house/<house_name>")
def house_match(house_name):

    house_name = house_name.replace(" ", "").lower()
    in_house = []
    for stu in hogwarts_students:
        search_term = stu["house"].replace(" ", "").lower()

        if search_term == house_name:
            in_house.append(stu['student'])
    
    if(len(in_house) == 0 and house_name != "hufflepuff"):
        return jsonify({"error": f"{house_name} is not a Hogwarts house."}), 404
    elif (house_name == "hufflepuff"):
        return jsonify(["No Students"])
    else: 
        return jsonify(in_house)
    
# Handle API route with a variable path that will allow getting info for a specific character based on their name
@app.route("/student/<student_name>")
def student_match(student_name):
    
    student_name = student_name.replace(" ", "").lower()
    for stu in hogwarts_students:
        search_term = stu["student"].replace(" ", "").lower()
        
        if search_term == student_name:
            return jsonify(stu)
        
    return jsonify({"error": f"{student_name} is not a Hogwarts student."}), 404

if __name__ == "__main__":
    app.run(debug=True)
