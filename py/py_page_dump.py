import urllib.request, urllib.error, urllib.parse
from html.parser import HTMLParser
import io


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = io.StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def add_line_break(s):
    new_str = ['#']
    length = 2
    for c in s.split():
        if length + len(c) + 1 > 79:
            length = 2
            new_str.append('\n#')
        length += len(c) + 1
        new_str.append(c)
    return ' '.join(new_str)


def add_whitespace(s):
    new_str = ''
    for c in s:
        new_str += c
        if c == '.':
            new_str += ' '
    return new_str


start = 1
stop = 747
urls, titles, problems, files = {}, {}, {}, {}
err = []
for i in range(start, stop + 1):
    url = 'https://projecteuler.net/problem=' + str(i)
    response = urllib.request.urlopen(url)
    html = response.read().decode().replace('\n', '')
    urls[i] = url
    titles[i] = html.split('<h2>')[1].split('</h2>')[0]

    prob_url = 'https://projecteuler.net/minimal=' + str(i)
    response = urllib.request.urlopen(prob_url)
    prob_html = response.read().decode().replace('\n', '')
    problems[i] = add_line_break(add_whitespace(strip_tags(prob_html)))    

    f_name = 'py_' + str(i).zfill(4) + '_' + str(titles[i]).replace(' ', '_').lower()
    content = [
        "# Solution of;",
        "# Project Euler Problem " + str(i) + ": " + str(titles[i]),
        "# " + str(urls[i]),
        "# ",
        problems[i],
        "# ",
        "# by lcsm29 http://github.com/lcsm29/project-euler",
        "import timed",
        "",
        "",
        "def dummy(n):",
        "    pass",
        "",
        "",
        "if __name__ == '__main__':",
        "    n = 1000",
        "    i = 10000",
        "    prob_id = " + str(i),
        "    timed.caller(dummy, n, i, prob_id)"
    ]
    files[f_name + '.py'] = content
    try:
        with io.open(f_name + '.py', 'w', encoding='utf-8') as f:
            for line in content:
                try:
                    f.write(line + '\n')
                except UnicodeEncodeError:
                    err.append((f_name, line))
                    continue
    except OSError:
        err.append((f_name, 'OSError'))
        continue

with io.open('py_page_dump_error.txt', 'a', encoding='utf-8') as f:
    f.write('\n'.join('%s %s' % x for x in err))
