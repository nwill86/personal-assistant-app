# Import the necessary modules
from flask import Flask, request

app = Flask(__name__)

# Initialize an empty list to store to-do items
todos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle form submission (add a to-do)
        user_command = request.form.get("user_command")
        if user_command:
            todos.append(user_command)
            return "To-do added successfully!"
        else:
            return "Invalid input. Please enter a to-do."
    else:
        # Display the form (get to-do list)
        return """
        <form method="post">
            <label for="user_command">How can I help you?</label>
            <input type="text" name="user_command" id="user_command">
            <input type="submit" value="Submit">
        </form>
        <p>To-dos: {}</p>
        """.format(", ".join(todos))

if __name__ == "__main__":
    app.run(debug=True)
