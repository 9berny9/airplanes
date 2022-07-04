from utils import AirportUtils

# test cases copied from the mail
# test_cases = [
#     ([155, 55, 2, 96, 67, 203, 3], 454),
#     ([155, 54, 3, 10], 165),
#     ([12, 43, 10, 8, 90, 123, 5, 3, 56], 230),
#     ([1, 10, 200, 154, 160, 289, 454, 5, 10, 34], 849),
#     ([347, 440, 342, 297, 104, 118, 119, 268, 218], 1130),
#     ([463,  73, 282, 422, 271, 118, 112], 1128)
# ]

if __name__ == "__main__":
    test = [
        [155, 55, 2, 96, 67, 203, 3],
        [155, 54, 3, 10],
        [12, 43, 10, 8, 90, 123, 5, 3, 56],
        [1, 10, 200, 154, 160, 289, 454, 5, 10, 34],
        [347, 440, 342, 297, 104, 118, 119, 268, 218],
        [463,  73, 282, 422, 271, 118, 112]
    ]
    
    au = AirportUtils()
    for airportQueue in test:
        maxCheckedPassengers = au.maximizeLanding(airportQueue)
        print(maxCheckedPassengers)
