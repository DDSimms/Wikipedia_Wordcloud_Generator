# Requires user-config file in same directory as .py

import pywikibot
import mwparserfromhell
from wordcloud import WordCloud
import matplotlib.pyplot as plt

site = pywikibot.Site()  # Site object
page = pywikibot.Page(site, u"Data (computing)")  # Wikipedia entry in quotes

wikicode_unparsed = page.get()
wikicode_parsed = mwparserfromhell.parse(wikicode_unparsed)

plain_text = wikicode_parsed.strip_code()

wordcloud = WordCloud(width=1200, height=600, max_font_size=150, background_color='white', colormap='Blues').generate(plain_text)

plt.figure(figsize=[12, 8])
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
