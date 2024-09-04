from textblob import TextBlob
def check_sentiment(text):
    blob=TextBlob(text)
    score=blob.sentiment.polarity

    if score>0:
        return "Positive"
    elif score<0:
        return "Negative"
    else:
        return "Neutral"
    
def main():
    ans = "Yes"
    while(ans=="Yes"):
        inputText= input("Enter a sentence: ")
        sentiment= check_sentiment(inputText)
        print(f"The sentiment of the text is: {sentiment}")
        ans=input("Would you like to check another sentence. (Yes or No)\n")
if __name__ == "__main__":
    main()

