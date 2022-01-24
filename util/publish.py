#!/usr/bin/env python3

import dateutil.parser
import glob
import re

re_date = re.compile(r'.*(\d\d\d\d-\d\d-\d\d.*)$')
time_string = "DAY_OF_MONTH MONTH_LONG YEAR_LONG г." #, HOUR_24:MINUTE"
re_date_holder = re.compile(r'.*<time>(.*)</time>')


def write_toc():
    text_files = glob.glob('../docs/content/2*.md')
    blog_posts = []
    for text_file in sorted(text_files, reverse=True):
        m = re.match(re_date, text_file)
        if not m: continue
        blog_post = [f'#{m.group(1)}']
        with open(text_file, 'r') as f:
            for line in f:
                if '# ' in line:
                    blog_post.append(line.replace('#', '').strip())
                if '<time>' in line:
                    #date = line.replace('<time>', '').replace('</time>', '').strip()
                    date = re.match(re_date_holder, line).groups(1)[0]
                    date = dateutil.parser.isoparse(date)
                    date = human_format(time_string, date)
                    blog_post.append(date)
                    blog_posts.append(blog_post)
                    break
    sorted(blog_posts, key=lambda el: el[0], reverse=True)
    years = sorted(list(set(map(lambda el: el[0][1:5], blog_posts))), reverse=True)

    with open('../src/pug_modules/main/aside-links.pug', 'w') as f:
        for year in years:
            spaces = "    "
            f.write(f'h5.offcanvas-title Материалы за {year} г:\n')
            f.write(f'{spaces}ul.nav.nav-pills.flex-column.mb-auto\n')
            for link in sorted(blog_posts, key=lambda el: el[0], reverse=True):
                f.write(f'{spaces * 2}li\n')
                f.write(f'{spaces * 3}a.nav-link.link-secondary(href="{link[0]}")\n')
                f.write(f'{spaces * 4}<svg class="link-secondary aside-icon"><use xlink:href="#blockquote-left"></use></svg>\n')
                f.write(f'{spaces * 4}span {link[1]}.\n')
                f.write(f'{spaces * 4}<br>\n')
                f.write(f'{spaces * 4}time {link[2]}\n')

    with open('../src/pug_modules/main/article-links.pug', 'w') as f:
        for year in years:
            spaces = "    "
            f.write(f'h2 Материалы за {year} г:\n')
            f.write(f'ul\n')
            for link in sorted(blog_posts, key=lambda el: el[0], reverse=True):
                f.write(f'{spaces * 1}li\n')
                f.write(f'{spaces * 2}a(href="{link[0].replace("#", "https://github.com/yababay/humanitarian-blog/blob/main/docs/content/")}")\n')
                f.write(f'{spaces * 3}span {link[1]}\n')
                f.write(f'{spaces * 3}|&nbsp;\n')
                f.write(f'{spaces * 3}span [{link[2]}]\n')


def human_format(time_string, datetime_value):
    aliases = {
        "WEEKDAY_SHORT": "%a",
        "WEEKDAY_LONG": "%A",
        "WEEKDAY_NUM": "%w",
        "DAY_OF_MONTH": "%d",
        "MONTH_SHORT": "%b",
        "MONTH_LONG": "%B",
        "MONTH_NUM": "%m",
        "YEAR_SHORT": "%y",
        "YEAR_LONG": "%Y",
        "HOUR_24": "%H",
        "HOUR_12": "%I",
        "AM_PM": "%p",
        "MINUTE": "%M",
        "SECOND": "%S",
        "MICROSECOND": "%f",
        "UTC_OFFSET": "%z",
        "TZ_NAME": "%Z",
        "DAY_OF_YEAR": "%j",
        "WEEK_NUM": "%U",
        "WEEK_NUM_START_MONDAY": "%W",
        "LOCAL_DATETIME": "%c",
        "LOCAL_DATE": "%x",
        "LOCAL_TIME": "%X",
    }

    for alias, directive in aliases.items():
        time_string = time_string.replace(alias, directive)

    return datetime_value.strftime(time_string) \
        .replace('January',   'января') \
        .replace('February',  'февраля') \
        .replace('March',     'марта') \
        .replace('April',     'апреля') \
        .replace('May',       'мая') \
        .replace('June',      'июня') \
        .replace('July',      'июля') \
        .replace('August',    'августа') \
        .replace('September', 'сентября') \
        .replace('October',   'октября') \
        .replace('November',  'ноября') \
        .replace('December',  'декабря') 


if __name__ == "__main__":
    write_toc()

