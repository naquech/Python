punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    for char in punctuation_chars:
        word = word.replace(char, '')
    return word


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_pos(string):
    countp = 0
    for word in string.split():
        s_strip = strip_punctuation(word)
        s_lower = s_strip.lower()
        if s_lower in positive_words:
            countp += 1
    return countp


def get_neg(string):
    countn = 0
    for word in string.split():
        s_strip = strip_punctuation(word)
        s_lower = s_strip.lower()
        if s_lower in negative_words:
            countn += 1
    return countn

"""
# Open tweets file
fileconnection = open("project_twitter_data.csv", 'r')
lines = fileconnection.readlines()[1:]
header = lines[0]
tweet_list = []
for line in lines[1:]:
    tweet = line.split(',')
    tweet_list.append(tweet[0])
    pos_score = get_pos(tweet[0])
    neg_score = get_neg(tweet[0])
    #tweet_list.append(tweet[0])
"""

# Create csv file and write the headers
outfile = open('resulting_data.csv', 'w')
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

# Open tweets file
fileconnection = open("project_twitter_data.csv", 'r')
lines = fileconnection.readlines()

for line in lines[1:]:
    tweet = line.split(',')
    pos_score = get_pos(tweet[0])
    neg_score = get_neg(tweet[0])
    net_score = pos_score - neg_score
    replies = tweet[2].replace('\n','')
    print('{},{},{},{},{}'.format(tweet[1], replies, pos_score, neg_score, net_score))
    row_string = ('{},{},{},{},{}'.format(tweet[1], replies, pos_score, neg_score, net_score))
    outfile.write(row_string)
    outfile.write('\n')

"""
# Output each row
for tweet in tweet_list:
    pos_score = get_pos(tweet[0])
    neg_score = get_neg(tweet[0])
    net_score = pos_score + neg_score
    row_string = '{},{},{},{},{}'.format(tweet[1], tweet[2], pos_score, neg_score, net_score)
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
"""
