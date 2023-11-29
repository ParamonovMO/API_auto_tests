import requests

class Test_new_location:
    """Работа с новой локацией"""
    def test_create_new_location(self):
        """Создаение новой локации"""
        
        base_url = 'https://rahulshettyacademy.com' #базовый урл
        post_resurce = '/maps/api/place/add/json' #ручка
        key = '?key=qaclick123' #ключ авторизации
        
        post_url = base_url + post_resurce + key
        print(post_url)
        
        body_json = {"location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
            
        }
        result_post = requests.post(post_url, json =body_json)
        print(result_post.text)
        print("Статус код:", result_post.status_code)
        assert 200 == result_post.status_code
        print("Успешно!!! Мы создали новое место")
        if result_post.status_code != 200:
            print("Провал!!! Запрос ошибочный")
        
        check_post = result_post.json()
        check_info_post = check_post.get('status')
        print('Статус ответа:', check_info_post)
        assert check_info_post == 'OK'
        print("Статус код верный")
        
        place_id = check_post.get('place_id')
        print('ID места:', place_id)
        
        
        """Проверка создания новой локации"""
        get_resourse = '/maps/api/place/get/json'
        get_url = base_url + get_resourse + key + '&place_id=' + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Статус код:", result_post.status_code)
        assert 200 == result_get.status_code
        print("Проверка создания новой локации прошла успешно")
        if result_get.status_code != 200:
            print("Провал!!! Запрос ошибочный")
        
        
        
new_place = Test_new_location()
new_place.test_create_new_location()
