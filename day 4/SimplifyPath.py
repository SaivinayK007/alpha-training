class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//" ,'/')
        path = path.replace("///" , '/')

        path = path.split("/")

        paths = list()

        for s in path:
            if s== '' or s == '.':continue 
            if s == '..':
                if paths:
                    paths.pop()
            else:
                paths.append(s)
        
        return '/' + '/'.join(paths)
