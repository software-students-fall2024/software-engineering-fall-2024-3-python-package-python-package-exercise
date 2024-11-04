# create arrays of different units and the unit categories they belong to

# first need to create a dictionary mapping units to unit types (length, weight, temperature, etcetera)
UNITS_CATEGORY_DICT = {unit: 'weight' for unit in WEIGHT_UNITS}
UNITS_CATEGORY_DICT = {unit: 'length' for unit in LENGTH_UNITS}
UNITS_CATEGORY_DICT = {unit: 'temp' for unit in TEMP_UNITS}

# helper function that will return the unit's category from premade dictionary
def getUnitCategory(unit):
    return UNITS_CATEGORY_DICT.get(unit)

def getUnits(args):
    from_unit = args.from_unit
    to_unit = args.to_unit

    if from_unit is None or to_unit is None:
        return "Error: unit either does not exist or is not registered in system.\n"

    if from_unit == to_unit:
        #converted_from_unit = convert(args.value)



