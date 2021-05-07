f = open("output.txt", "w", encoding="utf8")
with open('v1.txt', encoding="utf8") as text:
    for line in text:
        if line.strip():
            content = line.strip() + " " 
            f.write(content)
f.close()