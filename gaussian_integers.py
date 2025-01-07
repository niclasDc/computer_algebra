def UnitaryNormalPart(a, b):
    """
        This function calculates the unitary normal part of a given complex number.
    """
    if a == 0:
        if b == 0:
            return "0", "1"
        elif b > 0:
            return f"{b}i" , "1"
        elif b < 0:
            return f"{-b}", "-i"
    
    if b == 0:
        if a > 0:
            return f"{a}", "1"
        elif a < 0:
            return f"{-a}", "-1"    
      
    if a > 0 and b > 0:
        return f"{a} + {b}i", "1"
    elif a < 0 and b > 0:
        return f"{b} + {-a}i", "i"
    elif a < 0 and b < 0:
        return f"{-a} + {-b}i", "-1"
    else:
        return f"{-b} + {a}i", "-i"


# Test the function

a = 2
b = -5

normal_part, unitary_part = UnitaryNormalPart(a, b)

print(f"({normal_part}, {unitary_part})")
print(f"{a} {f"+ {b}" if b> 0 else f"- {-b}i"} = ({normal_part})({unitary_part})")