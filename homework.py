# Davaleba 12
collection = {}

def add_book(author, title, genre):
    if author not in collection:
        collection[author] = []
    collection[author].append({'title': title, 'genre': genre})
    print("წიგნი დაემატა კოლექციას.")

def search_author(author_name):
    return collection.get(author_name, [])

def all_books():
    return collection

def main():
    while True:
        action = input("შეიყვანეთ რომელიმე: (add/title/author/end): ").strip().lower()
        if action == "end":
            break
        elif action == "add":
            title = input("შეიყვანეთ წიგნის სახელწოდება: ").strip()
            author = input("შეიყვანეთ ავტორის სახელი: ").strip()
            genre = input("შეიყვანეთ ჟანრი: ").strip()
            add_book(author, title, genre)
        elif action == "author":
            author_name = ("შეიყვანეთ ავტორის სახელი: ").strip()
            books = search_author(author_name)
            if books:
                print(f"წიგნები {author_name} მიერ:")
                for book in books:
                    print(f"სახელწოდება: {book['title']}, ჟანრი: {book['genre']}")
            else:
                print(f"{author_name} ავტორის სახელით წიგნი არ მოიძებნა.")
        elif action == "title":
            title_name = input("შეიყვანეთ წიგნის სახელწოდება: ").strip()
            found = False
            for author, books in collection.items():
                for book in books:
                    if book['title'].lower() == title_name.lower():
                        print(f"მოიძებნა: \"{book['title']}\" {author}-ს მიერ, ჟანრი: {book['genre']}")
                        found = True
                if not found:
                    print(f"წიგნი დასახელებით {title_name} არ მოიძებნა.")
        elif action == "all":
            print(all_books())
        else:
            print("არასწორი ბრძანება. გთხოვთ შეიყვანოთ რომელიმე: (add/title/author/end): ")

main()