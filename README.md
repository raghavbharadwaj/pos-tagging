Homework-2 ---- Part IV

1) Accuracy of Part of Speech Tagger : 0.9391031233641598 ( 93.91% )

2) Precision and Recall Name Entity Recognizer

B-MISC Precision: 0.5052910052910053  Recall: 0.42921348314606744 f-score: 0.4641555285540705

B-LOC Precision: 0.5530492898913951  Recall: 0.6727642276422764 f-score: 0.6070609812012838

B-PER Precision: 0.8164556962025317  Recall: 0.527823240589198 f-score: 0.6411530815109345

B-ORG Precision: 0.6891223733003708  Recall: 0.6558823529411765 f-score: 0.6720916214587102

Overall Precision: 0.6560381621893046  Recall: 0.6005515973339463 f-score: 0.6270698344132469

3) Accuracy of POS Tagging using Naive Bayes Classifier : 0.91033726350425 ( 91.03% )
   Accuracy of NER using Naive Bayes Classifier : 0.901 (90.1% )

The performance metrix decreases upon using Naive Bayes Classifier as there is no provision in Naive bayes classification 
to learn from erroneous predictions and all the classification is based on prior probabilities. Also, the classification using
Average perceptron has many types of tuning to get a more accurate model. 
