import os
import requests
from picture_manager.API_Manager import API_Counter


def remove_bg(downloaded_files,):
    bg_removed_files = []
    for file in downloaded_files:
        API_Key = API_Counter()
        print(API_Key)
        try:
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': open(file, 'rb')},
                data={'size': 'auto'},
                headers={'X-Api-Key': API_Key},
            )
            if response.status_code == requests.codes.ok:
                name = str(file) + 'no-bg.png'
                print("test")
                with open(name, 'wb') as out:
                    out.write(response.content)
                    bg_removed_files.append(name)
                    os.remove(file)

                API_Key = API_Counter()
                print(API_Key)


            print(response.json())
        except:
            print("failed to download" + " " + str(file))

    return bg_removed_files
