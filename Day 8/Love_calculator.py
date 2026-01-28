
def calculate_love_score(name1 , name2):
    whole_name = (name1 + name2).lowercase()
    t = whole_name.count("t")
    r = whole_name.count("r")
    u = whole_name.count("u")
    e = whole_name.count("e")

    true_ = t + r + u + e

    l = whole_name.count("l")
    o = whole_name.count("o")
    v = whole_name.count("v")
    e1 = whole_name.count("e")

    love_ = l + o + v + e1

    score = str(true_) + str(love_)
    print(score)


calculate_love_score(kim,ajd)