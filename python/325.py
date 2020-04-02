# --------------------------
# Author: Tuan Nguyen
# Date created: 20200402
#!325.py
# --------------------------
"""
The United States uses the imperial system of weights and measures, which means that there are many different, seemingly arbitrary units to measure distance. 
There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.

Create a data structure that can efficiently convert a certain quantity of one unit to the correct amount of any other unit. 
You should also allow for additional units to be added to the system.
"""
class ImperialMetrics:
    """ A data structure that can efficiently convert one unit to another unit in imperical metrics system """
    def __init__(self):
        """ create a basic look up table """
        self._look_up = {'in': 1, 'ft': 12}  # inch is the base unit, e.g 1 ft = 12 in
    
    def convert(self, amount, from_unit, to_unit):
        """ return the correct quantity after converting a certain quantity from a unit to a new unit """
        if from_unit not in self._look_up.keys():
            raise ValueError("Original unit does not exist")
        if to_unit not in self._look_up.keys():
            raise ValueError("Target unit does not exist")
        return amount * self._look_up[from_unit] / self._look_up[to_unit]

    def add(self, new_unit, amount, ref_unit):
        if ref_unit not in self._look_up.keys():
            raise ValueError("Reference unit does not exist")
        self._look_up[new_unit] = amount * self._look_up[ref_unit]

def main():
    imperial_system = ImperialMetrics()
    assert imperial_system.convert(5, 'ft', 'in') == 60
    imperial_system.add('yd', 3, 'ft')
    assert imperial_system.convert(10, 'yd', 'in') == 360
    imperial_system.add('chain', 22, 'yd')
    assert imperial_system.convert(1, 'chain', 'in') == 792
    imperial_system.add('mi', 1760, 'yd')
    assert imperial_system.convert(1, 'mi', 'ft') == 5280

if __name__ == "__main__":
    main()