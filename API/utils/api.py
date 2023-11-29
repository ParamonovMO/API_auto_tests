from utils import http_methods


"""Методы для тестирования Google_maps_api"""
base_url = 'https://rahulshettyacademy.com'  #базовый url
key = '?key=qaclick123' #параметр - ключ

class Google_maps_api:
  """Метод для создания новой локации"""
  @staticmethod
  def create_new_place():
    post_resourse = '/maps/api/place/add/json' #ресурс метода post
    json_for_create_new_place = {"location": 
                                 {"lat": -38.383494, 
                                  "lng": 33.427362 
                                 }, 
                                 "accuracy": 50, 
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
    post_url = base_url + post_resourse + key
    print('Запрос для создания направлен по адресу:', post_url)
    result_post = Http_method.post(post_url, json_for_create_new_place)
    print('Текст ответа:', result_post.text)
    return result_post
    
