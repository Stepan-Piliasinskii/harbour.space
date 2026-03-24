"""Problem 03: GET request for HTML content.

Task:
1. Send GET to https://example.com
2. Print:
   - status code
   - Content-Type header
   - HTML body (response.text)
3. Verify content type contains text/html
4. Add raise_for_status()
"""

import requests

URL = "http://example.com"


def main() -> None:
    response = requests.get(URL)
    response.raise_for_status()

    content_type = response.headers.get("Content-Type", "")
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type Header: {content_type}")

    if "text/html" in content_type:
        print("\nVerified: Content-Type contains 'text/html'")

    print("\nHTML Body (truncated):")
    print(response.text[:500] + "...")


if __name__ == "__main__":
    main()
