import random
import string

GENRE = ['Classic', 'Drama', 'Romance', 'Satire', 'Horror', 'Science']
COVER = ['Paperback', 'Hardcover']


def generate_name(length):
    alphabet = string.ascii_lowercase
    return ''.join(random.choices(alphabet, k=length)).capitalize()


def generate_data(n, _format=list):
    book_names = [generate_name(random.randint(5, 8)) for _ in range(n)]
    book_lengths = [random.randint(50, 540) for _ in range(n)]
    book_categories = random.choices(GENRE, k=n)
    book_covers = random.choices(COVER, k=n)

    if _format == dict:
        return [{"book_name": name, "book_length": length, "book_cover": cover, "book_category": category}
                for name, length, cover, category in zip(book_names, book_lengths, book_covers, book_categories)]
    else:
        return list(zip(book_names, book_lengths, book_categories, book_covers))


if __name__ == "__main__":
    print(generate_data(10))
