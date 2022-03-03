# For Python 2 compatibility.
from __future__ import print_function

import lxml.html
import requests

def main():
  for i in range(0,100,1):
    r = requests.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    url = r.url
    html_source = r.text
    root_element = lxml.html.fromstring(html_source)
    id = "mw-parser-output"
    content = root_element.find_class(id)
    filename = 'выкачка' + str(i) + '.txt';

    with open(filename, 'w') as f:
      for p in content:
        text = p.text_content()
        f.write(text)
      #print(p.text_content(), end = " ")
    indexfile = 'index.txt'
    with open(indexfile, 'a') as index:
      index.write(url + ' - ' + filename + '\n')
      
if __name__ == '__main__':
    main()