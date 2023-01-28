import requests


URL = 'https://petstore.swagger.io/v2/'
new_pet = {
  "id": 179534685,
  "category": {
    "id": 93,
    "name": "Dog"
  },
  "name": "doggie795",
  "photoUrls": [
    "NoPhotos"
  ],
  "tags": [
    {
      "id": 0,
      "name": "testing"
    }
  ],
  "status": "available"
}


def test_add_pet():
    response = requests.post(url=URL + 'pet', json=new_pet)
    assert response.status_code == 200


def test_added_pet():
    added_pet = requests.get(url=URL + 'pet/' + str(new_pet['id']))
    assert added_pet.status_code == 200
    assert added_pet.json()['name'] == 'doggie795'


def test_delete_pet():
    delete_pet = requests.delete(url=URL + 'pet/' + str(new_pet['id']))
    assert delete_pet.status_code == 200
