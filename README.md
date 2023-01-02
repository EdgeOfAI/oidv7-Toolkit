# oidv7-Downloader
Download subdataset of Open Images Dataset V7

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

All Optinal arguments have default 0 value

Optional arguments:
  - isOcclud
  - isTruncated
  - isGroupOf
  - isDepiction
  - isInside


```bash
python3 main.py --classes Car Person # downloads dataset for Car and Person classes with default parameters
```
