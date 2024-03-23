import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from wordcloud import WordCloud, STOPWORDS
df = pd.read_csv('online_course.csv')
df.dropna(axis=0)
df.drop_duplicates()
df['Launch Date'] = [datetime.strptime(date, '%m/%d/%Y').year for date in df['Launch Date']]


#1. Print the line charts of total online course number for two universities
def course_number():
    df2 = df.groupby(['Launch Date','Institution'], as_index=False).size()
    x = df2[df2["Institution"] == "HarvardX"]["Launch Date"]
    y_harvard = df2[df2["Institution"] == "HarvardX"]["size"]
    y_mit = df2[df2["Institution"] == "MITx"]["size"]

    plt.plot(x, y_harvard)
    plt.plot(x, y_mit)
    plt.xticks(x)
    plt.xlabel("Year")
    plt.ylabel("Distinct course numbers")
    plt.legend(["Harvard", "MIT"])
    plt.title("The distinct courses number offerd by two institutions")
    plt.show()

#2.Print the popular subject
def popular_subject():
    text = "".join(df['Course Subject'])
    wordcloud = WordCloud(
        width = 800, height = 400, background_color='white', stopwords=STOPWORDS,
    ).generate(text)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

# 3.Age distribution of students
def age_distribution():
    df['Median Age'].hist()
    plt.title('Age Distribution of students')
    plt.xlabel('Student Ages')
    plt.show()

# 4. Course display by participants number
def course_display():
    df.groupby('Course Subject')['Participants (Course Content Accessed)'].sum().plot(kind='bar')
    plt.title('Total Participants by Course Subject')
    plt.xlabel('Course Subject')
    plt.ylabel('Total Participants')
    plt.show()


if __name__ == '__main__':
    course_number()
    popular_subject()
    age_distribution()
    course_display()
