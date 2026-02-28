import json
import requests
import sys

# Configuration
API_ENDPOINT = "https://YOUR_API_ENDPOINT_HERE/posts"

def publish_blog_post(article_data):
    """
    Publishes a blog post to the API (Step 4 & 5).
    """
    print(f"Publishing article: '{article_data.get('blog_title', 'Unknown Title')}'...")

    try:
        # Step 4: Post to the API
        response = requests.post(
            API_ENDPOINT,
            headers={"Content-Type": "application/json"},
            json=article_data
        )

        # Step 5: Confirm Success
        if response.status_code in (200, 201):
            print(f"✅ Your blog post '{article_data.get('blog_title')}' has been published successfully.")
        else:
            print(f"❌ Failed to publish. API returned status code: {response.status_code}")
            print(f"Error details: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred while connecting to the API: {e}")

if __name__ == "__main__":
    # Accept JSON from file path or from stdin (no args or "-")
    if len(sys.argv) > 1 and sys.argv[1] != "-":
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            publish_blog_post(data)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error: File '{file_path}' does not contain valid JSON.")
    else:
        # Read JSON from stdin
        try:
            data = json.load(sys.stdin)
            publish_blog_post(data)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON on stdin: {e}")
