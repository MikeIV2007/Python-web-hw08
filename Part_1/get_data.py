from models import Quote, Author
import connect

def get_quots_by_tags(value):
    print (value)
    tags_list =value.split(",")
    print (tags_list)
    for tag in tags_list:
        quotes = Quote.objects(tags=tag)
        if quotes:
            for quote in quotes:
                print("-------------------")
                print(f"Quote: {quote.quote}")
                print(f"Author: {quote.author.fullname}")
                print(f"Tags: {quote.tags}")
        else:
            print(f"Tag '{value}' not found in the database.")


def get_quots_by_tag(value):
    quotes = Quote.objects(tags=value.strip())
    if quotes:
        for quote in quotes:
            print("-------------------")
            print(f"Quote: {quote.quote}")
            print(f"Author: {quote.author.fullname}")
            print(f"Tags: {quote.tags}")
    else:
        print(f"Tag '{value}' not found in the database.")


def get_quots_by_name(value):
    author_instance = Author.objects(fullname=value.strip()).first()
    if author_instance:
        quotes = Quote.objects(author=author_instance)
        for quote in quotes:
            print("-------------------")
            print(f"Quote: {quote.quote}")
            print(f"Author: {quote.author.fullname}")
            print(f"Tags: {quote.tags}")
    else:
        print(f"Author '{value}' not found in the database.")

def get_user_input():
        try:
            command = input("Input command (for instance: 'name: Steve Martin', 'tag:life', 'tags:life,live', or 'exit'): ")
            return command
        except TypeError as err:
            print (err) 


def main():
    while True:
        command = get_user_input()
        if command == 'exit':
            print("The end")
            break
        
        command_type, value = command.split(':', 1)

        if command_type.strip() == 'name':
            get_quots_by_name(value)

        elif command_type.strip() == 'tag':
            get_quots_by_tag(value)

        elif command_type.strip() == 'tags':
            get_quots_by_tags(value)
        else:
            print (f"Command: {command_type} not exists!")
    
if __name__ == "__main__":
    main()