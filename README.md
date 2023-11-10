Nicholas Sanso <br>
Oct 19, 2023 <br>

# **Subreddit Classification**


## Table of Contents:
1. [Background](#section-title)
1. [Objective](#section-title)
1. [Data Description](#section-title)
1. [Model Performance](#section-title)
1. [Model and Feature Mapping](#section-title)
1. [Primary Conclusions](#section-title)
1. [Next Steps](#section-title)

<font size="6"> Background <br> </font>
          Reddit is a social media site centered around news agggregation, content rating and discussion threads. Reddit is divided into "subreddits" which are subsections reddit, bringing all of reddit's functionality to a narrow theme or subject matter. People who would like to share text with other reddit users, will create a submission. If the subject matter of a submission corresponds to a subreddit, the user will typically post the submission to that subreddit.  r_stocks and r_investing are two subreddits. <br>
          These two subreddits are deeply similar sharing a cosine similarity score of .75 according to shorttails. Similarity between subreddits is based on the cosine similarity of their word vectors. <br> <br> 
  

<font size="6"> Objective <br> </font>
Build a model that will use submission text complexity, submission engagement metrics, and submission term (word) frequency to distinguish which subreddit a submission was posted to (r_investing or r_stocks). 
 <br> 
       
  


<font size="6"> Data Description <br> </font>
| Feature | Definition |
| --- | --- |
| title | the title of a submission on reddit |
| selftext | the text content of a text submission |
| subreddit | the name of the subreddit where the submission was posted |
| ups | number of upvotes a submission has received|
| total_awards_received | number of awards a submission has received |
| num_comments| number of comments on the submission |
| character_count_title | number of characters in the document's (submission's) title|
| word_count_title| number of words in the document's (submission's) title|
| sentences_count_title | number of sentences in the document's (submission's) title |
| character_count_selftext | number of characters in the document's (submission's) selftext |
| word_count_selftext| number of words in the document's (submission's) selftext |
| sentences_count_selftext| number of sentences in the document's (submission's) selftext |
| char_over_sent_title| (character count) / (sentences count) --> for  the document's (submissions's) title |
| char_over_word_title| (character count) / (word count) --> for  the document's (submissions's) title |
| word_over_sent_title | (word count) / (sentences count) --> for  the document's (submissions's) title  |
| char_over_sent_selftext | (character count) / (sentences count) --> for  the document's (submissions's) selftext  |
| char_over_word_selftext | (character count) / (word count) --> for  the document's (submissions's) selftext |
| word_over_char_selftext |(word count) / (character count) --> for  the document's (submissions's) selftext |
<br>

            

<font size="6">Model and Feature Mapping <br> </font>
<img src="feature_and_model_map" alt="Alt text" width="800" height="400">
<img src="preprocessing" alt="Alt text" width="800" height="400">



<font size="6">4. Model Performance on training/test data<br> </font>
| Metrics of Base Models | Logistic selftext | Logistic title  | AdaBoost 
|----------|----------|----------|----------|
|train accuracy          |  0.995     |   0.882       |  0.699           
|validation accuracy          |     0.772     |  0.743        |   0.729
|cross validation standard deviation          |  0.0127        |  0.0142        |    0.0124 
|cross validation mean         |  0.761        |  0.730        |    0.654       



| Engagement Metrics of Base Models | Knn | RF | Decision Tree  |
|----------|----------|----------|----------|
|train accuracy        |0.689|    0.727      |   0.6811       |
|validation accuracy     |  0.631       |     0.645    |    0.643      |
|cross validation standard deviation|    0.0136     |     0.0108     |   0.0090        |
|cross validation mean        |    0.655     |    0.663     |     0.6626     |


| Metrics of Stacked Models | Stacked Logistic Regression | Stacked Adaboost
|----------|----------|----------|
|train accuracy         |     0.7763     | 0.7748 
|validation accuracy          |   0.7911       | 0.8022
|cross validation standard deviation          |   0.0201       | 0.0195
|cross validation mean          |   0.7770       | 0.7756


<br><br>
<font size="6">5. Primary Conclusions <br> </font>
1. Due to the diversity of the features in the base models, each of which individually have predictive power, the two stacked models both outperformed all their component base models in the validation accuracy and cross validation mean metrics.
2. The logistic regression model that was trained exclusively on the Tfidvectorizer of the title text was nearly as accurate as the logistic regression model that was trained exclusively on the TfidVectorizer of the submission text. Signaling that there is almost as much predictive power in the title of a submission as there is in the entire body of the submission.
3. The ridge regression regularizer was the optimal regularizer for both the submission text and title text models, likely a result of the high correlation of features in the documents. 
4. The validation accuracy of the AdaBoost model which used only metrics representing the complexity of the language of the features was 72.9%, showing that the complexity and length of the words, sentences and document itself are indicative of which subreddit the document belongs to.
5. The validation accuracy of the Knn, RF, and Decision Tree models show that the engagement on the submission is indicative of which subreddit the post belongs to.





<br><br>
<font size="6">6. Next steps<br> </font>

1) Feature engineer more specific grammatical features which count: <br>
    a) Coordinating conjunctions ("for, "and", "nor", "but", "or" "yet"), followed by a comma allows you to join two independent clauses together, creating compound sentences. <br>
    b) Commas not associated with a coordinating conjunctions to count the number of complex sentences<br>
    c) The number of sentences with high word counts and a coordinating conjunction but no comma in order to try to gauge how many submissions might be forgetting to use commas. <br>
    d) The number of sentences with high comma to character counts to gauge how many submissions might be misusing commas. <br>
    e) Misplaced and incorrectly used commas to see if grammar mistakes could serve as a feature. <br>
2) Apply Random Forest to the length and ratio features. Random Forests are good with multicollinearity and unscaled data. Also good at incorporating uneven predictive power of different features in the feature set.<br>
 </font>
 
### sources: 
1. https://www.shorttails.io/interactive-map-of-reddit-and-subreddit-similarity-calculator/
2. https://fivethirtyeight.com/features/dissecting-trumps-most-rabid-online-following/
3. 'https://oauth.reddit.com/r/investing' <br>
4. 'https://oauth.reddit.com/r/stocks'<br>
    
   
    
    



 
