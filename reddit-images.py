import os
import requests
import praw
import sys
import json


class FileIO:
    @staticmethod
    def create_directory(path, existok):
        os.makedirs(path, exist_ok=existok)

    @staticmethod
    def get_filename(url):
        if url.find('/'):
            fn = url.rsplit('/', 1)[1]
        return fn

    @staticmethod
    def download_file(url, path, name):
        r = requests.get(url, allow_redirects=False)
        open(os.path.join(path, name), 'wb').write(r.content)


class Reddit:
    def __init__(self, reddit):
        self.reddit = reddit

    def get_submissions(self, subreddit, count):
        ext = [".jpg", ".jpeg", ".png", "bmp"]
        titles = []
        for submission in self.reddit.subreddit(subreddit).hot(limit=count):
            if submission.url.endswith(tuple(ext)):
                titles.append(submission.url)
                print(submission.title)
        return titles


def download_images_from_reddit():
    with open('config.json') as config_file:
        config = json.load(config_file)

    reddit = praw.Reddit(client_id=config['client_id'],
                         client_secret=config['client_secret'],
                         user_agent=config['user_agent'])
    posts = Reddit(reddit)
    submissions = posts.get_submissions(sys.argv[1], int(sys.argv[2]))

    fileio = FileIO()
    file_path = os.path.join(config['file_path'], sys.argv[1])
    fileio.create_directory(file_path, True)

    for sub in submissions:
        fn = fileio.get_filename(sub)
        fileio.download_file(sub, file_path, fn)


def main():
    download_images_from_reddit()


if __name__ == "__main__":
    main()
