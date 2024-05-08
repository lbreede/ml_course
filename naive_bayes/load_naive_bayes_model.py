import pickle
from naive_bayes_class import NaiveBayesClassifier

with open("naive_model.pkl","rb") as file:
    model = pickle.load(file)

with open("/Users/felipepesantez/Documents/ML_COURSE/test_stage/users_dialogue.txt","r") as text_file:
    text_lines = text_file.readlines()

for line in text_lines:
    predicted_label = model.predict(line, threshold=0.5)
    print(line)
    print("Predicted label: ", predicted_label)
