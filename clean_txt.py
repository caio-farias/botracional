from os import listdir

books = listdir('./bad_txt')

for book in books:
    f = open(f"./content_collection/books/UED-vol{book[:len(book)-4]}.txt", "w", encoding="utf8")
    with open(f"./bad_txt/{book}", encoding="utf8") as text:
        for line in text:
            if line.strip():
                content = line.strip() + " " 
                f.write(content)
    f.close()
