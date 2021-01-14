from PIL import Image
import numpy as np
import os

def cropper(bg_removed_files):
    cropped_files = []
    for file in bg_removed_files:
        try:
            image=Image.open(file)
            image.load()

            image_data = np.asarray(image)
            image_data_bw = image_data.max(axis=2)
            non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
            non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
            cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

            image_data_new = image_data[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]

            new_image = Image.fromarray(image_data_new)
            new_name = str(file) + 'cropped.png'
            new_image.save(new_name)
            cropped_files.append(new_name)
            os.remove(file)
        except:
            print("failed to cropp" + " " + str(file))
    print(cropped_files)
    return cropped_files

