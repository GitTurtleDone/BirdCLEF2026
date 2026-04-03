import pandas

print ("-"*30)
train_df = pandas.read_csv('data/train.csv')
taxonomy_df = pandas.read_csv('data/taxonomy.csv')
train_ss_lbl_df = pandas.read_csv('data/train_soundscapes_labels.csv')


print(f"Total number of rows in train.csv: {len(train_df)}")
print(f"Total number of rows in train_soundscapes_labels.csv: {len(train_ss_lbl_df)}")
print(f"Total number of rows in taxonomy.csv: {len(taxonomy_df)}")
