def contacts(contact_dict, query):
    count = contact_dict.get(query, 0)
    return count

if __name__ == '__main__':

    queries_rows = int(input())

    contact_dict = {}

    for i in range(0, queries_rows):
        query = input().rstrip().lower().split(' ')
        if query[0].lower() == 'add':
            for j in range(1, len(query[1]) + 1):
                keys = query[1][0:j]
                val = contact_dict.get(keys, 0)
                contact_dict[keys] = val + 1
            # print(contact_dict)
        elif query[0].lower() == 'find':
            result = contacts(contact_dict, query[1])
            print(str(result))


