import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#load all tweets text
def loadTweets(tweetData, polarityList, subjectivityList):
	for tweet in tweetData:
		tweetblob = TextBlob(tweet["text"])
		polarityList.append(tweetblob.polarity)
		subjectivityList.append(tweetblob.subjectivity)

#Display Polarity Histogram Graph
def displayPolarityHistogram(polarityList):
	plt.hist(polarityList, bins=[-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
	plt.xlabel('Polarities')
	plt.ylabel('Number of Tweets')
	plt.title('Histogram of Tweet Polarity')
	plt.axis([-1.1, 1.1, 0, 80])
	plt.grid(True)
	plt.show()

#Display Subjectivity Histogram Graph
def displaySubjectivityHistogram(subjectivityList):
	plt.hist(subjectivityList, bins=[-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
	plt.xlabel('Subjectivities')
	plt.ylabel('Number of Tweets')
	plt.title('Histogram of Tweet Subjectivity')
	plt.axis([-1.1, 1.1, 0, 60])
	plt.grid(True)
	plt.show()

#Scatter plot: Polarity vs Subjectivity
def displayPolarityvsSubjectivityPlot(polarityList, subjectivityList):
	plt.plot(polarityList, subjectivityList, 'ro')
	plt.xlabel('Polarity')
	plt.ylabel('Subjectivity')
	plt.title('Tweet Polarity vs Subjectivity')
	plt.axis([-1.1, 1.1, -0.1, 1.1])
	plt.grid(True)
	plt.show()

def calculatePolarityAvg(polarityList):
	totalPolarity = 0
	for eachPolarity in polarityList:
		totalPolarity += eachPolarity
	return totalPolarity/len(polarityList)

def calculateSubjectivityAvg(subjectivityList):
	totalSubjectivity = 0
	for eachSubjectivity in subjectivityList:
		totalSubjectivity += 0
	return totalSubjectivity/len(subjectivityList)

def main():
	# Want to open the JSON file. Tag the file as
	# "r" read only because only going to look at the data.
	tweetFile = open("TwitterData/tweets_small.json", "r")
	# Using the JSON library to get data from the file as JSON data.
	tweetData = json.load(tweetFile)
	#Closing the file now that data is locally stored
	tweetFile.close()

	polarityList = []
	subjectivityList =[]
	loadTweets(tweetData, polarityList, subjectivityList)

	displayPolarityHistogram(polarityList)
	displaySubjectivityHistogram(subjectivityList)
	displayPolarityvsSubjectivityPlot(polarityList, subjectivityList)

	print("The average tweet polarity is: " + str(calculatePolarityAvg(polarityList)))
	print("The average tweet subjectivity is: " + str(calculateSubjectivityAvg(subjectivityList)))

if __name__ == "__main__":
	main()
