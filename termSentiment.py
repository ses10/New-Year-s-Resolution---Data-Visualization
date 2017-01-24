"""
Builds a dictionary of term sentiments from the AFINN-111 list.
"""

def buildSentimentDict(sent_file):
    file = open(sent_file)
    scores = {}
    for line in file:
        term, score = line.split("\t")
        scores[term] = int(score)

    file.seek(0)
    return scores
