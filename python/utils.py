class Utils:
    '''
    Basic function to help with computation.  
    '''

    def __init__(self) -> None:
        pass

    def sumOfList(self, aList: list, size: int):
        if (size == 0):
          return 0
        else:
          return aList[size - 1] + self.sumOfList(aList, size - 1)

    @staticmethod
    def listsMultiplier(aList: list, bList: list) -> list:
        if (len(aList) == len(bList)):
            if len(aList) == 0:
                return []
            else:
                return [aList[i] * bList[i] for i in range(len(aList))]
        else:
            return []

class AirportUtils(Utils):
    '''
    More specific function related to the issue itself.
    detectTurbulence: returns the fact if there is a danger of turbulence for a given itenerary
    generate: generates {0,1}-permutations for a given length
    maximizeLanding: computes all allowed itineraries and finds maximum
        if there is more than 1 maximum func returns only the the first one! No other criterias are considered.
    '''
    def __init__(self) -> None:
        super().__init__()

    def detectTurbulence(self, locList: list) -> bool:
        repList = locList[1:]
        repList.append(0)
        mult = [locList[i] * repList[i] for i in range(len(locList))]
        if self.sumOfList(mult, len(mult)) == 0:
            return False
        else:
            return True

    def generate(self, ones: int, zeroes: int, locList: list, len1: int) -> list:
        global perms
        # If permutation is full append it to set of all permutatations
        if (len1 == len(locList)):
            perms.append(locList)
            return 

        # Append a 1 and recur
        self.generate(ones+1, zeroes, locList + [1], len1)
    
        # Append a 0 as well, and recur
        self.generate(ones, zeroes+1, locList + [0], len1)

    def maximizeLanding(self, airportQueue: list) -> tuple:
        locLenght = len(airportQueue)
        global perms
        perms = []
        l = []
        self.generate(0,0,l,locLenght)
        turbulenceFreeItineraries = [el for el in perms if not self.detectTurbulence(el)]
        safeCheckNumber = [
            (
                itin,
                self.sumOfList(self.listsMultiplier(airportQueue, itin), len(airportQueue))
            )
                 for itin in turbulenceFreeItineraries
        ]

        return max(safeCheckNumber, key = lambda i : i[1])
