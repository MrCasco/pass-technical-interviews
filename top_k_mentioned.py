from collections import defaultdict
def topKFrequent(words, k):
    mentioned = defaultdict(lambda: 0)
    for word in words:
        mentioned[word] += 1

    res = []
    temp = list(dict(sorted(mentioned.items(), key=lambda item: item[1], reverse=True)).keys())
    import ipdb; ipdb.set_trace()
    for i, word in enumerate(temp):
        if len(res) < k:
            if i < len(mentioned)-1 and mentioned[temp[i+1]] == mentioned[temp[i]]:
                word = sorted([temp[i+1], temp[i]])[0]
            res.append(word)
    return res

print(topKFrequent(['aaa', 'aa', 'a'], 1))
print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))
