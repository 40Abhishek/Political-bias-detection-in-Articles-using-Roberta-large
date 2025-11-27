import webbrowser
import zipfile
import os
import time



file=open("datafiles.txt", "r")

sites=file.readlines()

for i in sites[:1]:
    print(i)
    pass
    webbrowser.open(i)


time.sleep(6)

down="C:\\Users\\2077a\\Downloads"


files = os.listdir(down)
# print("Files in folder:", files)
zip_file=[]

for i in files:
    if ".zip" and "gkg" in i:
        zip_file.append(i)

     
extract_to = "Extracted_data"    

for i in zip_file:
    with zipfile.ZipFile(down+"\\"+i, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

print("Extraction complete!")