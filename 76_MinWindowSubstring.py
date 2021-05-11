"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no
 such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
"""
from collections import defaultdict


def min_window_all_characters(s: str, t: str) -> str:
    """
    :param s: query string to search the window in
    :param t: window should have all characters in t. may contain duplicates
    :return: the one unique minimum window in s that contains all characters of t, or empty string "" if no such window
        exists
    """
    if not s or not t:
        return ""

    # sliding window needs to contain following characters
    dict_t = defaultdict(int)
    for t_i in t:
        dict_t[t_i] += 1
    # t contains following unique characters
    unique_chr_t = len(dict_t)

    # scanning window is s[window_start: window_end + 1]
    window_start = 0
    # these characters are present in the window, with more than enough repetitions
    chr_in_window_satisfied = 0

    window_character = defaultdict(int)

    min_window_size, min_window_left, min_window_right = len(s) + 1, 0, 0

    for window_end in range(len(s)):
        # expand window to the right
        right_character = s[window_end]
        if right_character in dict_t:
            window_character[right_character] += 1
            if right_character in dict_t and window_character[right_character] == dict_t[right_character]:
                chr_in_window_satisfied += 1

            # try to shrink the window from the left
            while window_start <= window_end and chr_in_window_satisfied == unique_chr_t:
                if s[window_start] in dict_t:
                    if window_end - window_start + 1 < min_window_size:
                        min_window_size = window_end - window_start + 1
                        min_window_left, min_window_right = window_start, window_end

                    left_character = s[window_start]
                    window_character[left_character] -= 1
                    if left_character in dict_t and window_character[left_character] < dict_t[left_character]:
                        chr_in_window_satisfied -= 1

                window_start += 1

    return "" if min_window_size > len(s) else s[min_window_left: min_window_right + 1]


def min_window_select_characters(s: str, t: str) -> str:
    """
    :param s: query string to search the window in
    :param t: window should have all characters in t. may contain duplicates
    :return: the one unique minimum window in s that contains all characters of t, or empty string "" if no such window
        exists
    """
    if not s or not t:
        return ""

    # sliding window needs to contain following characters
    dict_t = defaultdict(int)
    for t_i in t:
        dict_t[t_i] += 1
    # t contains following unique characters
    unique_chr_t = len(dict_t)

    filtered_s = [(i, c_s) for i, c_s in enumerate(s) if c_s in dict_t]

    left_pointer = right_pointer = 0
    chr_in_window_satisfied = 0
    window_character = defaultdict(int)

    min_window_size, min_window_left, min_window_right = len(s) + 1, 0, 0

    while right_pointer < len(filtered_s):
        # expand window to the right
        window_end, right_character = filtered_s[right_pointer]
        window_character[right_character] += 1

        if window_character[right_character] == dict_t[right_character]:
            chr_in_window_satisfied += 1

        # try to shrink the window from the left
        while left_pointer <= right_pointer and chr_in_window_satisfied == unique_chr_t:
            window_start, left_character = filtered_s[left_pointer]
            if window_end - window_start + 1 < min_window_size:
                min_window_size = window_end - window_start + 1
                min_window_left, min_window_right = window_start, window_end

            window_character[left_character] -= 1
            if window_character[left_character] < dict_t[left_character]:
                chr_in_window_satisfied -= 1

            left_pointer += 1

        right_pointer += 1

    return "" if min_window_size > len(s) else s[min_window_left: min_window_right + 1]


def min_window_dict_diff(s: str, t: str) -> str:
    """
    :param s: query string to search the window in
    :param t: window should have all characters in t. may contain duplicates
    :return: the one unique minimum window in s that contains all characters of t, or empty string "" if no such window
        exists
    """
    if not s or not t:
        return ""

    t_over_s = defaultdict(int)
    for t_i in t:
        t_over_s[t_i] += 1
    outstanding_chr_count = len(t)

    window_start = 0
    min_str = ""
    min_window_size = len(s) + 1

    for window_end in range(len(s)):
        if t_over_s[s[window_end]] > 0:
            # if some characters are present in t but are missing in current window
            # t_over_s[s[window_end]] will be positive
            # otherwise, it is either not in t or already been satisfied
            outstanding_chr_count -= 1
        t_over_s[s[window_end]] -= 1

        # try to shrink the window from the left
        while outstanding_chr_count == 0 and window_start <= window_end:
            if min_window_size > window_end - window_start + 1:
                min_str = s[window_start:window_end + 1]
                min_window_size = window_end - window_start + 1

            t_over_s[s[window_start]] += 1
            if t_over_s[s[window_start]] > 0:
                outstanding_chr_count += 1

            window_start += 1

    return min_str


test_cases = [("ADOBECODEBANC", "ABC", "BANC"),
              ("a", "a", "a"),
              ("a", "aa", ""),
              ("cacaaabacbcccccbabcaa", "bbabcbc", "bacbcccccbab"),
              ("caacbabbbcacbabaabcbbbcbbcbbbbbbabbcacbbcbabccbabbc", "bababbcabccccbabbacacb",
               "caacbabbbcacbabaabcbbbcbbc"),
              (
                  "obzcopzocynyrsgsarijyxnkpnukkrvzuwdjldxndmnvevpgmxrmvfwkutwekrffnloyqnntbdohyfqndhzyoykiripdzwiojyoznb" +
                  "togjyfpouuxvumtewmmnqnkadvzrvouqfbbdiqremqzgevkbhyoznacqwbhtrcjwfkzpdstpjswnpiqxjhywjanhdwavajrhwtwzlr" +
                  "qwmombxcaijzevbtcfsdcuovckoalcseaesmhrrizcjgxkbartdtotpsefsrjmvksqyahpijsrppdqpvmuocofuunonybjivbjviyf" +
                  "tsyiicbzxnwnrmvlgkzticetyfcvqcbjvbufdxgcmesdqnowzpshuwcseenwjqhgsdlxatamysrohfnixfprdsljyyfhrnnjsagtui" +
                  "huczilgvtfcjwgdhpbixlzmakebszxbhrdibpoxiwztshwczamwnninzmqrmpsviydkptjzpktksrortapgpxwojofxeasoyvyprjo" +
                  "guhqobehugwdvtzlenrcttuitsiijswpogicjolfxhiscjggzzissfcnxnvgftxvbfzkukqrtalvktdjsodmtgzqtuyaqvvrbuexgw" +
                  "qzwduixzrpnvegddyyywaquxjxrnuzlmyipuqotkghfkpknqinoidifnfyczzonxydtqroazxhjnrxfbmtlqcsfhshjrxwqvblovao" +
                  "uxwempdrrplefnxmwrwfjtebrfnfanvvmtbzjesctdgbsfnpxlwihalyiafincfcwgdfkvhebphtxukwgjgplrntsuchyjjuqozaki" +
                  "glangxkttsczhnswjksnuqwflmumpexxrznzwxurrysaokwxxqkrggytvsgkyfjrewrcvntomnoazmzycjrjrqemimyhriyxgrzcfu" +
                  "qtjhvjtuhwfzhwpljzajitrhryaqchnuawbxhxrpvyqcvhpggrpplhychyulijhkglinibedauhvdydkqszdbzfkzbvhldstocgydn" +
                  "bfjkcnkfxcyyfbzmmyojgzmasccaahpdnzproaxnexnkamwmkmwslksfpwirexxtymkmojztgmfhydvlqtddewjvsrmyqjrpycbmnd" +
                  "hupmdqqabiuelacuvxnhxgtpvrtwfgzpcrbhhtikbcqpctlxszgpfbgcsbaaiapmtsucocmpecgixshrrnhyrpalralbccnxvjzjll" +
                  "arqhznzghswqsnfuyywmzbopyjyauknxddgdthlabjqtwxpxwljvoxkpjjpfvccyikbbrpdsyvlxscuoofkecwtnfkvcnzbxkeabtd" +
                  "usyhrqklhaqreupakxkfzxgawqfwsaboszvlshwzhosojjotgyagygguzntrouhiweuomqptfjjqsxlbylhwtpssdlltgubczxslqj" +
                  "gxuqnmpynnlwjgmebrpokxjnbiltvbebyytnnjlcwyzignmhedwqbfdepqakrelrdfesqrumptwwgifmmbepiktxavhuavlfaqxqhr" +
                  "eznbvvlakzeoomykkzftthoemqwliednfsqcnbexbimrvkdhllcesrlhhjsspvfupxwdybablotibypmjutclgjurbmhztboqatrdw" +
                  "somnxnmocvixxvfiqwmednahdqhxjkvcyhpxxdmzzuyyqdjibvmfkmonfxmohhshpkhmntnoplphqyprveyfsmsxjfosmicdsjriee" +
                  "ytpnbhlsziwxnpmgoxneqbnufhfwrjbqcsdfarybzwaplmxckkgclvwqdbpumsmqkswmjwnkuqbicykoisqwoootrdpdvcuiuswfqm" +
                  "rkctsgrevcxnyncmivsxbpbxzxpwchiwtkroqisnmrbmefbmatmdknaklpgpyqlsccgunaibsloyqpnsibwuowebomrmcegejozypj" +
                  "zjunjmeygozcjqbnrpakdermjcckartbcppmbtkhkmmtcngteigjnxxyzaibtdcwutkvpwezisskfaeljmxyjwykwglqlnofhycwui" +
                  "vdbnpintuyhtyqpwaoelgpbuwiuyeqhbvkqlsfgmeoheexbhnhutxvnvfjwlzfmvpcghiowocdsjcvqrdmkcizxnivbianfpsnzabx" +
                  "qecinhgfyjrjlbikrrgsbgfgyxtzzwwpayapfgueroncpxogouyrdgzdfucfrywtywjeefkvtzxlwmrniselyeodysirqflpduvibf" +
                  "dvedgcrzpzrunpadvawfsmmddqzaaahfxlifobffbyzqqbtlcpquedzjvykvarayfldvmkapjcfzfbmhscdwhciecsbdledspgpdts" +
                  "teuafzbrjuvmsfrajtulwirzagiqjdiehefmfifocadxfuxrpsemavncdxuoaetjkavqicgndjkkfhbvbhjdcygfwcwyhpirrfjziq" +
                  "onbyxhibelinpllxsjzoiifscwzlyjdmwhnuovvugfhvquuleuzmehggdfubpzolgbhwyeqekzccuypaspozwuhbzbdqdtejuniuuy" +
                  "agackubauvriwneeqfhtwkocuipcelcfrcjcymcuktegiikyosumeioatfcxrheklookaqekljtvtdwhxsteajevpjviqzudnjnqbu" +
                  "cnfvkybggaybebljwcstmktgnipdyrxbgewqczzkaxmeazpzbjsntltjwlmuclxirwytvxgvxscztryubtjweehapvxrguzzsatozz" +
                  "jytnamfyiitreyxmanhzeqwgpoikcjlokebksgkaqetverjegqgkicsyqcktmwjwakivtsxjwrgakphqincqrxqhzbcnxljzwturms" +
                  "aklhnvyungjrxaonjqomdnxpnvihmwzphkyuhwqwdboabepmwgyatyrgtboiypxfavbjtrgwswyvcqhzwibpisydtmltbkydhznbsv" +
                  "xktyfxopwkxzbftzknnwipghuoijrbgqnzovxckvojvsqqraffwowfvqvfcmiicwitrhxdeombgesxexedlakitfovtydxunqnwqqd" +
                  "eeekiwjnwoshqcsljiicgobbbuqakjdonjawgjlezdnqhfdqnmsuavxdpnfzwipmspiabveaarshzwxmirgkmfncvtdrdvfxkpxlkd" +
                  "okxgtwcskmjryyymcthfnkasinihaunohkxaibtsqelockaefjmsuolebtnepauwmrxutspjwaxbmahsjtkfkxlnszribmeofbkyvb" +
                  "jscjtqjakuwvcgunvnonvqbbggfshauqsyznokqbhowjusypfnecffenojfvlblgzntqzlrgzprvhqnpfrrkzxznieiuivajivzijs" +
                  "qijigtatifmbplzqahuidegfoobpymkputzamzvweiyvvzlwihgmmmrcburbgbsdxrfjsbiylitghgcpqjbevvgypxcybubyoijijr" +
                  "huzcdijfybqbfowlookqmlnplbxvjjosfqviygqyhgamuwzjklbyzopkrnhbywtfoqomweldmlrhjqswctubiknzzvcztyehouvnyi" +
                  "qnvkufaobehxhrjvtisxjlxoumipzjarwvbsaegdkpbsjmpevjbewzuqnfhoohhmdjgfpmjzdmtmykqvtucptwfidpwtwffzolffzq" +
                  "fdearclkyeecuzabjeqhxpmfodsvisnpxrqowdawheydfyhoexvcmihdlzavtqlshdhdgjzpozvvackebhgqppvcrvymljfvooauxc" +
                  "jnbejdivikcoaugxwzsulgfqdtefpehbrlhaoqxwcancuvbqutnfbuygoemditeagmcveatgaikwflozgdhkyfqmjcruyyuemwbqwx" +
                  "yyfiwnvlmbovlmccaoguieu",
                  "cjgamyzjwxrgwedhsexosmswogckohesskteksqgrjonnrwhywxqkqmywqjlxnfrayykqotkzhxmbwvzstrcjfchvluvbaobymlrcg" +
                  "bbqaprwlsqglsrqvynitklvzmvlamqipryqjpmwhdcsxtkutyfoiqljfhxftnnjgmbpdplnuphuksoestuckgopnlwiyltezuwdmhs" +
                  "gzzajtrpnkkswsglhrjprxlvwftbtdtacvclotdcepuahcootzfkwqhtydwrgqrilwvbpadvpzwybmowluikmsfkvbebrxletigjjl" +
                  "ealczoqnnejvowptikumnokysfjyoskvsxztnqhcwsamopfzablnrxokdxktrwqjvqfjimneenqvdxufahsshiemfofwlyiionrybf" +
                  "chuucxtyctixlpfrbngiltgtbwivujcyrwutwnuajcxwtfowuuefpnzqljnitpgkobfkqzkzdkwwpksjgzqvoplbzzjuqqgetlojnb" +
                  "lslhpatjlzkbuathcuilqzdwfyhwkwxvpicgkxrxweaqevziriwhjzdqanmkljfatjifgaccefukavvsfrbqshhswtchfjkausgauk" +
                  "eapanswimbznstubmswqadckewemzbwdbogogcysfxhzreafwxxwczigwpuvqtathgkpkijqiqrzwugtr",
                  "twxpxwljvoxkpjjpfvccyikbbrpdsyvlxscuoofkecwtnfkvcnzbxkeabtdusyhrqklhaqreupakxkfzxgawqfwsaboszvlshwzhos" +
                  "ojjotgyagygguzntrouhiweuomqptfjjqsxlbylhwtpssdlltgubczxslqjgxuqnmpynnlwjgmebrpokxjnbiltvbebyytnnjlcwyz" +
                  "ignmhedwqbfdepqakrelrdfesqrumptwwgifmmbepiktxavhuavlfaqxqhreznbvvlakzeoomykkzftthoemqwliednfsqcnbexbim" +
                  "rvkdhllcesrlhhjsspvfupxwdybablotibypmjutclgjurbmhztboqatrdwsomnxnmocvixxvfiqwmednahdqhxjkvcyhpxxdmzzuy" +
                  "yqdjibvmfkmonfxmohhshpkhmntnoplphqyprveyfsmsxjfosmicdsjrieeytpnbhlsziwxnpmgoxneqbnufhfwrjbqcsdfarybzwa" +
                  "plmxckkgclvwqdbpumsmqkswmjwnkuqbicykoisqwoootrdpdvcuiuswfqmrkctsgrevcxnyncmivsxbpbxzxpwchiwtkroqisnmrb" +
                  "mefbmatmdknaklpgpyqlsccgunaibsloyqpnsibwuowebomrmcegejozypjzjunjmeygozcjqbnrpakdermjcckartbcppmbtkhkmm" +
                  "tcngteigjnxxyzaibtdcwutkvpwezisskfaeljmxyjwykwglqlnofhycwuivdbnpintuyhtyqpwaoelgpbuwiuyeqhbvkqlsfgmeoh" +
                  "eexbhnhutxvnvfjwlzfmvpcghiowocdsjcvqrdmkcizxnivbianfpsnzabxqecinhgfyjrjlbikrrgsbgfgyxtzzwwpayapfgueron" +
                  "cpxogouyrdgzdfucfrywtywjeefkvtzxlw"), ]
for min_window in [min_window_dict_diff, min_window_select_characters, min_window_all_characters]:
    for test_s, test_t, expected_window in test_cases:
        assert min_window(test_s, test_t) == expected_window, min_window.__name__
