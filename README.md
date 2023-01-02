# <div align="center">Open Images V7  ToolKit</div>
Download dataset for custom classes from [Open Images Dataset V7](https://storage.googleapis.com/openimages/web/index.html)

## <div align="center">Documentation</div>

### Installation
Clone repo and install [requirements.txt](https://github.com/EdgeOfAI/oidv7-Downloader/blob/main/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment

```bash
git clone https://github.com/EdgeOfAI/oidv7-Downloader.git  # clone
cd oidv7-Downloader
pip3 install -r requirements.txt  # install
```
### Download Custom Dataset


Choose class names from [Available classes](https://github.com/EdgeOfAI/oidv7-Downloader/blob/main/class_names.csv) and provide choosen class names to the required argument

Required argument:
  - classes




Change optional arguments to set custom bounding box parameters

All Optional arguments equal to 0 as a default value 

Optional arguments:
  - isOcclud
  - isTruncated
  - isGroupOf
  - isDepiction
  - isInside


Run main.py to download dataset for custom classes
```bash
python3 main.py --classes Car Person # downloads dataset for Car and Person classes with default parameters
```

The algorithm will take care to download all the necessary files and build the directory structure like this:
```
main_folder
│   main.py
│
└───dataset
    │   img_ids.txt
    │
    └───images
    |    │   0fdea8a716155a8e.jpg
    |    │   2fe4f21e409f0a56.jpg
    |    |   ...
    |
    └───labels
        |    0fdea8a716155a8e.txt
        |    2fe4f21e409f0a56.txt
        |    ...
```  

