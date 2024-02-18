import os
from urllib.parse import urlparse
from .file import sure_dir, remove_path
from .shell import shell_wrapper


def download_from_http(url, path_dest):
    sure_dir(os.path.dirname(path_dest))
    remove_path(path_dest)
    shell_wrapper(f'curl -fLSs {url} -o {path_dest}')


def download_from_git(url, path_dest):
    sure_dir(path_dest)
    ul = url.split('+', 1)
    b = []
    if len(ul) > 1:
        b = ['-b', ul[1]]
    sub = ' '.join([*b, ul[0]])
    shell_wrapper(f'git clone  {sub} .')


def download_tree_from_http(path_dest, url_list):
    result = {}
    for url in url_list:
        pr = urlparse(url)
        path = pr.path[1:]
        result[url] = path
        filepath = os.path.join(path_dest, path)
        download_from_http(url, filepath)
    return result
