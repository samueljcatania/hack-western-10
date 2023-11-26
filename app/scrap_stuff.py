"""import json

byte_string = b'\n            {\n    "component": "flashcard",\n    "info": [\n        {\n            "unit_name": "Circular Motion",\n            "topic": "Uniform Circular Motion",\n            "question": "What is the definition of uniform circular motion?",\n            "answer": "Uniform circular motion is a type of motion in which an object moves in a circle at constant speed with constant direction of motion."\n        },\n        {\n            "unit_name": "Circular Motion",\n            "topic": "Centripetal Acceleration",\n            "question": "What is the formula for centripetal acceleration?",\n            "answer": "Centripetal acceleration is given by the equation a = v\xc2\xb2/r, where a is the centripetal acceleration, v is the tangential velocity, and r is the radius of the circle."\n        },\n        {\n            "unit_name": "Circular Motion",\n            "topic": "Centripetal Force",\n            "question": "What is the formula for centripetal force?",\n            "answer": "Centripetal force is given by the equation F = mv\xc2\xb2/r, where F is the centripetal force, m is the mass of the object, v is the tangential velocity, and r is the radius of the circle."\n        },\n        {\n            "unit_name": "Circular Motion",\n            "topic": "Angular Acceleration",\n            "question": "What is the formula for angular acceleration?",\n            "answer": "Angular acceleration is given by the equation \xce\xb1 = \xce\x94\xcf\x89/\xce\x94t, where \xce\xb1 is the angular acceleration, \xce\x94\xcf\x89 is the change in angular velocity, and \xce\x94t is the change in time."\n        },\n        {\n            "unit_name": "Circular Motion",\n            "topic": "Angular Momentum",\n            "question": "What is the formula for angular momentum?",\n            "answer": "Angular momentum is given by the equation L = I\xcf\x89, where L is the angular momentum, I is the moment of inertia, and \xcf\x89 is the angular velocity."\n        },\n        {\n            "unit_name": "Circular Motion",\n            "topic": "Centripetal Force",\n            "question": "What is the direction of the centripetal force?",\n            "answer": "The centripetal force always acts in the direction towards the center of the circle."\n        },\n        {\n            "unit_name": "Circular Motion",\n            "topic": "Centripetal Force",\n            "question": "What is the relation between centripetal force and centripetal acceleration?",\n            "answer": "The centripetal force is equal to the mass times the centripetal acceleration, i.e. F = ma."\n        },\n        {\n            "unit_name": "Circular Motion",\n            "topic": "Angular Velocity",\n            "question": "What is the relationship between angular velocity and linear velocity?",\n            "answer": "The linear velocity is equal to the angular velocity times the radius of the circle, i.e. v = \xcf\x89r."\n        },\n        {\n            "unit_name": "Circular Motion",\n            "topic": "Uniform Circular Motion",\n            "question": "What is the equation for the period of uniform circular motion?",\n            "answer": "The period of uniform circular motion is given by the equation T = 2\xcf\x80r/v, where T is the period, r is the radius of the circle, and v is the tangential velocity."\n        },\n        {\n            "unit_name": "Circular Motion",\n            "topic": "Centripetal Force",\n            "question": "What is the source of centripetal force?",\n            "answer": "The centripetal force is provided by an external force, such as gravity, tension, friction, or a centripetal force that is generated by the object itself."\n        }\n    ]\n}'
# Step 1: Parse the Byte String
# Convert byte string to regular string and then parse JSON
data = json.loads(byte_string)

# Step 2: Organize and Display the Data
for flashcard in data['info']:
    print(f"Unit Name: {flashcard['unit_name']}")
    print(f"Topic: {flashcard['topic']}")
    print(f"Question: {flashcard['question']}")
    print(f"Answer: {flashcard['answer'].encode('utf-8')}")


    
    print("\n")  # Adds a newline for better readability between flashcards
"""
import requests
import json

def getCourses():
    # Define the API endpoint URL
    api_url = 'http://127.0.0.1:3000/users/retrieveEnrolled'  # Replace with the actual API endpoint URL

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON data
            data = response.json()
            print(data)
            return data  # You can now work with the data
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")



getCourses()