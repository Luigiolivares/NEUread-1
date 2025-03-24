import bcrypt

password = b"admin12stem7b"  # Original password
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode()

print("Save this hash:", hashed_password)