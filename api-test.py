import unittest
import requests

BASE_URL = "http://127.0.0.1:5000/posts"

class TestAPI(unittest.TestCase):

    def test_create_post(self):
        # Create a new post
        payload = {"title": "Test Post", "content": "This is a test post."}
        response = requests.post(BASE_URL, json=payload)

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)
        json_data = response.json()
        self.assertIn("id", json_data)
        self.assertEqual(json_data["title"], "Test Post")
        self.assertEqual(json_data["content"], "This is a test post.")

    def test_get_all_posts(self):
        # Get all posts
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertIsInstance(json_data, list)

    def test_get_specific_post(self):
        # Get a specific post (assuming post with ID 1 exists)
        response = requests.get(f"{BASE_URL}/1")
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data["id"], 1)


if __name__ == "__main__":
    unittest.main()
