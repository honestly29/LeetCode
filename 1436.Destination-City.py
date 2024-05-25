class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        setA = set()
        setB = set()

        for path in paths:
            setA.add(path[0])
            setB.add(path[1])
        

        for city in setB:
            if city not in setA:
                return(city)