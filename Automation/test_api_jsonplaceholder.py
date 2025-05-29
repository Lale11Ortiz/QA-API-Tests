import unittest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestJSONPlaceholderAPI(unittest.TestCase):

    def test_get_all_posts(self):
        response = requests.get(f"{BASE_URL}/posts")
        self.assertEqual(response.status_code, 200)
        print("✅ GET all posts → OK")

if __name__ == "__main__":
    unittest.main()
    def test_get_single_post(self):
        response = requests.get(f'{BASE_URL}/posts/1')
        self.assertEqual(response.status_code, 200)
        print("✅ GET single post ➜ OK")
    def test_create_new_post(self):
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = requests.post(f'{BASE_URL}/posts', json=payload)
        self.assertEqual(response.status_code, 201)
        print("✅ POST create new post → OK")
    def test_update_post(self):
        payload = {
            "id": 1,
            "title": "updated title",
            "body": "updated body",
            "userId": 1
        }
        response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=payload)
        self.assertEqual(response.status_code, 200)
        print("✅ PUT update post → OK")

    def test_partial_update_post(self):
        payload = {
            "title": "patched title"
        }
        response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=payload)
        self.assertEqual(response.status_code, 200)
        print("✅ PATCH partial update → OK")

    def test_delete_post(self):
        response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
        self.assertEqual(response.status_code, 200)
        print("✅ DELETE post → OK")