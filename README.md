reddit-images
================

Tool for getting images from Reddit

## Installation
1. Clone repository
```
git clone https://github.com/ansonj712/reddit-images.git
```
2. Update config.json with client_id, client_secret, user_agent and file_path
3. Install packages
```
pip install -r requirements.txt
```


## How to Use
### Example - Getting the hot 10 images from /r/EarthPorn
```
python reddit-images.py earthporn 10 hot 
```