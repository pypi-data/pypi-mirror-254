def print_prog():
    print(
        """
import nltk
from nltk.util import ngrams
from collections import defaultdict

nltk.download("nps_chat")
posts = nltk.corpus.nps_chat.posts()
words = [word for post in posts for word in post]
print(words)


def predict_next_word(tokens, n, partial_sequence):
    n_gram_freq = defaultdict(int)
    for gram in ngrams(tokens, n + 1):
        n_gram_freq[" ".join(gram)] += 1

    last_n_words = " ".join(partial_sequence.split()[-n:])
    candidates = {k: v for k, v in n_gram_freq.items() if k.startswith(last_n_words)}

    return (
        max(candidates, key=candidates.get).split()[-1]
        if candidates
        else "No prediction"
    )


n = 5
partial_sequence = str(input("Enter sequence"))
predicted_word = predict_next_word(words, n, partial_sequence)
print(f"The next word after '{partial_sequence}' could be: '{predicted_word}'")

"""
    )
