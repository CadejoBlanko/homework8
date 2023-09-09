from models import Author, Quote, connect


def connect_to_database():
    connect('HomeWork08', host='mongodb+srv://Cadejo:0aGnluXd4Y56CviJ@homework08.lgshiv5.mongodb.net/?retryWrites=true&w=majority')


def search_quotes_by_author(author_name):
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
    else:
        quotes = []
    return quotes


def search_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return quotes


def search_quotes_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return quotes



def main():
    connect_to_database()
    while True:
        command = input("Enter the command (for example, name: Steve Martin): ")
        if command == 'exit':
            break

        command_parts = command.split(': ')
        if len(command_parts) != 2:
            print("Invalid command format. Please use the format 'command:value'.")
            continue

        action = command_parts[0]
        value = command_parts[1]

        if action == 'name':
            quotes = search_quotes_by_author(value)
        elif action == 'tag':
            quotes = search_quotes_by_tag(value)
        elif action == 'tags':
            quotes = search_quotes_by_tags(value)
        else:
            print("Invalid command. Valid commands: name, tag, tags.")
            continue

        if not quotes:
            print(f"No citations for author/tag: {value}")

        for quote in quotes:
            print(f"Author: {quote.author.fullname}, Quote: {quote.quote}")


if __name__ == '__main__':
    main()