from beautifultable import BeautifulTable

table = BeautifulTable()
table.columns.header = ["Name", "Frequency"]

text = input("Please Enter Text: ").lower()

for char in sorted(set(text)) :
    if char.isalpha():
        table.rows.append([char, text.count(char)])

print(table)