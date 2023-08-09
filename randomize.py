    # imports
import os
import shutil
import random
import numpy as np
import time

# missions list

if os.path.exists("missionshuffle"):
    shutil.rmtree("missionshuffle", ignore_errors=True)

# create directories
os.mkdir("missionshuffle")

missions_in_order = [
    #"1_01.lur",
    "1_02.lur",
    "1_02A.lur",
    "1_02B.lur",
    "1_02C.lur",
    "1_03.lur",
    #"1_04.lur",
    "1_05.lur",
    #"1_E01.lur",
    "1_07.lur",
    "1_08.lur",
    "1_09.lur",
    #"1_10.lur",
    #"1_11xp.lur",
    "1_B.lur"
]


missions_list = [
    # first missions
    # never softlock
    # put any order
    [
        "1_08.lur", "1_03.lur", "1_09.lur",   #"1_01.lur" #"1_04.lur" 
    ],
    [
        "1_05.lur", "1_07.lur",  "1_02B.lur", "1_02.lur",  "1_B.lur", "1_02A.lur", "1_02C.lur" #"1_E01.lur",    #"1_10.lur",
    ]
]

pairs = []

j = 0
for i in range(len(missions_list)):
    for k in range(len(missions_list[i])):
        mission1 = missions_in_order[j]
        random.shuffle(missions_list[i])
        #print(missions_list[i])
        pairs.append([mission1, missions_list[i][0]])
        #print(mission1)
        missions_list[i].pop(0)
        j = j + 1

for mission1, mission2 in pairs:
    print("INJECTING SCRIPT: ", mission1, "->", mission2)
    shutil.copy("./lurfiles/"+mission2, "./missionshuffle")
    os.rename("./missionshuffle/"+mission2, "./missionshuffle/"+mission1)
    os.system('img -open "../Scripts.img" -add ' + "./missionshuffle/" + mission1 + ' -rebuild')

print("SCRIPTS SUCCESSFULLY RANDOMIZED")