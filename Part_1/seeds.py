import json
from pathlib import Path
from models import Author, Quote
import connect

author_data_path = Path('JSON/authors.json')
with open(author_data_path, 'r', encoding='utf-8') as author_file:
    author_data = json.load(author_file)

for obj in author_data:
    author = Author(
        fullname=obj['fullname'],
        born_date=obj['born_date'],
        born_location=obj['born_location'],
        description=obj['description']
    )
    author.save()

quote_data_path = Path('JSON/qoutes.json')
with open(quote_data_path, 'r', encoding='utf-8') as quote_file:
    quote_data = json.load(quote_file)

for obj in quote_data:
    author = Author.objects(fullname=obj['author']).first()

    if author:
        quote = Quote(
            tags=obj['tags'],
            author=author,
            quote=obj['quote']
        )
        quote.save()
    else:
        print(f"Author '{obj['author']}' not found, skipping quote.")
