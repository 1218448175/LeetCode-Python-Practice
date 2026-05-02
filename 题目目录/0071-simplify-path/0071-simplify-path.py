class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directory_list = path.split('/')
        for directory in directory_list:
            if directory == '..':
                if stack:
                    stack.pop()
            elif directory != '.' and directory != '':
                stack.append(directory)
        return '/' + '/'.join(stack)
        