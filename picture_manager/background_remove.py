import requests
import os


def remove_bg(downloaded_files):
    bg_removed_files =[]
    for file in downloaded_files:
        try:
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': open(file, 'rb')},
                data={'size': 'auto'},
                headers={'X-Api-Key': os.getenv("BG_REMOVE_API_KEY")},
            )
            if response.status_code == requests.codes.ok:
                name = str(file) + 'no-bg.png'
                with open(name, 'wb') as out:
                    out.write(response.content)
                    bg_removed_files.append(name)
                    os.remove(file)
        except:
            print("failed to download" + " " + str(file))

    return bg_removed_files