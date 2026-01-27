import requests

def fetch_and_display_users(num_users):
    """
    Fetches users from JSONPlaceholder API and displays
    name, email, and city for the first num_users users.

    Returns None if an error occurs.
    """
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)

        # Handle non-200 status codes
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return None

        users = response.json()

        # Ensure response is a list
        if not isinstance(users, list):
            print("Error: Unexpected JSON structure.")
            return None

        for i, user in enumerate(users[:num_users], start=1):
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]

                print(f"{i}. Name: {name}")
                print(f"   Email: {email}")
                print(f"   City: {city}")
            except KeyError as e:
                print(f"Error: Missing expected key {e} in user data.")
                return None

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None


# Example calls
fetch_and_display_users(3)
print("-" * 40)
fetch_and_display_users(15)
