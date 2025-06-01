import pytest
import requests

# Fixture con la URL base
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


def test_get_all_posts(base_url):
    response = requests.get(f"{base_url}/posts")
    print("✅ GET all posts →", response.status_code)
    assert response.status_code == 200


def test_get_specific_post(base_url):
    response = requests.get(f"{base_url}/posts/1")
    print("✅ GET specific post →", response.status_code)
    assert response.status_code == 200


def test_create_new_post(base_url):
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{base_url}/posts", json=payload)
    print("✅ POST create →", response.status_code)
    assert response.status_code == 201


def test_update_post_put(base_url):
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(f"{base_url}/posts/1", json=payload)
    print("✅ PUT update →", response.status_code)
    assert response.status_code == 200


def test_partial_update_patch(base_url):
    payload = {
        "title": "patched title"
    }
    response = requests.patch(f"{base_url}/posts/1", json=payload)
    print("✅ PATCH partial update →", response.status_code)
    assert response.status_code == 200


def test_delete_post(base_url):
    response = requests.delete(f"{base_url}/posts/1")
    print("✅ DELETE →", response.status_code)
    assert response.status_code == 200