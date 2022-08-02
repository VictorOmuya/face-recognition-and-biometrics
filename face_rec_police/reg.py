# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:28:17 2022

@author: HP
"""


from PIL import Image  
import csv


def registeration(imgurl, name, Description):
  
    directory = imgurl
    picture = Image.open(directory)
    imgname = f'registered/{name}.jpg'
    picture = picture.save(imgname)
    
    
    
    filename = "database.csv"
    #with open(filename, 'w') as csvfile:
     #   filewriter = csv.writer(csvfile)
      #  filewriter.writerow([name, Description])
        
    
    with open(filename,'r+') as f:
        myDataList = f.readlines()
        nameList = []
       
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        
        if name not in nameList:
            f.writelines(f'\n{name},{Description}')
            res = 'registration successful'
        elif name in nameList:
            res = 'name already exist'
            
    return res

            
      