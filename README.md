# TweetVisualization
Data Visualization of Tweets regarding Automation
--

Using data from Twitter, I wanted to find out how people feel about "automation" by doing some sentiment analysis on the data. I used the TextBlob library's algorithm for sentiment analysis.

Afterwards, I used the sentiment data to create visuals that can represent how positive or negative the tweets are. Specifically, I created two histograms - one for polarity, another for subjectivity - and a scatter plot graph that compares polarity vs. subjectivity from the dataset. 

The polarity attribute in TextBlob is a float type which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement. Subjective sentences generally refer to personal opinion, emotion or judgment whereas objective refers to factual information. Subjectivity is also a float type which lies in the range of [0,1].

A histogram is a bar graph that shows how many things are in each range of values. A Scatter Plot has points that show the relationship between two sets of data. 

Below are the graphs, I produced:

![](https://user-images.githubusercontent.com/9923181/49534962-f093d780-f890-11e8-934a-9360b5a0e5d6.png)

![](https://user-images.githubusercontent.com/9923181/49534921-d22ddc00-f890-11e8-8f9c-c7c1e2428e21.png)

Based on the histogram, the data follows the shape of a bell curve. Most tweets on the topic of automation are on a neutral to positive polarity spectrum (meaning mostly neutral to positive statements). 

![](https://user-images.githubusercontent.com/9923181/49534944-e1ad2500-f890-11e8-9ea6-b9340b9c5388.png)

Based on the histogram, majority of people's tweets were either very objective or very subjective. Majority were subjective rather than objective. 
