import config
import requests
import strings as ss

config = config.Config()
vkapi = config.vkapi

def vk_get_screen_name(custom_url):
    method = 'utils.resolveScreenName'
    url = 'https://api.vk.com/method/{}?screen_name={}&access_token={}&v=5.131'.format(method, custom_url, vkapi)
    response = requests.get(url)
    data = response.json()
    if 'response' in data:
        success_data = vk_get_name(custom_url, data['response']['type'])
        return success_data
    else:
        return None

def vk_get_name(original_id, type):
    if type == 'group':
        method = 'groups.getById'
        url = 'https://api.vk.com/method/{}?group_id={}&access_token={}&v=5.131&lang=ru'.format(method, original_id, vkapi)
        responce = requests.get(url)
        data = responce.json()
        if 'response' in data:
            info = {
                'url': f'{ss.src_vk}public{data["response"][0]["id"]}',
                'id': f'{data["response"][0]["id"]}',
                'name' : f'{data["response"][0]["name"]}',
                'type' : type
            }
            return info
    elif type == 'user':
        method = 'users.get'
        url = 'https://api.vk.com/method/{}?user_id={}&access_token={}&v=5.131&lang=ru'.format(method, original_id, vkapi)
        responce = requests.get(url)
        data = responce.json()
        if 'response' in data:
            info = {
                'url': f'{ss.src_vk}id{data["response"][0]["id"]}',
                'id': f'{data["response"][0]["id"]}',
                'name' : f'{data["response"][0]["first_name"]} {data["response"][0]["last_name"]}',
                'type': type
            }
            return info
    return None


