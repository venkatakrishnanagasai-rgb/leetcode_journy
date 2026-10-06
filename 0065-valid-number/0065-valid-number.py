class Solution(object):

    def isNumber(self, s):

        return bool(re.match(
            r"^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$",
            s
        ))