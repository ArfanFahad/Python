# regex in - NLP (Cleaning Training Data)
import re 

text = """
RT @elonmusk: Going to Mars!!! 
#SpaceX http://spacex.com 
"""

#Let's remove mentions first 
text = re.sub(r"@\w+", "", text)

#Remove hashtags 
text = re.sub(r"#\w+", "", text)

#remove URLs
text = re.sub(r"http\S+", "", text)

#remove extra space
text = re.sub(r"\s+", " ", text).strip()

print(text)