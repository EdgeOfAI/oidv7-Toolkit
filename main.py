import csv
import os
import sys
import shutil
from downloader import *
from settings import *


class ExtractData:
    def __init__(self,file_path, data_type, params):
        self.file_path = file_path
        self.data_type = data_type
        self.params = params
    
    def Download(self):
        file_path = self.file_path
        data_type = self.data_type
        
        
        ##Required classes and parameters of data
        required_params, class_names = ParamSettings(self.params)


        #Extract images according to classes needed
        file = open(file_path, 'r')
        lines =  file.readlines()[1:]

        labels = dict()
        img_ids = set()
        #TODO : add image counter and class counter 
        for line in lines:
            
            info = line.split(',')
            img_id, class_name, xmin, xmax, ymin, ymax = info[0], info[2], info[4], info[5], info[6], info[7]
            img_params = info[8:]
            img_params[4] = img_params[4][0]
            ismatched = True
            for i in range(5):
                if img_params[i] != required_params[i] and required_params[i] != '2':
                    ismatched = False
            
            if (class_name in class_names) and ismatched:
                img_ids.add(img_id)
                if not img_id in labels:
                    labels[img_id] = []
                labels[img_id].append([class_names[class_name], xmin, xmax, ymin, ymax])

        #Write image_ids.txt to download images
        pathToImgIDs = "dataset/img_ids.txt"
        with open(pathToImgIDs, 'w') as fp:
            for item in img_ids:
                # write each item on a new line
                fp.write(f"{data_type}/{item}\n")
        

        #Download images for selected classes according to img_ids.txt
        download_all_images({
            'image_list' : pathToImgIDs,
            'download_folder' : "dataset/images",
            'num_processes' : 5
        })
        
        
        '''
        Creating labels in YOLOv5 format but class_name is not an integer:
            class_name x y weight height
            class_name is id of this class in class_names.csv 
        '''
        for name, classes in labels.items():
            with open("dataset/labels/" + name + ".txt", 'w') as f:
                for line in classes:
                    x = (float(line[1]) + float(line[2])) / 2
                    y = (float(line[3]) + float(line[4])) / 2
                    w = float(line[2]) - float(line[1])
                    h = float(line[4]) - float(line[3])
                    f.write(f"{line[0]} {x} {y} {w} {h}\n")




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Download data from OpenImages')
    parser.add_argument('--isOccluded', type=int, default=2, help='Description ')
    parser.add_argument('--isTruncated', type=int, default=2, help='Description ')
    parser.add_argument('--isGroupOf', type=int, default=2, help='Description ')
    parser.add_argument('--isDepiction', type=int, default=2, help='Description ')
    parser.add_argument('--isInside', type=int, default=2, help='Description ')
    parser.add_argument('--classes', nargs='+', type=str, required=True)

    args = vars(parser.parse_args())

    #Downloading labels and creating folders for data
    PrepareFolders()

    ExtractData("oidv6-train.csv", 'train', args).Download()
    ExtractData("oidv7-validation.csv", 'validation', args).Download()
    ExtractData("oidv7-test.csv", 'test', args).Download()