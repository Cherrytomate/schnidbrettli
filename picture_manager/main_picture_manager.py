import ftplib
from picture_manager.ftp_manager import FDPParteiManager
from picture_manager.background_remove import remove_bg
from picture_manager.image_cropper import cropper
import time
import os



upload_ftp_dir ="/www/schnidbrettli.ch/wp-content/uploads/pictureresizer_out"
download_ftp_dir ="/www/schnidbrettli.ch/wp-content/uploads/pictureresizer_in"

def pictures():
    fdp_partei_manager = FDPParteiManager(FTP_HOST, FTP_USER, FTP_PASS,upload_ftp_dir,download_ftp_dir)


    # initialize FTP session

    # force UTF-8 encoding
    fdp_partei_manager.encoding = "utf-8"
    # print the welcome message
    #print(fdp_partei_manager.getwelcome())

    while True:
        files_list = fdp_partei_manager.list()
        if files_list != []:

            downloaded_files = fdp_partei_manager.download_images(files_list)
            bg_removed_files = remove_bg(downloaded_files)
            cropped_files = cropper(bg_removed_files)

            for file in cropped_files:
                try:
                    fdp_partei_manager.upload_image(file)
                except:
                    print()

        else:
            time.sleep(1)

if __name__ == '__main__':
    pictures()



