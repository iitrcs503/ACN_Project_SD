import csv
import sys
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
reload(sys)
sys.setdefaultencoding('utf8')
data=open("Twitter Spam Dataset.csv",'rU')
text=[]
for i in data:
	temp=i.split(',')
	if len(temp)>2 and temp[-1][:-1] in ['Spam','Ham']:
		temp1=""
		for i in temp[:-1]:
			temp1=temp1+i
		text.append([temp1,temp[-1]])
	elif len(temp)==2 and temp[-1][:-1] in ['Spam','Ham']:
		text.append(temp)
	else:
		pass
tweets_spam=[]
tweets_ham=[]
alphabet=set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
stopwords=set(stopwords.words("english"))
for i in text:
	words=re.sub("[^a-zA-Z]"," ",i[0]).lower().split()
	words=[w for w in words if w not in stopwords]
	words=[w for w in words if w not in alphabet]
	i[0]=" ".join(words)
	if i[1][:-1]=='Spam':
		tweets_spam.append(i[0])
	elif i[1][:-1]=='Ham':
		tweets_ham.append(i[0])

#open("crap3","w").write(str(tweets_spam))
#open("crap4","w").write(str(tweets_ham))


test_tweets_spam=tweets_spam[:int(len(tweets_spam)*0.20)]
test_tweets_ham=tweets_ham[:int(len(tweets_ham)*0.20)]
tweets_spam=tweets_spam[int(len(tweets_spam)*0.20):]
tweets_ham=tweets_ham[int(len(tweets_ham)*0.20):]

#print test_tweets_spam in tweets_spam
#print test_tweets_ham in tweets_ham


vectorizer = CountVectorizer(analyzer = "word",tokenizer = None,preprocessor = None,stop_words = None,max_features = 5000)
tweets_bow = vectorizer.fit_transform(tweets_spam+tweets_ham)
tweets_bow = tweets_bow.toarray()


#print tweets_bow.shape
#vocab = vectorizer.get_feature_names()
#print vocab
forest = RandomForestClassifier(n_estimators = 100)
#classification=[i[1] for i in text]
forest = forest.fit(tweets_bow, ["Spam"]*len(tweets_spam)+["ham"]*len(tweets_ham))
print "training completed"
#test=["hi how are you","hi lets catch up","prayers and wishes","u","a","taylor full talenteda amiabley yearned loyalo one amillionr reseverved best best write taylor name full"]
#test spam features
test_data_features = vectorizer.transform(test_tweets_spam)
test_data_features = test_data_features.toarray()
result = forest.predict(test_data_features)
open("test_spam_result.txt","w").write(str(result))

#test ham features
test_data_features = vectorizer.transform(test_tweets_ham)
test_data_features = test_data_features.toarray()
result = forest.predict(test_data_features)
open("test_ham_result.txt","w").write(str(result))
print "Completed"
