import numpy as np
import pandas as pd
import string
import pickle
from collections import defaultdict


class NaiveBayesClassifier:
    def __init__(self, df):
        self.df = self.set_dataframe(df)
        self.vocab = set()

    def preprocess_text(self, text):
        text = text.lower()
        text = "".join([char for char in text if char not in string.punctuation])
        return text

    def _update_email(self, df, preprocess_text):
        df['email'] = df['email'].apply(preprocess_text)

    def tokenize(self,text):
        return text.split()

    def _update_tokens(self, df, tokenize):
        df['tokens'] = df['email'].apply(tokenize)

    def _set_vobab(self, df,vocab):
        for tokens in df['tokens']:
            vocab.update(tokens)
        return vocab

    def counts(self):
        word_counts = defaultdict(lambda: {'ham':0,'spam':0})
        class_counts = {'ham':0,'spam':0}

        return word_counts, class_counts

    def set_dataframe(self, df):
        self._update_email(df, self.preprocess_text)
        self._update_tokens(df, self.tokenize)
        return df

    #assuming the dataset columns are label and tokens
    def _update_counts(self, df, word_counts, class_counts):
        for i, row in df.iterrows():
            class_label = row['label']
            class_counts[class_label] += 1
            for token in row['tokens']:
                word_counts[token][class_label] += 1

    def calculate(self, df, class_counts):
        total_samples = len(df)
        prior_ham = class_counts['ham'] / total_samples
        prior_spam = class_counts['spam'] / total_samples

        return prior_ham, prior_spam

    def _update_likelihood(self, word_counts, class_counts, vocab):
        likelihood_probs = {}
        for word in vocab:
            likelihood_probs[word] = {
                        'ham': (word_counts[word]['ham'] + 1) / (class_counts['ham'] + len(vocab)),
                        'spam': (word_counts[word]['spam'] + 1) / (class_counts['spam'] + len(vocab))
                    }

        return likelihood_probs


    def predict(self, email, threshold=0.6):
        tokens = self.tokenize(self.preprocess_text(email))

        word_counts, class_counts = self.counts()
        prior_ham = self._update_counts(self.df, word_counts, class_counts)
        prior_spam = self._update_counts(self.df, word_counts, class_counts)

        processed_df = self.df
        vocab = self._set_vobab(processed_df,self.vocab)

        prior_ham, prior_spam = self.calculate(self.df, class_counts)
        likelihood_probs = self._update_likelihood(word_counts, class_counts, vocab)


        log_prob_ham = np.log(prior_ham) + sum(np.log(likelihood_probs.get(word, {'ham':1})['ham']) for word in tokens)
        log_prob_spam = np.log(prior_spam) + sum(np.log(likelihood_probs.get(word, {'spam':1})['spam']) for word in tokens)

        if log_prob_ham - log_prob_spam > np.log(threshold):
            return 'ham'
        else:
            return 'spam'


if __name__ == '__main__':
    #change to your dataset
    df = pd.read_csv("/Users/felipepesantez/Documents/development/datasets/email_classification.csv")
    #inference
    #new_email = "Win bitcoin today, click here: "
    #new_email = "Are you free today?, I can come around 2pm"
    new_email = input("Enter a message to classify: ")

    #model instance
    model = NaiveBayesClassifier(df)


    #save the model
    with open("naive_model.pkl","wb") as file:
        pickle.dump(model, file)

    predicted_label = model.predict(new_email, threshold=0.5)
    print("Predicted label: ", predicted_label)

