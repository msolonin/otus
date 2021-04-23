from allpairspy import AllPairs

data = [
    ["DELL", "ACER", "ASUS", "MS"],
    ["WIN7", "XP", "WIN10", "WIN8"],
    ["AMD", "INTEL", "ARM64", "ARMv7"],
    ["CHROME", "FIREFOX", "IE11", "SAFARI"]
]

# pairwised_result = AllPairs(data)
#
# for i, el in enumerate(pairwised_result):
#     print(i+1, el)
#
# print("=" * 20 + " End Pairwised Test")

i = 1
for comp in data[0]:
    for oper in data[1]:
        for proc in data[2]:
            for browser in data[3]:
                print(i, [comp, oper, proc, browser])
                i += 1
