"""Problem 07 (part B): messenger sender client.

Task:
1. Split into pairs
2. Write an infinite loop reading message text from terminal
3. Send each message to partner API endpoint /messages
4. Show send status in terminal


Partner setup:
- Partner gives you ngrok public URL
- You set TARGET_BASE_URL to that URL
"""

import requests

TARGET_BASE_URL = "https://replace-with-partner-ngrok-url"
SENDER_NAME = "replace-with-your-name"


def main() -> None:
    print(f"Messenger Client started as {SENDER_NAME}")
    print("Type your message and press Enter (or 'exit' to quit):")

    while True:
        try:
            text = input("> ")
            if text.lower() in ("exit", "quit"):
                break

            if not text.strip():
                continue

            payload = {
                "user": SENDER_NAME,
                "text": text
            }

            response = requests.post(f"{TARGET_BASE_URL}/messages", json=payload)
            response.raise_for_status()
            print(f"Sent! Response: {response.json()}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
