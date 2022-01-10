import dateutil.parser
import glob
import json
import pytz
import re
from datetime import datetime
from transliterate import translit
from .human_time import format as human_format

re_date = re.compile(r'.*(\d\d\d\d-\d\d-\d\d.*)$')
time_string = "DAY_OF_MONTH MONTH_LONG YEAR_LONG г., HOUR_24:MINUTE"


def write_toc():
    text_files = glob.glob('./docs/content/*.md')
    blog_posts = []
    for text_file in sorted(text_files, reverse=True):
        m = re.match(re_date, text_file)
        if not m: continue
        blog_post = [f'#{m.group(1)}']
        with open(text_file, 'r') as f:
            for line in f:
                if '#' in line:
                    blog_post.append(line.replace('#', '').strip())
                if '<time>' in line:
                    blog_post.append(line.replace('<time>', '').replace('</time>', '').strip())
                    blog_posts.append(blog_post)
                    break
    with open('./docs/toc.json', 'w') as f:
        output = json.dumps(blog_posts, ensure_ascii=False)
        f.write(output)
        return output


def initialize(title, date):
    m = re.match(re_date, date)
    if m:
        date = dateutil.parser.isoparse(date)
    else:
        date = datetime.now(pytz.timezone('Europe/Moscow'))
    fn = f'./docs/content/{date.isoformat().replace(":", "-").replace("T", "-")[:16]}-{distill(title)}.md'
    with open(fn, 'w') as file:
        file.write(f'# {title}\n\n<time>{human_format(time_string, date)}</time>\n\n')
    write_toc()


def distill(value):
    return translit(value, 'ru', reversed=True).lower().strip() \
            .replace(' ', '-') \
            .replace(',', '')  \
            .replace('?', '')  \
            .replace('!', '')  \
            .replace('@', '')  \
            .replace(':', '')  \
            .replace(';', '')  \
            .replace('"', '')  \
            .replace("'", '')  \
            .replace("«", '')  \
            .replace("»", '')  \
            .replace('.', '-')


