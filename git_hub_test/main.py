my_list = [
    {"author": "J.K. Rowling", "books": ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban"]},
    {"author": "Stephen King", "books": ["The Shining", "Carrie", "Misery"]},
    {"author": "Agatha Christie", "books": ["Murder on the Orient Express", "Death on the Nile", "And Then There Were None"]}
]


def parser_(str_to_search):
    for a in my_list:
        if str_to_search.lower()==a["author"].lower():
            return(a["books"])
        else:
            for b in a["books"]:
                if str_to_search.lower()==b.lower():
                    return(a["author"])
    return(False)


def searcher(name=None, book=None):
    search_result=[]
    if name:
        print(parser_(name))
    if book:
        print(parser_(book))

searcher("Stephen King", "")