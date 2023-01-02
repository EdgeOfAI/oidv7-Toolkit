#Downloading labels and creating folders for data
import os
import shutil
import urllib

def PrepareFolders():
    #Re-setting folders
    if os.path.isdir('dataset'):
        remove = input('You have to remove dataset folder to continue (yes/no):').lower()
        if remove.startswith('n'):
            exit(0)
    shutil.rmtree('dataset', ignore_errors=True)
    os.mkdir("dataset")
    os.mkdir("dataset/images")
    os.mkdir("dataset/labels")

    #Download annonation files
    files = os.listdir()
    if not "oidv6-train.csv" in files:
        urllib.request.urlretrieve("https://storage.googleapis.com/openimages/v6/oidv6-train-annotations-bbox.csv", "oidv6-train.csv")

    if not "oidv7-validation.csv" in files:
        urllib.request.urlretrieve("https://storage.googleapis.com/openimages/v5/validation-annotations-bbox.csv", "oidv7-validation.csv")

    if not "oidv7-test.csv" in files:
        urllib.request.urlretrieve("https://storage.googleapis.com/openimages/v5/test-annotations-bbox.csv", "oidv7-test.csv")


def ParamSettings(params):
    
    #required_params
    required_params = []
    for key in params:
        if key != 'classes':
            required_params.append(str(params[key]))
    

    #Read class_names.csv
    file = open('class_names.csv', 'r')
    lines = file.readlines()
    all_class_names = {}
    for line in lines:
        id, name = line.split(',')[0], line.split(',')[1][:-1]
        all_class_names[name] = id


    #required_class_names
    required_class_names = {}
    name = None
    for i in params['classes']:
        if i[0].isupper():
            if name is not None:
                if name in all_class_names:
                    required_class_names[name] = all_class_names[name]
                else:
                    raise NameError(f'incorrect class name: {name}')
            name = i
        else:
            name += " " + i
    if len(name.split()) > 1:
        if name in all_class_names:
            required_class_names[name] = all_class_names[name]
        else:
            raise NameError(f'incorrect class name: {name}')
    required_class_names = dict((v,k) for k,v in required_class_names.items())
    return (required_params, required_class_names)
