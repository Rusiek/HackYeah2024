import requests
import json

def get_segment_info_by_id(ID:int, headers:dict, idx:int):
    current_json_file = 'segments_info.json'
    try:
        with open(current_json_file, 'r') as file:
            current_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        current_data = {}

    url = f"https://www.strava.com/api/v3/segments/{ID}"
    response = requests.get(url=url, headers=headers)

    new_info = response.json()
    current_data[idx] = new_info

    with open(current_json_file, 'w') as file:
        json.dump(current_data, file, indent=4)


def get_all_segments_info():
    headers_list = [{'Authorization': 'Bearer 2ea2409c0afcdc8fdf66b0e0ef5c2141a0dd86bb'},
                    {'Authorization': 'Bearer 55ffbb6e6bb2102ea703762f45aa81d77485df9c'},
                    {'Authorization': 'Bearer 8a62bd0832311207a304dcfee3ccea150c676a6d'},
                    {'Authorization': 'Bearer 49b22581cb284896530b838d01c3b7a1ed208286'},
                    {'Authorization': 'Bearer 5ae11ec223c35d9f9fb349ba8c232c943bcbd6bf'},
                    {'Authorization': 'Bearer 724084c086bb2f4bc8cca508518f5764d1be9c0f'},
                    {'Authorization': 'Bearer 1298822628a0d86e0d0f0f3e0a41bf343791d7ad'},
                    {'Authorization': 'Bearer d889e5cd7a3d6d1c53ad89437ffd783f80561b8b'},
                    {'Authorization': 'Bearer ff72815354e5073c381b2a863e9033c2287f2563'},
                    {'Authorization': 'Bearer bcf0af1f2b2f01afd9dd877443b9acccfbb0f043'},
                    ]

    idx = 1
    with open('segments_id.txt', 'r') as f:
        for headers in headers_list:
            for i in range(920):
                ID = int(f.readline())
                get_segment_info_by_id(ID=ID, headers=headers, idx=idx)
                idx += 1

if __name__ == '__main__':
    get_all_segments_info()