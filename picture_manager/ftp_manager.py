import ftplib
import logging
import os
import random
from datetime import datetime

logger = logging.getLogger(__name__)


class FDPParteiManager:
    FTP_HOST = None
    FTP_USER = None
    FTP_PASS = None

    def __init__(self, url, user, password, upload_ftp_dir, download_ftp_dir):
        self._url = url
        self._user = user
        self._password = password
        self._upload_ftp_dir = upload_ftp_dir
        self._download_ftp_dir = download_ftp_dir

    def upload_image(self, file):

        session = ftplib.FTP(self._url, self._user, self._password)
        session.cwd(self._upload_ftp_dir)
        f = open(file, 'rb')
        print(str(file) + " processed image successfully uploaded")
        hash = random.getrandbits(128)
        filename = str(hash) + ".png"
        print(filename)
        session.storbinary('STOR ' + filename, f)
        f.close()
        session.quit()
        os.remove(file)

    def download_images(self, files_list):
        session = ftplib.FTP(self._url, self._user, self._password)
        start = datetime.now()
        session.cwd(self._download_ftp_dir)
        downloaded_files = []
        for file in files_list:
            print(files_list)
            if file != "." and file != "..":

                print(file)
                try:
                    inputs = []
                    print("Downloading..." + file)
                    session.retrbinary("RETR " + file, open(file, 'wb').write)
                    downloaded_files.append(file)
                    print(file + " successfully downloaded")
                    # input_data = str(file) #...get inputs(category,name,width, height)
                    # x = input_data.replace('.jpg',"")
                    # a = x.split("@")
                    # a.remove('')
                    # print(a)
                    # if (len(a)) == 4:
                    # print("inputs for file: " + str(file) + ": "+ str(a[0])+ str(a[1]) + str(a[2]) + str(a[3]))
                    # football@smiley@10.5@10@.jpg".... file imput structure
                    session.delete(self._download_ftp_dir + str(file))

                    # else:








                except Exception as s:
                    os.remove(file)
                    print("wrong input data")
                    # print((len(a)))
                    session.delete(self._download_ftp_dir + str(file))
        session.quit()

        end = datetime.now()
        diff = end - start
        print('All files downloaded in ' + str(diff.seconds) + 's')
        print(downloaded_files)
        return downloaded_files

    def list(self):
        session = ftplib.FTP(self._url, self._user, self._password)
        session.cwd(self._download_ftp_dir)
        files_list = session.nlst()
        files_list.remove(".")
        files_list.remove("..")
        print(files_list)

        return files_list
