# -----------------------
# Author: Tuan Nguyen
# Date created: 20190911
#!solutions/87.py
# ----------------------
"""
A rule looks like this:

A NE B
This means this means point A is located northeast of point B.

A SW C
means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:
A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.
"""

delta = {
    "N": [0, 1],
    "NE": [1, 1],
    "E": [1, 0],
    "SE": [1, -1],
    "S": [0, -1],
    "SW": [-1, -1],
    "W": [-1, 0],
    "NW": [-1, 1],
}


def isValid(rules):
    # input:
    # output:
    points = {}  # point_name: [x_coord, y_coord]
    for rule in rules:  # go through all rules
        ruleAnalyzer = rule.split()  # analyze rule from string to list
        d, loc, s = (
            ruleAnalyzer[0],
            ruleAnalyzer[1],
            ruleAnalyzer[2],
        )  # destination "d", location "loc", source "s" from current rule
        if s not in points.keys():  # new source
            points[s] = [0, 0]
        x_s, y_s = points[s][0], points[s][1]  # get coords of source
        delta_x, delta_y = (
            delta[loc][0],
            delta[loc][1],
        )  # locate the distance of destination from source by direction
        # calculate destination coords from rule
        x_d = x_s + delta_x
        y_d = y_s + delta_y
        # check valid
        if d not in points.keys():  # new destination
            points[d] = [x_d, y_d]
            continue
        else:  # this destination appeared before
            real_x_d, real_y_d = (
                points[d][0],
                points[d][1],
            )  # get destination coords calculated from previous rules
            if (real_x_d != x_d) and (
                real_y_d != y_d
            ):  # coords from previous rule are different from calculation of current rule
                return False  # conflict of previous rule and current rule
    return True  # no conflict rules if reach this


def isValid_test(rules):
    print(rules, "~>", isValid(rules))


if __name__ == "__main__":
    isValid_test(rules=["A N B", "B NE C", "C N A"])  # print False
    isValid_test(rules=["A NW B", "A N B"])  # print True
