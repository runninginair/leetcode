''' 71. Simplify Path

Medium      3.4K       672      Companies

Given a string path, which is an absolute path (starting with a slash '/') to
a file or directory in a Unix-style file system, convert it to the simplified
canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a
double period '..' refers to the directory up a level, and any multiple
consecutive slashes (i.e. '//') are treated as a single slash '/'. 
For this problem, any other format of periods such as '...' are treated as
file/directory names.

The canonical path should have the following format:

 * The path starts with a single slash '/'.
 * Any two directories are separated by a single slash '/'.
 * The path does not end with a trailing '/'.
 * The path only contains the directories on the path from the root directory
   to the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.


Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.


Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root
level is the highest level you can go.


Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced
by a single one.
 

Constraints:    1 <= path.length <= 3000
                path consists of English letters, digits, period '.', slash '/' or '_'.
                path is a valid absolute Unix path.
Accepted:           501.8K
Submissions:        1.3M
Acceptance Rate:    39.4%
'''

class Solution:     ### Passed.
    def simplifyPath(self, path: str) -> str:
        ptr, n, que = 0, len(path), []
        while ptr < n:
            if path[ptr] == '/':
                while ptr + 1 < n and path[ptr + 1] == '/': ptr += 1
                if not que or (que and que[-1] != '/'): que.append('/')

            elif path[ptr] == '.':
                curr, cntDot, isFile = ptr, 1, False
                while ptr + 1 < n and path[ptr + 1] == '.':
                    cntDot += 1
                    ptr += 1
                while ptr + 1 < n and path[ptr + 1] != '/':
                    ptr += 1
                    isFile = True
                if isFile or cntDot > 2:
                    que.append(path[curr: ptr + 1])
                elif cntDot == 2:
                    if (ptr + 1 < n and path[ptr + 1] == '/') or ptr == n - 1:
                        if len(que) > 1 and que[-1] == '/':
                            que.pop()
                            que.pop()
            else:
                cur = ptr
                while ptr+1 < n and path[ptr + 1] != '/': ptr += 1
                que.append(path[cur: ptr + 1])
            ptr += 1
        # while que and que[0] == '.': que.pop(0)
        if que and que[-1] == '/': que.pop()
        return '/' if not que else "".join(que)


class Solution_v2:
    def simplifyPath(self, path: str) -> str:
        dir_stack = []
        path = path.split("/")
        for elem in path:
            if dir_stack and elem == "..":
                dir_stack.pop()
            elif elem not in [".", "", ".."]:
                dir_stack.append(elem)
                
        return "/" + "/".join(dir_stack)


def main():

    sol = Solution()
    sol = Solution_v2()


    path = "/home/"                 # Output: "/home"
    print(sol.simplifyPath(path))

    path = "/../"                   # Output: "/"
    print(sol.simplifyPath(path))

    path = "/home//foo/"            # Output: "/home/foo"
    print(sol.simplifyPath(path))

    path = "/a/./b/../../c/"        # Output: "/c"
    print(sol.simplifyPath(path))

    path = "/..hidden"              # Output: "/..hidden"
    print(sol.simplifyPath(path))

    path = "/a//b////c/d//././/.."  # Output: "/a/b/c"
    print(sol.simplifyPath(path))

    path = "/.hidden"               # Output: "/.hidden"
    print(sol.simplifyPath(path))

    path = "/hello../world"         # Output: "/hello../world"
    print(sol.simplifyPath(path))

    ### Testing case: 258/258
    path = "/home/foo/.ssh/../.ssh2/authorized_keys/"  # "/home/foo/.ssh2/authorized_keys"
    print(sol.simplifyPath(path))


if __name__ == "__main__":
    main()
