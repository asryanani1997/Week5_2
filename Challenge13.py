x="the sky is blue"
words=x.split()
reversed_words=[i[::-1] for i in words]
final=" ".join(reversed_words)
print(final)