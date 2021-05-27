"""
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history
 number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:
- Assuming x is the length of history
- BrowserHistory(string homepage): Initializes the object with the homepage of the browser.
- void visit(string url): Visits url from the current page. It clears up all the forward history.
- string back(int steps): Move steps back in history. If you can only return x steps in the history and steps > x, you
    will return only x steps. Return the current url after moving back in history at most steps.
- string forward(int steps): Move steps forward in history. If you can only forward x steps in the history and steps > x
    , you will forward only x steps. Return the current url after forwarding in history at most steps.
"""
from typing import List, Optional, Union


class BrowserHistory:
    def __init__(self, homepage: str):
        """
        :param homepage: Initializes the object with the homepage of the browser
        """
        self.history = [homepage]
        self.history_pointer = 0

    def visit(self, url: str) -> None:
        """
        :param url: Visits url from the current page. It clears up all the forward history.
        """
        self.history = self.history[:self.history_pointer + 1] + [url]
        self.history_pointer += 1

    def back(self, steps: int) -> str:
        """
        :param steps: Move steps back in history.
        :return: the current url after moving back in history at most steps.
        """
        self.history_pointer = max(0, self.history_pointer - steps)
        return self.history[self.history_pointer]

    def forward(self, steps: int) -> str:
        """
        :param steps: Move steps forward in history
        :return: the current url after forwarding in history at most steps.
        """
        self.history_pointer = min(len(self.history) - 1, self.history_pointer + steps)
        return self.history[self.history_pointer]


def run_simulation(instructions: List[str], parameters: List[List[Union[int, str]]],
                   expected_output: List[Optional[str]]) -> None:
    test_object = BrowserHistory(parameters[0][0])
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i][0], expected_output[i]
        if next_instruction == "visit":
            test_object.visit(next_parameter)
        elif next_instruction == "back":
            assert test_object.back(next_parameter) == expected_value
        else:
            assert test_object.forward(next_parameter) == expected_value


test_cases = [
    (["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward", "visit", "forward", "back", "back"],
     [["leetcode.com"], ["google.com"], ["facebook.com"], ["youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2],
      [7]],
     [None, None, None, None, "facebook.com", "google.com", "facebook.com", None, "linkedin.com",
      "google.com", "leetcode.com"]
     ),
    (["BrowserHistory", "visit", "forward", "visit", "visit", "visit", "back", "visit", "forward", "visit", "visit",
      "visit", "visit", "visit", "visit", "visit", "forward", "visit", "back", "visit", "forward", "visit", "visit",
      "visit", "forward", "visit", "visit", "visit", "visit", "visit", "back", "visit", "visit", "visit", "visit",
      "forward", "visit", "visit", "visit", "visit", "forward", "visit", "visit", "visit", "visit", "forward", "visit",
      "visit", "visit", "back", "visit", "forward", "visit", "visit", "back", "visit", "visit", "visit", "forward",
      "forward", "back", "back", "visit", "visit", "visit", "visit", "visit", "visit", "visit", "back", "visit"],
     [["mipvzdy.com"], ["wioafrx.com"], [4], ["bz.com"], ["bjjeyv.com"], ["bj.com"], [6], ["lzu.com"], [2],
      ["knov.com"], ["gyy.com"], ["hnl.com"], ["yyfp.com"], ["rpc.com"], ["ccqxuwp.com"], ["xyqi.com"], [6], ["ds.com"],
      [10], ["pzrtgx.com"], [6], ["xpmkdqq.com"], ["dkcvwkz.com"], ["pzyzj.com"], [7], ["jd.com"], ["lmpwat.com"],
      ["mry.com"], ["iu.com"], ["kcajce.com"], [1], ["xnzy.com"], ["llf.com"], ["irmrp.com"], ["rqrtok.com"], [4],
      ["jgsz.com"], ["ixnbjhy.com"], ["fwcv.com"], ["zqdtht.com"], [9], ["begu.com"], ["pouwyrz.com"], ["seubwdz.com"],
      ["sgsglc.com"], [3], ["ipfcvrp.com"], ["fqhgatg.com"], ["wyyami.com"], [9], ["qujavtk.com"], [6], ["wr.com"],
      ["bdh.com"], [5], ["vvr.com"], ["pblspj.com"], ["supgur.com"], [5], [7], [9], [7], ["wom.com"], ["hbytgj.com"],
      ["xc.com"], ["mbou.com"], ["ng.com"], ["griq.com"], ["zns.com"], [1], ["zugu.com"]],
     [None, None, "wioafrx.com", None, None, None, "mipvzdy.com", None, "lzu.com", None, None, None, None, None, None,
      None, "xyqi.com", None, "mipvzdy.com", None, "pzrtgx.com", None, None, None, "pzyzj.com", None, None, None, None,
      None, "iu.com", None, None, None, None, "rqrtok.com", None, None, None, None, "zqdtht.com", None, None, None,
      None, "sgsglc.com", None, None, None, "ixnbjhy.com", None, "qujavtk.com", None, None, "rqrtok.com", None, None,
      None, "supgur.com", "supgur.com", "lmpwat.com", "mipvzdy.com", None, None, None, None, None, None, None,
      "griq.com", None]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
