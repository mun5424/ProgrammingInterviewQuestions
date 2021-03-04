class Trie:
    def __init__(self, x):
        self.val = x
        self.children = []
        self.isWord = False
        
def validDictionaryWord(digits, dictionary):
    # dictionary = ['a', 'also' ,' best', 'bluestorm']
    key_map = ['', '', 'abc','def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    root = Trie(None)
    for i in range(len(dictionary)): 
        addToTrie(dictionary[i])
    
    # 23232
    for i in range(len(digits)):
        # 2, 23, 232
        possible_chars = digits(int(digits[i]))
        for j in range(possible_chars):
            char = possible_chars[i]
            if char in root.children: 
                trie = root
                while (len(trie.children > 0)):
                    pass
                

def dfs(trie, result_array, key_map, current_word, index): 
    if trie.isWord:
        result_array.append(current_word)
    for c in key_map[index]: 
        current_word.append(c)
        dfs(trie, result_array, key_map, current_word, index + 1)


def dfs(root):
    return root.val if not root.left else dfs(root.left)




            
            

def addToTrie(root, word): 
    trie = root
    for i in range(len(word)):
        char = word[i]
        if trie.children.keys():
            trie.children[Trie(char)]
        trie = trie.children[char]
    trie.isWord = True

def printTrie(root): 
    if root:
        print(root.val)
        print(root.children)

list = ['a', 'abc' , 'abcd'] 
root = Trie('a')
addToTrie(root, 'a')
addToTrie(root, 'ab')
addToTrie(root, 'ac')
printTrie(root)


```
def valid_dict_word2(phone, dict):
    trie = build_trie(dict)
    digit_map = {}

    results = []
    def dfs(root, so_far, rest):
        if root.isWord:
            results.append(so_far)
        if not rest:
            return
        digit, rest = rest[0], rest[1:]
        for choice in digit_map[digit]:
            if choice in root.children:
                dfs(root.children[choice], so_far + choice, rest)
    dfs(trie, '', phone)
    return results
```