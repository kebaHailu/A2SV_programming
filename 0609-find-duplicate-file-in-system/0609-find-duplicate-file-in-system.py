class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for line in paths:
            data = line.split()
            root = data[0]
            for file in data[1:]:
                
                # used to distribute the data into partition and find the file content
                name, nums , content = file.partition('(')
                dic[content[:-1]].append(root + '/' + name)

        final_list = [i for i in dic.values() if len(i)>1] 
        
        return  final_list 