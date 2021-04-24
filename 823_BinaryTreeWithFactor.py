"""
Given an array of unique integers, each integer is strictly greater than 1.
- We make a binary tree using these integers and each number may be used for any number of times.
- Each non-leaf node's value should be equal to the product of the values of it's children.
How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.
"""
from typing import List


def num_factored_binary_trees(int_arr: List[int]) -> int:
    """
    Dynamic Programming Approach

    :param int_arr: an array of unique integers, each integer is strictly greater than 1
    :return: answer modulo 10 ** 9 + 7
    """
    _mod_value = 10 ** 9 + 7
    int_arr.sort()
    lookup_map = {a_i: i for i, a_i in enumerate(int_arr)}
    # dp_memory[i] stores # of factor binary tree with int_arr[i] as root node
    dp_memory = [1] * len(int_arr)
    for i, a_i in enumerate(int_arr):
        for a_j in int_arr[:i]:
            if a_i % a_j == 0 and a_i / a_j in lookup_map and a_j * a_j <= a_i:
                if a_j * a_j < a_i:
                    # Left Child and Right Child can swap
                    dp_memory[i] += (2 * dp_memory[lookup_map[a_j]] * dp_memory[lookup_map[a_i / a_j]]) % _mod_value
                else:
                    # Left Child and Right Child have same value, cannot swap
                    dp_memory[i] += (dp_memory[lookup_map[a_j]] * dp_memory[lookup_map[a_i / a_j]]) % _mod_value

    return sum(dp_memory) % _mod_value


test_cases = [([2, 4], 3),
              ([2, 4, 5, 10], 7),
              ([242, 315, 26, 27, 16, 337, 75, 371, 253, 67, 105, 327, 96, 373, 113, 167, 3, 99, 193], 21),
              ([971588554, 520749447, 513757887, 356788063, 379421244, 334699070, 801826060, 638738612, 653781951,
                460666710, 807141900, 929231987, 297512619, 6379760, 489106943, 628271028, 340935071, 967513857,
                180148101, 761244375, 597342008, 615772190, 724451136, 156377973, 688556948, 831332491, 733176736,
                208041691, 389648590, 161022238, 515610564, 150675857, 509429598, 823949222, 588859735, 453671129,
                30238374, 824683171, 131803832, 892866393, 107942717, 560039467, 143093909, 997422290, 194174308,
                862589146, 818071068, 693274617, 185009960, 693700721, 58513372, 438718445, 287965773, 689582058,
                614172953, 700651151, 261372170, 75354128, 147909532, 17228919, 715958073, 136158414, 331954012,
                185618368, 862734075, 707150336, 728938522, 162008403, 172786110, 280903590, 343005938, 244111565,
                855806684, 589965235, 126901051, 306282962, 770459398, 921746511, 703761214, 421881560, 234488692,
                727254497, 2759161, 670049873, 922168104, 260297905, 531652898, 982438210, 225731770, 816657952,
                980558196, 394321587, 461519578, 184495724, 664385099, 869060936, 271278958, 456998531, 871564841,
                194362094], 100),
              ([277175715, 645202070, 364632537, 989641912, 828726955, 516494729, 744368921, 787673501, 565349276,
                66362806, 569924966, 992821705, 122920640, 109930324, 835922180, 520204529, 835084297, 236498012,
                928248777, 141110751, 489261337, 649156648, 436578721, 910801047, 773574661, 518559104, 795556604,
                298295858, 566409758, 414558765, 252901034, 671475249, 575646220, 741223205, 928095754, 510826559,
                887250629, 309285712, 262726698, 583185947, 944200547, 361273025, 347143430, 711037876, 901756858,
                876533036, 401578972, 469285200, 613003678, 567205063, 864446653, 766144361, 999084821, 608567724,
                343829933, 231868180, 357142488, 656000024, 237356328, 92565745, 361494546, 260481036, 682440284,
                171822263, 33077720, 948703316, 696488817, 728466589, 509731246, 825634565, 151114491, 403117346,
                571434854, 607418837, 679569068, 197169383, 351185558, 907367299, 622611356, 589019084, 45799396,
                89709896, 83215058, 503426624, 8365368, 956759174, 234401323, 235198746, 690163075, 570111871,
                988501540, 189310016, 953906949, 811004260, 254259160, 167530127, 827678587, 184445459, 570098221,
                67682587, 614451652, 898798505, 304380490, 492503762, 707094947, 73340284, 920013951, 360441281,
                613354450, 43757272, 564540965, 367111634, 165073831, 841678358, 266297393, 718736228, 83209123,
                460661050, 347699330, 516825761, 114617039, 792371739, 717055186, 912281720, 752602462, 584146035,
                512604300, 348214514, 637393422, 617410916, 613512645, 116593793, 118365485, 716474963, 15158299,
                518429649, 360208903, 252402771, 79001902, 811481106, 554493548, 378546164, 861472182, 725617813,
                298734924, 917496962, 400471114, 211769619, 754110450, 671480369, 526023032, 963811156, 834476875,
                594080945, 519524599, 243890537, 755770534, 513807837, 166280763, 210308243, 753326440, 39078868,
                991125311, 487851164, 360295778, 541237452, 846997985, 154397235, 730999939, 455808341, 34916455,
                529706386, 371476236, 520557288, 594869694, 81289829, 73280673, 434755857, 121940467, 867320973,
                198342674, 649198480, 705456495, 929422329, 167216453, 154126563, 378166783, 909092672, 414445172,
                373734485, 225653324, 338482580, 471861963, 405183160, 894697885, 948412087, 277889875, 378761695,
                167579397, 598204636, 981960810, 554530174, 17604289, 751354813, 344122557, 560600534, 515691347,
                325048834, 888643661, 10803273, 642799919, 550531009, 193903787, 948351310, 940955846, 394398261,
                445655732, 388279110, 102081585, 939864945, 418401556, 998746596, 293329937, 145388523, 431956499,
                673015184, 775204641, 901160221, 911790557, 940184273, 208407398, 803283409, 861220895, 132619735,
                211057147, 435522876, 830910180, 485677380, 287640886, 618196005, 730926723, 120324880, 975112154,
                232982323, 601605873, 152906533, 642364982, 888424983, 566598920, 13313656, 664406132, 671322758,
                667442643, 30905309, 766150142, 220133474, 885841616, 679921351, 253924085, 872137052, 947150175,
                824466351, 409627566, 604896674, 269129684, 811915820, 349432521, 486699205, 492407657, 739762626,
                13706702, 323824148, 888236788, 365167912, 176227434, 806512147, 405441815, 741822623, 140684485,
                400598955, 525127675, 806585174, 636775981, 8660655, 474414188, 906749397, 573598822, 849463007,
                604708531, 396893916, 868055685, 775939575, 774893615, 631835248, 953960030, 718440370, 868083009,
                281535368, 440797455, 135118915, 851443387, 268625954, 626134542, 838457038, 502295824, 904492720,
                16957281, 296591012, 486504084, 332930135, 680467725, 567631364, 913563099, 346241212, 419824836,
                623814442, 432096253, 166002102, 741319754, 687562955, 624928708, 202449202, 606047867, 726687190,
                933533473, 183549945, 34689390, 559510190, 294119579, 921664913, 839651177, 448676502, 950530672,
                261205560, 236134283, 834435116, 722093036, 67873812, 101045912, 916626662, 213643486, 344348505,
                134060088, 288614510, 410945011, 691415883, 608883383, 623530769, 759338111, 664150714, 779387779,
                901668099, 143769465, 667614736, 222667159, 197850671, 435453310, 958237638, 641685586, 27472482,
                864168509, 89350753, 436729898, 300074951, 667587564, 944402412, 427220826, 218427294, 1327754,
                553949051, 19753043, 250029580, 284610098, 961993817, 206893989, 182239044, 211635057, 195713702,
                532660903, 456606473, 301435037, 226573604, 222757599, 695800483, 972616082, 362615751, 611650262,
                75812005, 368633882, 389718394, 344459078, 942736641, 798952966, 361028552, 947487627, 589692530,
                2838086, 285401227, 637904441, 733913350, 162419548, 683429791, 829682808, 447137181, 978367683,
                283202690, 578838186, 605737356, 591211483, 569320785, 586137801, 804149725, 664333774, 146249644,
                253241142, 355385804, 964323049, 595852969, 911668511, 137058035, 715183746, 59487219, 83737772,
                277933440, 166564273, 644069307, 623671394, 299037128, 885572724, 712266264, 156135124, 359566651,
                978969920, 78499080, 470776816, 719074486, 916351348, 753209926, 723213011, 8435261, 980498567,
                380466185, 935905192, 721689984, 170248512, 160768456, 231304887, 643561292, 328678264, 511383233,
                475162800, 34644875, 695735971, 574160186, 644586367, 578334624, 344396755, 714571112, 76253313,
                929232798, 997226705, 813782851, 513225900, 197501811, 570706425, 500183988, 618606158, 736260308,
                102522822, 36469719, 299560592, 423911440, 972788574, 829986549, 303634084, 569748322, 905123866,
                436856329, 39086681, 135792458, 792107556, 333824922, 842613566, 576514620, 123892611, 265503587,
                524590982, 69275403, 173188614, 784883058, 527470357, 714886172, 411280532, 183864705, 410540739,
                957194274, 571109513, 21607876, 938944360, 773654033, 355627408, 526474049, 521222401, 331190878,
                52612191, 461634994, 225974348, 52081425, 781201466, 950680306, 77057075, 829303028, 886921747,
                129171660, 980754891, 979743883, 164509875, 234425633, 188773795, 90668852, 76726925, 328952673,
                977785665, 432910206, 744013967, 543395817, 521054780, 49362843, 619253271, 25770173, 156609918,
                351561872, 977937336, 417869406, 722154516, 877490941, 629282132, 304702114, 496347475, 393887738,
                639859757, 844430292, 264088711, 531928383, 589697576, 35747046, 923226305, 376187752, 522431843,
                926380344, 949517035, 67282298, 910114873, 604483224, 888165508, 861181016, 894925005, 276553687,
                169981929, 808831093, 715403263, 97764536, 366792405, 148401696, 941550070, 756819067, 109961267,
                341646584, 754608275, 225890715, 412850283, 173307274, 635929236, 153676640, 36082505, 48058509,
                18109964, 376431776, 871826241, 108243316, 846355486, 914570580, 556530516, 159166747, 795605862,
                910823740, 507580856, 137937769, 832058698, 446434042, 262232722, 502471844, 643731966, 888999144,
                663439502, 894120445, 328533147, 661813194, 174422816, 450818266, 745517971, 632111403, 718670013,
                53488636, 263082467, 342963918, 877352517, 396220269, 997583980, 837672364, 32875168, 339608727,
                82864807, 257917421, 966264232, 118567826, 838297, 897728092, 796920533, 786165025, 607251970,
                481423369, 356327786, 771925143, 832054191, 578893052, 222121584, 82321099, 474364752, 586537922,
                584521103, 435546838, 511364930, 339375041, 580938383, 765143750, 464363311, 548929015, 780418460,
                175303067, 18633352, 99765597, 797585420, 357929488, 246561694, 820106728, 526272370, 644020146,
                952919041, 351790208, 654034467, 980363997, 962989721, 378820231, 344801071, 662646506, 697532621,
                402966867, 609748224, 355413558, 838237902, 7211260, 422933955, 573091756, 742546758, 444056630,
                779727840, 64931068, 909678912, 710942539, 840681037, 820758326, 168464032, 472083779, 14832511,
                580458405, 22510446, 662851796, 535454204, 79699304, 11668403, 793921408, 882050473, 37382996,
                640074009, 526400448, 351601557, 528482509, 377696833, 228654326, 73288137, 620981853, 941512899,
                83819421, 645182437, 938552729, 676033284, 831342562, 105799236, 632349562, 626209098, 520950008,
                430804676, 659810686, 925685369, 515012126, 709374966, 714488893, 884278347, 561367332, 726742135,
                148141778, 653335839, 606692007, 554674478, 835427604, 332725045, 545189107, 905677818, 286082771,
                635249124, 782952287, 104828280, 167605384, 502500267, 578453626, 20187484, 748995880, 506001559,
                437164976, 598420284, 403948116, 369514237, 470279153, 984253780, 432882272, 44068797, 334482160,
                914568018, 456172283, 554620845, 29700973, 399998616, 746398960, 628741213, 987583913, 459540303,
                590102724, 157082912, 810014140, 565053765, 491574480, 837589207, 631776844, 860957509, 913489825,
                475067028, 375870370, 281300881, 376330117, 67682436, 381564191, 413254577, 42428584, 754176951,
                370060002, 622410107, 483943547, 147513811, 607831311, 200308118, 91098725, 381634800, 744679270,
                924259680, 925857531, 538920949, 880446905, 746563995, 923567926, 358873278, 711688776, 661603127,
                9513214, 967803036, 1283983, 501490046, 390028966, 522998045, 386168077, 399477590, 302046965, 8860865,
                230188138, 152203631, 536304560, 174041347, 396410471, 741122702, 732982587, 416425121, 498530743,
                586836933, 777159823, 796671581, 895821093, 144310878, 946806285, 803223216, 475941610, 523380038,
                889583930, 509481706, 521049032, 609576556, 437643835, 595966729, 833134499, 885769548, 653253281,
                525170156, 434417043, 911306075, 645242588, 376283568, 741235651, 362467983, 904878610, 693748556,
                763813351, 504252828, 428683797, 718007098, 883410088, 773836047, 526468838, 17783175, 272874751,
                251755092, 980504038, 392242680, 747729675, 331306210, 476563176, 68444018, 9967213, 249408089,
                450359157, 811158096, 861238126, 941793398, 376277094, 715077647, 317675157, 77937106, 604988944,
                649536231, 894068622, 457851953, 282388742, 832932326, 61791080, 437970820, 591568668, 710677181,
                691575869, 692465985, 839026800, 998177996, 449946898, 108472878, 585173385, 997305296, 565568592,
                461874572, 429139043, 535692218, 517041022, 389904517, 813012906, 563785093, 211615051, 816344794,
                199013964, 405481770, 527006118, 449848653, 199675318, 906924957, 433428953, 107637958, 444033788,
                365041815, 646719331, 309645690, 184898752, 408794686, 298633657, 978190234, 992637103, 323150325,
                804100446, 319567860, 893926696, 526070444, 957726158, 846873545, 442352342, 736579230, 842022592,
                801934907, 699089932, 309388516, 36382907, 365274794, 187636444, 34776105, 86101036, 962933221,
                498863810, 877495995, 685098208, 632324649, 128152463, 866495241, 232335752, 4557072, 660105624,
                777797140, 684709078, 709864141, 171419181, 799108088, 300200856, 808997306, 586573065, 441002205,
                679858729, 538553087, 787537626, 976208665, 447544017, 64617769, 958043957, 577059550, 923798469,
                531857052, 805178338, 508631533, 287575619, 226264211, 115801442, 679319866, 643883590, 950592754,
                833971266, 820583092, 405196429, 634297097, 111185557, 200171804, 563461734, 545736076, 689190873,
                131695582, 357152244, 235319442, 685101024, 681330702, 769624500, 923164068, 283707156, 397643520,
                88911325, 288386638, 825963922, 828277947, 197833549, 543803880, 135519431, 70625116, 719306090,
                904011526, 258402863, 914849220, 431739659, 353602410, 994742483, 870361812, 768937324, 935333864,
                927572969, 869204616, 977762425, 749941379, 573258055, 645631624, 208802226, 94109095, 439392875],
               1000),
              ([767520, 91499520, 1336764, 41598354, 48070400, 14676480, 51781632, 45603480, 43200, 5640, 665, 67392000,
                258876, 177553950, 281424, 838515600, 88179840, 695705472, 53143734, 670320, 806, 647534592, 289476000,
                259616700, 538989360, 18461520, 493722432, 372960, 49, 9013200, 1462, 160496640, 8262, 551110560,
                394740, 3455060, 9752400, 375840, 18079200, 516, 51, 57542400, 1864800, 7215744, 1380672, 33601920,
                14403840, 20, 8536704, 58373172, 802433016, 21471480, 1129392, 460, 413540, 2137444, 1636800, 10880,
                833, 270802, 1252800, 203040, 26, 992, 70640400, 534600, 2169132, 673505280, 11566800, 41446080, 780,
                178200, 7, 26127360, 480924900, 575769600, 146577600, 2019600, 1008, 357283840, 159936000, 1693120,
                737095680, 90, 328230700, 53856000, 5347056, 132192, 772390080, 47434464, 115473600, 9319536, 19800,
                62100, 198000, 26231040, 71075520, 167400000, 78586200, 2575872, 716636160, 399360, 46, 29760, 56627904,
                57564000, 50379840, 153125000, 319800, 475136928, 313728, 24437760, 8526, 486205440, 4626720, 2340576,
                78975468, 3004400, 47, 3201600, 55944000, 8370, 642600, 6300, 100352, 19440, 225330, 19906560, 3520,
                16379904, 13104, 837000000, 174960000, 623001600, 2178560, 11664000, 17539200, 4230, 574801920, 21930,
                864000, 480664800, 4656960, 720, 96623280, 28576800, 8337210, 146126592, 10, 110522880, 933970752, 3,
                983537280, 218268, 179625600, 114576, 656250, 847086240, 4860, 330, 655361280, 129024480, 213440000,
                105, 10546200, 12210, 3720, 3149250, 33, 109680480, 1865920, 29568, 1456, 91264, 2700000, 192447360, 28,
                304378200, 116746344, 85225896, 722610, 13053600, 1664832, 808790400, 96909120, 64912800, 252, 69300,
                2813580, 392, 554098272, 62775648, 900900, 2387280, 11, 46690, 51930240, 2946240, 30427488, 1296000,
                4176, 327360, 20995200, 34992, 492602880, 5583600, 46679328, 582120, 343656000, 21548160, 273240,
                66846720, 1870848, 629185920, 578088000, 74840640, 493580, 2025000, 113286600, 65790, 1014594, 1334,
                886485600, 150585600, 1104, 55573544, 340200, 761400, 42328000, 121524, 268272000, 336, 4233600, 6,
                109058400, 8491392, 527788800, 702240, 708505600, 644744240, 77760, 1207680, 31, 135475200, 244944000,
                40924800, 123530400, 257094000, 9622800, 226842560, 25719120, 112, 5331312, 96, 507735360, 864230400,
                44, 987033600, 8714240, 85, 25272000, 70048800, 372552000, 20401920, 476280000, 338348400, 10060200,
                5616, 12600, 37, 7959168, 12027960, 788256, 1034880, 852405120, 200970, 100640, 6375, 20700, 45540,
                1612806, 18480, 5167800, 1918080, 1512, 50592, 9504000, 6109440, 47720904, 80388, 2294, 673200, 57528,
                11340000, 147052800, 230247360, 1940400, 2980416, 105840, 763680, 264600000, 523832400, 3264, 78732000,
                22680, 10031040, 38, 142147710, 7931040, 7603200, 777288960, 20304, 808635, 421303680, 238392000, 48,
                14, 196416000, 625, 7188480, 9535680, 3888, 2302020, 1458240, 117028800, 19404, 49920, 34467840,
                20098044, 501600, 1350000, 21, 224640, 7244160, 208800, 11416720, 533520, 70531776, 165267200, 13,
                209119680, 16339200, 5076, 960, 118329120, 43848, 3735200, 499685760, 6396, 437060, 447635160, 151200,
                4080, 120, 526156280, 2040, 31579200, 609120, 5959800, 35, 1025640, 228937500, 17168580, 102750480,
                297216, 6210, 769984800, 1599360, 32640, 11664, 690, 1797120, 25, 43623360, 15, 42412500, 683860320,
                40102920, 182700, 1048320, 202368, 5287680, 2622, 16996320, 147840, 8916480, 2141594, 825, 183283200,
                115128000, 1445220, 16524000, 7102158, 19183500, 1050, 738720, 23310, 108864000, 972537020, 371226240,
                17884800, 94474512, 641491200, 235544960, 28753920, 1854840, 199920000, 2464, 17582400, 757350, 13440,
                66640, 13200, 319872, 45, 466527600, 156247476, 44198784, 249458, 496800, 7105320, 30, 7618560, 2024640,
                198042624, 550560, 30787680, 371726250, 182564928, 152064000, 20403240, 55480320, 415441920, 1040520,
                367080, 2, 320993280, 18060, 16, 14968800, 22291200, 118800, 117600, 6182568, 371520, 9473760,
                191147040, 55836, 65120, 21311472, 757680, 991440, 13003200, 681807168, 94500, 590020200, 208915200,
                103783680, 395136000, 17, 300641280, 10080, 2048, 151208640, 721677600, 28171800, 142076480, 102236160,
                115953600, 282, 1740800, 198288000, 255494250, 74810540, 15960, 1727530, 27744, 349920, 489600,
                954600000, 120294720, 26656, 328440, 2673528, 44915780, 1392, 23284800, 7507200, 14850000, 67092480,
                950400, 425952, 23, 6293, 28690200, 146286000, 1522800, 590475600, 60234240, 812036160, 305777640, 1066,
                4071600, 37684224, 816, 47250, 130, 616, 60, 14283000, 671422500, 993600, 392544, 126904320, 52026,
                4546080, 53581500, 13739040, 85260, 61289760, 163397520, 2520, 138, 713, 102060, 129254400, 233280,
                956188800, 288921600, 43545600, 939060, 879298560, 2518960, 485222400, 9434880, 5128200, 2071008,
                10523520, 517267296, 216720, 4263840, 705640320, 524929944, 12792, 417530880, 169099, 22453200,
                103530240, 600880, 66816, 687063360, 1692, 163800576, 1247400, 169136, 471458880, 26649000, 100850400,
                1527360, 234426192, 11880, 1325184, 3861, 68080, 13226976, 135449600, 378510, 18328320, 9720, 11408,
                6528, 444426240, 23603400, 24041472, 250240, 840, 3136, 9098112, 33024, 608860800, 197070720, 160992,
                316838340, 86935680, 361584000, 537062400, 13340000, 1666, 714, 3207600, 414607200, 4388580, 703296000,
                4898880, 10281600, 66166400, 774225, 429028320, 8, 10800, 99435600, 142884000, 532980000, 35897400,
                418660704, 634016292, 36, 43, 60999680, 1560, 174155520, 7236900, 360, 9, 20457360, 25704, 332640,
                1572480, 60775680, 1084566, 21242, 877282560, 159667200, 18823680, 213840000, 237762000, 19, 12420,
                122496192, 14674, 49338720, 187200, 245877120, 28050, 499035600, 199920, 27165600, 130032, 11881800,
                1339200, 67860, 9977760, 540, 11152, 503884800, 498960, 4128, 5, 15218272, 12384, 14084280, 19699680,
                110735100, 301806000, 348532800, 2728, 5644800, 2064, 24960, 1520, 263736000, 99145200, 25515000,
                91672560, 663264000, 8586900, 96368160, 53280, 367007760, 72783360, 35424000, 1142400, 515040, 3150,
                16037280, 4, 18, 494, 761425920, 579889800, 4252500, 13746240, 958566400, 816083424, 8596560, 2375,
                171360, 128943360, 420, 269494680, 22, 18052776, 36691200, 21288960, 31360, 434928, 41, 64, 130713600,
                623162880, 9806850, 144, 403307520, 760872960, 57283200, 329041440, 373626000, 8040384, 410231680,
                3572100, 472024800, 5330, 2668000, 1716858, 33566400, 25704000, 1800, 1707520, 190920, 36288, 303030,
                1224510, 16200, 12791520, 3294720, 4950, 2397600, 916531200, 285418000, 1740, 3250800, 265920480,
                844074, 217600, 75984480, 170100, 9164160, 28800, 8326668, 99840, 68211072, 3951360, 10421208,
                443573676, 1267200, 1134, 520914240, 194016, 27, 678585600, 45460800, 289800, 923155200, 55350000,
                38880, 99993972, 13880160, 99, 113308800, 475200, 396809280, 30437820, 399600000, 71442000, 12474000,
                104570880, 71038240, 1944320, 142128, 899469480, 7996800, 261870, 310500, 17205, 4144608, 23560,
                14513920, 709789500, 455112000, 51149532, 3137280, 30240000, 15966240, 1080000, 268531200, 102228480,
                366300, 1638, 417384000, 489888000, 29, 352235520, 129600, 61630800, 12, 82368000, 41025600, 272, 370,
                272320, 181238400, 42, 6603300, 814531200, 33881760, 6763960, 124200, 16842240, 6201600, 91282464, 196,
                276307200, 295160840, 107678880, 256493280, 89302500, 71850240, 291600, 7402752, 6090, 10148160, 743040,
                142560, 256, 84150000, 15315300, 258075, 245000, 200448, 9896040, 176344128, 10495800, 999694080,
                428652000, 547181040, 317906120, 2612288, 32, 347276160, 601201440, 6416540, 334816020, 89804880,
                30902400, 39, 152189100, 927628800, 57507840, 97524000, 3995136, 401289420, 591763200, 266760, 21960960,
                29955200, 791683200, 776160, 527472000, 16074240, 16920, 595200, 67173120, 5280, 620, 68376000,
                479587500, 21735000, 525477888, 1269504, 21600000, 334863360, 39513600, 735540, 408064800, 310464,
                114048000, 847895040, 454896, 2160, 8145312, 24, 106720, 188770176, 99021312, 62937000, 41400, 80,
                29937600, 99163584, 412387200, 69076800, 358092, 749700000, 15385920, 41354, 449064000, 3654, 62,
                9979200, 5362560, 16512, 714067200, 86423040, 27410400, 555, 284342100, 21769440, 812700, 126491904,
                486, 97796160, 8412320, 155790720, 464032800, 389999232, 131369472, 9102240, 2679600, 4334400, 60480,
                9343152, 303061248, 5832000, 922521600, 594762, 1278900, 349440, 6240, 5552064, 6557760, 34986,
                945584640, 211221504, 6606720, 935813760, 40, 198660, 2960, 84123200, 156864, 203, 101594064, 6765120,
                43706, 309104640, 523169280, 25159680, 42477120, 41650000, 125, 598, 8352, 270, 763408800, 53706240,
                477459840, 2634240, 22232560, 370828800, 798336000, 36720, 30735360, 34], 888_820_343), ]
for test_int_arr, expected_output in test_cases:
    assert expected_output == num_factored_binary_trees(test_int_arr)
