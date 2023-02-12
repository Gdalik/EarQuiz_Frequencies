from pathlib import Path


def validUrls(urls: list):
    return [url for url in urls if url.toLocalFile() and Path(url.toLocalFile()).exists()]
