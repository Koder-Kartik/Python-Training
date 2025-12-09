words = {"steal", "least", "stale", "tales"}
common = set(words[0])

for w in words[1:]:
    common &= set(w)


#common_chars = set.intersection(*(set(word) for word in words))






print(common)