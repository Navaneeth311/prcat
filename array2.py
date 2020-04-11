string_count = int(input("Enter the number of strings = "))
strings = []

for _ in range(string_count):
    string_items = input("Enter strings = ")
    strings.append(string_items)

query_count = int(input("Enter the query count = "))
query = []

for _ in range(query_count):
    query_item = input("Enter the quries = ")
    query.append(query_item)

def recurring_count(strings, query):
    count = []
    for i in range(query_count):
        count_item = 0
        for j in range(string_count):
            if query[i] == strings[j]:
                count_item = count_item+1
                continue
        count.append(count_item)
    return count


res =recurring_count(strings,query)
print("\n".join(map(str,res)))