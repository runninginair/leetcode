''' 0211. Design Add and Search Words Data Structure

Medium      5.9K      340       Companies

Design a data structure that supports adding new words and finding if a string
matches any previously added string.

Implement the WordDictionary class:

 * WordDictionary() Initializes the object.

 * void addWord(word) Adds word to the data structure, it can be matched later.

 * bool search(word) Returns true if there is any string in the data structure
   that matches "word" or false otherwise. "word" may contain dots '.' where
   dots can be matched with any letter.
 

Example:

Input
["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
[[],               ["bad"],   ["dad"],   ["mad"],   ["pad"],  ["bad"],  [".ad"],  ["b.."]]

Output
[null,             null,      null,      null,      false,    true,     true,     true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:        1 <= word.length <= 25
                    word in addWord consists of lowercase English letters.
                    word in search consist of '.' or lowercase English letters.
                    There will be at most 3 dots in word for search queries.
                    At most 10^4 calls will be made to addWord and search.
Accepted:           472.3K
Submissions:        1.1M
Acceptance Rate:    43.0%
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.is_word

            if word[idx] == '.':
                for child in node.children.values():
                    if dfs(child, idx + 1): return True

            if word[idx] in node.children:
                return dfs(node.children[word[idx]], idx + 1)
        return dfs(self.root, 0)                 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

#       a   p   p   l   e
#       b   p   p   i   e   e
#       c   p   p   e   e

#           .   p   e   .