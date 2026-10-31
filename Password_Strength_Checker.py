def password_strength(pw):
    if pw in [" ",""]:
        return("Invalid")
    elif  pw.lower() in ["password", "12345678", "qwertyui", "letmein1"]:
        return("Weak")


