words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counter = Counter(words)
top_three = word_counter.most_common(3)
print(top_three)


from operator import itemgetter
rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows,key=itemgetter('fname'))
rows_by_fname = sorted(rows,rows['fname'])

rows_by_lfname = sorted(rows,key=itemgetter('lname','fname'))


class User:
       def __init__(self,user_id):
              self.user_id = user_id

       def __repr__(self):
              return 'User({})'.format(self.user_id)

from operator import attrgetter
sorted(users,key=attrgetter('user_id'))              
