from pyscript import document

def generate_message():
    output_div = document.getElementById("output")
    output_div.innerText = ""  # clear old content

    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value
    final = f"Hello {name}!\nYou're currently {age} years old.\nYou go to {school}!\nThis information was made with HTML and Python Script."

    message = f"""
    Student Profile
    -----------------
    Name: {name}
    Age: {age}
    School: {school}

    {final}
    """

    output_div.innerText = message
