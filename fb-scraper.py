# Before running:
# 1. pip install facebook-scraper
# 2. Creat blank post_contents.csv file

import csv

from facebook_scraper import get_posts

with open('pages.csv') as pages: 
    print('opened input file')
    reader = csv.reader(pages, delimiter=',')
    with open('post_contents.csv', 'w', encoding="utf-8") as export_data:
        print('opened output file')
        writer = csv.writer(export_data)
        writer.writerow(['Post Content'])
        line_count = 0
        for row in reader:
            print(row)
            # Skip header row
            if line_count == 0:
                line_count += 1
                continue
            # End reading at last row
            elif line_count == 5:
                break
            # Call extracting function
            else:
                page = row[0]
                for post in get_posts(page, pages = 15):
                    post_content = post['text']
                    if post_content is not None:
                        print(post_content[:50])
                        writer.writerow([post_content])
                line_count += 1
            print(line_count, " ", row[0])
    print('closed output file')
print('closed input file')

