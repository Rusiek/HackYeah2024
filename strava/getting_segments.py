import requests

headers = {
    'Authorization': 'Bearer ea84bf3b2bba311116ece97ea61c15e9397871db',
}

def get_starred_segments():
    with open("segments_id.txt", 'w') as f:
        for page in range(1, 47):
            url = f"https://www.strava.com/api/v3/segments/starred?page={page}&per_page=200"
            response = requests.get(url=url, headers=headers)
            for segment in response.json():
                ID = str(segment['id']) + "\n"
                f.write(ID)

if __name__ == '__main__':
    get_starred_segments()