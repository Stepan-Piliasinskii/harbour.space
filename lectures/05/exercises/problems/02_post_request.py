"""Problem 02: POST request to JSONPlaceholder.

Task:
1. Send POST to https://jsonplaceholder.typicode.com/posts
2. Send JSON payload with fields: title, body, userId
3. Print:
   - status code
   - raw body
   - parsed JSON
4. Confirm response includes your data + id

Note: JSONPlaceholder simulates writes; data is not truly persisted.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def main() -> None:
    payload = {
        "title": "Sample Title",
        "body": "Sample body text",
        "userId": 101
    }

    response = requests.post(URL, json=payload)
    response.raise_for_status()

    print(f"Status Code: {response.status_code}")
    print("\nRaw Body:")
    print(response.text)

    print("\nParsed JSON:")
    data = response.json()
    print(data)

    if data.get("title") == payload["title"] and "id" in data:
        print("\nResponse confirms post creation with generated ID.")


if __name__ == "__main__":
    main()
