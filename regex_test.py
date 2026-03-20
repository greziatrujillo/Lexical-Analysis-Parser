from regex import parse, accept

count = 0


# mater tests
# test 1
ans = accept(parse("mater"))
if "part" in ans:    
    print("accepted")
    count += 1

# test 2
ans = accept(parse("maternal"))
if "part" in ans:    
    print("accepted")
    count += 1

# test 3
ans = accept(parse("immaterial"))
if "part" in ans:    
    print("accepted")
    count += 1

# test 4
ans = accept(parse("maternity"))
if "part" in ans:    
    print("accepted")
    count += 1

# test 5
ans = accept(parse("material"))
if "part" in ans:    
    print("accepted")
    count += 1

# test 6
ans = accept(parse("animater"))
if "part" in ans:    
    print("accepted")
    count += 1


# domin tests
# test 7
ans = accept(parse("domin"))
if "part" in ans:    
    print("accepted")
    count += 1

# test 8
ans = accept(parse("dominate"))
if "part" in ans:    
    print("accepted")
    count += 1

# test 9
ans = accept(parse("abdominal"))
if "part" in ans:    
    print("accepted")
    count += 1

# test 10
ans = accept(parse("predominate"))
if "part" in ans:    
    print("accepted")
    count += 1

# test 11
ans = accept(parse("domino"))
if "part" in ans:    
    print("accepted")
    count += 1

# test 12
ans = accept(parse("doming"))
if "part" in ans:    
    print("accepted")
    count += 1


# miscelaneous tests
# test 13
ans = accept(parse("lively"))
if "not" in ans:    
    print("rejected")
    count += 1

# test 14
ans = accept(parse("zoom"))
if "not" in ans:    
    print("rejected")
    count += 1

# test 15
ans = accept(parse("word"))
if "not" in ans:    
    print("rejected")
    count += 1

# test 16
ans = accept(parse("matrix"))
if "not" in ans:    
    print("rejected")
    count += 1

# test 17
ans = accept(parse("mathematics"))
if "not" in ans:    
    print("rejected")
    count += 1


print("passed tests:", count, "of 17")