import os
import csv
import pandas as pd
import shutil

path = 'assets/train_images/'

flist = pd.read_csv('data-10.csv')

file_name = flist['file_name'].tolist()


for filename in os.listdir(path):
    print(filename)
    if filename not in file_name:
          os.remove(path+filename)
        
'''
with open('data-50.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['file_name', 'size'])
  for root, dirs, files in os.walk(path):
    for filename in files:
        #print(os.stat(os.path.join(root,filename)).st_size)
        writer.writerow([filename, os.stat(os.path.join(root,filename)).st_size])
        
path = 'assets/train_images' 
       
with open('ref_data-50.csv', 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['file_name', 'size'])
  for root, dirs, files in os.walk(path):
    for filename in files:
        #print(os.stat(os.path.join(root,filename)).st_size)
        writer.writerow([filename, os.stat(os.path.join(root,filename)).st_size])        
        '''