import nltk
import collections
import random

if __name__ == "__main__":
    with open(input(), encoding='utf-8') as f:
        all_bigrams = list(nltk.bigrams(f.read().split()))

    mk_chain: dict = collections.defaultdict(collections.Counter)
    for h, t in all_bigrams:
        mk_chain[h][t] += 1

    curword: str = random.choice(list(mk_chain.keys()))

    for _ in range(10):
        wordlist: list = []
        for _ in range(10):
            wordlist.append(curword)
            tails: dict = mk_chain[curword]
            new_word: str = random.choices(list(tails.keys()), weights=list(tails.values()))[0]
            curword = new_word
        print(" ".join(wordlist))
