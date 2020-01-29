import io
import os
import zipfile

import urllib.request

import fetch_data_uris

def download_and_extract_uris(uris, dest_dir, unzip=False):
    try:
        os.makedirs(dest_dir)
    except FileExistsError as e:
        print("WARN: dest_dir [%s] exists. Files will be overwritten." % dest_dir)

    os.chdir(dest_dir)

    for name, desc, uri in uris:
        print('[%s] %s' % (name, desc))
        print('○○ Downloading: %s' % uri, end='\r')

        with urllib.request.urlopen(uri) as resp:
            print('●● Downloaded: %s\033[K' % uri)
            if unzip:
                extract_path = os.path.join(os.getcwd(), '%s_unzip' % name)
                with zipfile.ZipFile(io.BytesIO(resp.read())) as zipf:
                    print('○○ Uncompressing %s into %s' % (name, extract_path), end='\r')
                    zipf.extractall(path=extract_path)
                    print('●● Uncompressed files at: %s\033[K' % extract_path)
            else:
                with open(name, 'xb') as fd:
                    print('○○ Saving file as %s' % name, end='\r')
                    fd.write(resp.read())
                    print('●● Saved file as %s' % name)

        print('')

if __name__ == '__main__':
    download_and_extract_uris(fetch_data_uris.uris, 'downloads', unzip=True)
