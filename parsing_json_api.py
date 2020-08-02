import requests
import json

url = 'https://www.instagram.com/graphql/query'

# shortcode didapat dari link ig, misal: https://www.instagram.com/p/CDQ1J-6JGvv/
# first adalah jumlah data yang akan dimuat, maksimal = 50
variable = {"shortcode": "CDQ1J-6JGvv", "first": 50}

# query_hash diberikan per-device bukan akun.
params = {
    'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
    'variables': json.dumps(variable)
}

results = requests.get(url, params=params).json()

# untuk bagian dalam kurung siku, cocokkan dengan yang ada di Instagram
all_users = results['data']['shortcode_media']['edge_liked_by']['edges']

for user in all_users:
    username = user['node']['username']
    fullname = user['node']['full_name']
    prof_pic = user['node']['profile_pic_url']

    print(username, fullname, prof_pic)
    # print(username)
