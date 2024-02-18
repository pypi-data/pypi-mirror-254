from urllib.parse import quote

import wikirate4py
import urllib.request

from wikirate4py import Cursor

api = wikirate4py.API('NzSK5muu3o7oSwDa2PpUVQtt')

cursor = Cursor(api.get_sources,
                wikirate_link='downloads.modern-slavery-statement-registry.service.gov.uk/pdf-published/', per_page=100)
while cursor.has_next():
    sources = cursor.next()
    for source in sources:
        if source.file_url == '':
            try:
                print(source)
                result = urllib.parse.urlparse(source.original_source)
                url = "https://{0}{1}".format(result.netloc, quote(result.path))
                urllib.request.urlretrieve(url, 'D://modern-slavery-statement.pdf')
                api.upload_file(source=source.name, file='D://modern-slavery-statement.pdf')
            except Exception as e:
                print(e.__str__())
