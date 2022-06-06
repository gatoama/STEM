def calc_variable(main_volt, load_volt, current, resistor):
    """ main_volt and resistor can be adjusted (but only one at a time).
    Indicate which one is to be calulated by passing in None.
    """
    
    if main_volt == None:
        main_volt = calc_main_volt_(load_volt, current, resistor)
        return main_volt
    else:
        resistor = calc_resistor_(main_volt, load_volt, current)
        return resistor

def calc_main_volt_(load_volt, current, resistor):
    return (current * resistor) + load_volt

def calc_resistor_(main_volt, load_volt, current):
    return (main_volt - load_volt) / current 
