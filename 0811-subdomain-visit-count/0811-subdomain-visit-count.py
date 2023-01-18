class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        


        mycounter = Counter()

        for each_cpdomanins in cpdomains:
            # the below code will split the number part and the domains 
            count , *domains = each_cpdomanins.replace(" ",".").split(".")

            # now for each domain we will add every possible domain and count them 

            for i in range(len(domains)):
                mycounter[".".join(domains[i:])] += int(count) 

        # finally return the complete counted values
        return [str(value)+" "+key for key,value in mycounter.items()]

    