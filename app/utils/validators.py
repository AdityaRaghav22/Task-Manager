def validate_register(data):
    errors = {}

    if not data.get("name"):
        errors["name"] = "Name is required"

    if not data.get("email"):
        errors["email"] = "Email is required"

    if not data.get("password"):
        errors["password"] = "Password is required"
    elif len(data.get("password")) < 6:
        errors["password"] = "Password must be at least 6 characters"

    email = data.get("email", "")

    if "@" not in email or "." not in email.split("@")[-1]:
        errors["email"] = "Invalid email format"

    return errors

def validate_login(data):
    errors = {}

    if not data.get("email"):
        errors["email"] = "Email is required"

    email = data.get("email", "")
    
    if "@" not in email or "." not in email.split("@")[-1]:
        errors["email"] = "Invalid email format"
        
    if not data.get("password"):
        errors["password"] = "Password is required"

    return errors

def validate_task(data):
    errors = {}

    if not data.get("title"):
        errors["title"] = "Task title is required"

    return errors
