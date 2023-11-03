# filename: word_cloud.py

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample headlines
headlines = [
    "Breaking News: New Study Reveals Surprising Discoveries",
    "COVID-19 Cases Continue to Rise in Several Countries",
    "Tech Giants Announce Exciting New Products",
    "Sports Team Wins Championship After Intense Match",
    "Weather Forecast: Sunny and Clear Skies All Week"
]

# Combine all headlines into a single string
all_text = ' '.join(headlines)

# Generate the word cloud
wordcloud = WordCloud(background_color='white').generate(all_text)

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# Save the word cloud as an image
wordcloud.to_file('word_cloud.png')