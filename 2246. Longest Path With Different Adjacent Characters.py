''' 2246. Longest Path With Different Adjacent Characters

Hard    1.2K    26     Companies

You are given a tree (i.e. a connected, undirected graph that has no cycles)
rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is
represented by a 0-indexed array parent of size n, where parent[i] is the
parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned
to node i.

Return the length of the longest path in the tree such that no pair of adjacent
nodes on the path have the same character assigned to them.


Example 1:
Input: parent = [-1, 0, 0, 1, 1, 2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different
characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3,
so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 

Example 2:
Input: parent = [-1, 0, 0, 0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different
characters is the path: 2 -> 0 -> 3. The length of this path is 3,
so 3 is returned.
 

Constraints:        n == parent.length == s.length
                    1 <= n <= 10^5
                    0 <= parent[i] <= n - 1 for all i >= 1
                    parent[0] == -1
                    parent represents a valid tree.
                    s consists of only lowercase English letters.
Accepted:           29.3K
Submissions:        57.3K
Acceptance Rate:    51.1%
'''

from typing import List

''' Official Java Solution
class Solution {
    private int longestPath = 1;

    public int dfs(int currentNode, Map<Integer, List<Integer>> children, String s) {
        // If the node is the only child, return 1 for the currentNode itself.
        if (!children.containsKey(currentNode)) {
            return 1;
        }

        // Longest and second longest path starting from currentNode (does not count the
        // currentNode itself).
        int longestChain = 0, secondLongestChain = 0;
        for (int child : children.get(currentNode)) {
            // Get the number of nodes in the longest chain starting from the child,
            // including the child.
            int longestChainStartingFromChild = dfs(child, children, s);
            // We won't move to the child if it has the same character as the currentNode.
            if (s.charAt(currentNode) == s.charAt(child)) {
                continue;
            }
            // Modify the longestChain and secondLongestChain if longestChainStartingFromChild
            // is bigger.
            if (longestChainStartingFromChild > longestChain) {
                secondLongestChain = longestChain;
                longestChain = longestChainStartingFromChild;
            } else if (longestChainStartingFromChild > secondLongestChain) {
                secondLongestChain = longestChainStartingFromChild;
            }
        }

        // Add "1" for the node itself.
        longestPath = Math.max(longestPath, longestChain + secondLongestChain + 1);
        return longestChain + 1;
    }

    public int longestPath(int[] parent, String s) {
        int n = parent.length;
        Map<Integer, List<Integer>> children = new HashMap<>();
        // Start from node 1, since root node 0 does not have a parent.
        for (int i = 1; i < n; i++) {
            children.computeIfAbsent(parent[i], value -> new ArrayList<Integer>()).add(i);
        }

        dfs(0, children, s);

        return longestPath;
    }
}

'''

class Solution:     ### Official Java Solution to Python
    def longestPath(self, parent: List[int], s: str) -> int:
        self.longestPath = 1
        n = len(parent)
        children = {}
        ### Start from node 1, since root node 0 does not have a parent.
        for i in range(1, n):
            if parent[i] in children: children[parent[i]].append(i)
            else: children[parent[i]] = [i]
        # print(children)

        def dfs(currentNode: int, children, s: str) -> int:
            ### If the node is the only child, return 1 for the currentNode itself.
            if currentNode not in children: return 1
            
            ### Longest and second longest path starting from currentNode (does not count the currentNode itself).
            longestChain = secondLongestChain = 0

            for child in children[currentNode]:
                longestChainStartingFromChild = dfs(child, children, s)
                ### Get the number of nodes in the longest chain starting from the child, including the child.
                if s[currentNode] == s[child]: continue
                ### Modify the longestChain and secondLongestChain if longestChainStartingFromChild is bigger.
                if longestChainStartingFromChild > longestChain:
                    secondLongestChain = longestChain
                    longestChain = longestChainStartingFromChild
                elif longestChainStartingFromChild > secondLongestChain:
                    secondLongestChain = longestChainStartingFromChild

            ### Add "1" for the node itself.
            self.longestPath = max(self.longestPath, longestChain + secondLongestChain + 1)
            return longestChain + 1
        
        dfs(0, children, s)

        return self.longestPath


class Solution_v1:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.longestPathRes, n, children = 1, len(parent), {}
        for i in range(1, n):
            if parent[i] in children: children[parent[i]].append(i)
            else: children[parent[i]] = [i]

        def dfs(currentNode) -> int:
            if currentNode not in children: return 1
            longestChain = secondLongestChain = 0

            for child in children[currentNode]:
                longestChainStartingFromChild = dfs(child)
                if s[currentNode] == s[child]: continue
                if longestChainStartingFromChild > longestChain:
                    secondLongestChain = longestChain
                    longestChain = longestChainStartingFromChild
                elif longestChainStartingFromChild > secondLongestChain:
                    secondLongestChain = longestChainStartingFromChild

            self.longestPathRes = max(self.longestPathRes, longestChain + secondLongestChain + 1)
            return longestChain + 1
        
        dfs(0)

        return self.longestPathRes


def main():
    sol = Solution()
    sol = Solution_v1()

    parent, s = [-1, 0, 0, 1, 1, 2], "abacbe"
    print(sol.longestPath(parent, s)) # Output: 3

    parent, s = [-1, 0, 0, 0], "aabc"
    print(sol.longestPath(parent, s)) # Output: 3


if __name__ == "__main__":
    main()
