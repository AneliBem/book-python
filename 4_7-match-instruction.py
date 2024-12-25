from os import system
system("pip3 install requests")

import requests

def check_website(url):
    try:
        response = requests.get(url)
        status = response.status_code  # Отримуємо HTTP-статус
        match status:
            case 200:
                return "The page is OK (200)"
            case 404:
                return "Page not found (404)"
            case 500:
                return "Server error (500)"
            case _:
                return f"Unhandled HTTP status: {status}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Використання функції
url = "https://www.google.com.ua/"
print(check_website(url))
