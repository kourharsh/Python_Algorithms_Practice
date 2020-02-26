class Solution:
    def __init__(self):
        self.str = None

    def suggestedProducts(self, products, searchWord):

        class TrieNode():
            def __init__(self, letter):
                self.letter = letter
                self.children = {}
                self.is_end = False

        class Trie():
            def __init__(self):
                self.root = TrieNode("*")

            def add_word(self, word):
                current = self.root
                for letter in word:
                    if letter not in current.children:
                        current.children[letter] = TrieNode(letter)
                    current = current.children[letter]
                current.is_end = True

            def check_word(self, word):
                word = word.lower()
                current = self.root
                for letter in word:
                    if letter not in current.children.keys():
                        return False
                    else:
                        current = current.children[letter]
                return current.is_end

            def find_word(self, word):
                listwords = []
                current = self.root
                for letter in word:
                    if letter not in current.children:
                        return False, current, listwords
                    else:
                        current = current.children[letter]
                if current.is_end and not current.children:
                    listwords.append(word)
                    return False, current, listwords
                else:
                    #print(current.children)
                    return True, current, listwords

            def recursive_fetch(self, current, listwords, word):
                if current.is_end:
                    #print(current.letter)
                    listwords.append(word)

                for a, n in current.children.items():
                    #print(current.children.items())
                    #print(a)
                    #print(n.letter)
                    self.recursive_fetch(n, listwords, word + a)

                return listwords

        trie = Trie()
        list_ma = []

        for i in range(0, len(products)):
            trie.add_word(products[i])

        #print(trie.check_word("mouse"))
        #print(trie.check_word("mousepad"))

        for i in range(1, len(searchWord)+1):
            #print(searchWord[0:i])
            flag, current, listwords = trie.find_word(searchWord[0:i])
            if flag:
                listwords = trie.recursive_fetch(current, listwords, searchWord[0:i])
                if len(listwords) > 3:
                    listwords.sort()
                lnew = sorted(listwords[0:3])
                list_ma.append(lnew)
            else:
                list_ma.append(listwords)

        return list_ma

sol = Solution()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
word = "mouse"
print("Products are:")
print(products)
print("Word to be searched: " + word)
print("Suggestions are : ")
print(sol.suggestedProducts(products, word))

products = ["bags","baggage","banner","box","cloths"]
word = "bags"
print("Products are:")
print(products)
print("Word to be searched: " + word)
print("Suggestions are : ")
print(sol.suggestedProducts(products, word))

