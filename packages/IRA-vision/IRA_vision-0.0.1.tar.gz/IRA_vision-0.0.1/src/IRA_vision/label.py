import cv2
import time
import easyocr

def find_partial_name(names_list, partial_name):
    matching_names = []
    
    for index, name in enumerate(names_list):
        if partial_name.lower() in name.lower():
            matching_names.append((index, name))
    
    return matching_names

def readlabel(imagePath,texts):
    result=[]
    information=[]
    reader = easyocr.Reader(['en'])
    img=cv2.imread(imagePath)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    output = reader.readtext(gray)
    for i in range(len(output)):
        information.append(output[i][1])
    for j in texts:
        result.append(find_partial_name(information, j))
    #cv2.imwrite('texts.jpg',img)
    return result