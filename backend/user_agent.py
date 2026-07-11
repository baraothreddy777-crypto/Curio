# Read the profile from the file instead of asking for input
with open("user_profile.txt", "r") as f:
    lines = f.readlines()

# Extract the values (stripping away labels like "Name: ")
name = lines[0].replace("Name: ", "").strip()
email = lines[1].replace("Email: ", "").strip()
topics = lines[2].replace("Topics: ", "").strip()
frequency = lines[3].replace("Frequency: ", "").strip()
preferences = lines[4].replace("Preferences: ", "").strip()

print("User profile loaded automatically!")