quora_dict is the dictionary/vocabulary of the words found in the training set in train folder.

quora.pkl is the dataset.
loading once will give you a tuple (train_x, train_y)
loading again will give you a tuple (test_x, test_y)

where train_x is a list of text documents (answers on quora) (in the form of sequence of numeric indices (instead of original words) :- accourding to word count in quora_dict.pkl )
and train_y is a list of numeric indices corresponding to the respective authors, according to the csv 'author.csv' .