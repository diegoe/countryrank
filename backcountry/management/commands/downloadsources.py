from django.core.management.base import BaseCommand, CommandError
import io, os, zipfile
import urllib.request

from backcountry.settings import BACKCOUNTRY_URIS

class Command(BaseCommand):
    help = 'Download and unzip the CSV files configure in BACKCOUNTRY_URIS'

    def download_and_extract_uris(self, uris, dest_dir, unzip=False):
        try:
            os.makedirs(dest_dir)
        except FileExistsError as e:
            self.stderr.write("WARN: dest_dir [%s] exists. Files will be overwritten." % dest_dir)

        os.chdir(dest_dir)

        for name, desc, uri in uris:
            self.stdout.write('[%s] %s' % (name, desc))
            self.stdout.write('○○ Downloading: %s' % uri, ending='\r')

            with urllib.request.urlopen(uri) as resp:
                self.stdout.write('●● Downloaded: %s\033[K' % uri)
                if unzip:
                    extract_path = os.path.join(os.getcwd(), '%s_unzip' % name)
                    with zipfile.ZipFile(io.BytesIO(resp.read())) as zipf:
                        self.stdout.write(
                                '○○ Uncompressing %s into %s'
                                % (name, extract_path), ending='\r')
                        zipf.extractall(path=extract_path)
                        self.stdout.write('●● Uncompressed files at: %s\033[K' % extract_path)
                else:
                    with open(name, 'xb') as fd:
                        self.stdout.write(
                                '○○ Saving file as %s' % name, ending='\r')
                        fd.write(resp.read())
                        self.stdout.write('●● Saved file as %s' % name)

            self.stdout.write('')

    def handle(self, *args, **options):
        # TODO: Use a path explicitly based on the django installation
        # and our app configuration. This works fine right now because
        # manage.py has a `cwd` on top of the whole django project.
        self.download_and_extract_uris(BACKCOUNTRY_URIS, 'downloads', unzip=True)
