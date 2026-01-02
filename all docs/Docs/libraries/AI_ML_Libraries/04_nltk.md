# NLTK - Natural Language Processing Library

> **What is it?** Library for processing and analyzing human language (text)
> **Install:** `pip install nltk`
> **Import as:** `import nltk`

---

## Table of Contents

1. [What is NLTK?](#1-what-is-nltk)
2. [Installation](#2-installation)
3. [Core Concepts](#3-core-concepts)
4. [Tokenization](#4-tokenization)
5. [Stop Words](#5-stop-words)
6. [Stemming and Lemmatization](#6-stemming-and-lemmatization)
7. [Part-of-Speech Tagging](#7-part-of-speech-tagging)
8. [Named Entity Recognition](#8-named-entity-recognition)
9. [Sentiment Analysis](#9-sentiment-analysis)
10. [Text Preprocessing Pipeline](#10-text-preprocessing-pipeline)
11. [Frequency Analysis](#11-frequency-analysis)
12. [Real-World Examples](#12-real-world-examples)
13. [Quick Reference](#13-quick-reference)

---

## 1. What is NLTK?

### Simple Explanation

NLTK (Natural Language Toolkit) helps computers **understand human language**.

```
What can NLTK do?

Break text into pieces:
- "Hello world" → ["Hello", "world"]

Understand grammar:
- "The cat sat" → cat = noun, sat = verb

Clean text:
- Remove "the", "is", "a" (common words)
- Convert "running" → "run"

Analyze meaning:
- "I love this!" → Positive sentiment
- "This is terrible" → Negative sentiment

Used in:
- Chatbots
- Spam detection
- Sentiment analysis
- Search engines
- Translation
```

### Why NLTK for AI/ML?

```
Machine Learning needs numbers → Text is not numbers

NLTK converts text to data:
1. "The movie was great!" (raw text)
2. ["movie", "great"] (tokenized, cleaned)
3. [0.5, 0.8, 0.2, ...] (vectors for ML)
4. Feed to model (scikit-learn, TensorFlow)

NLTK = The tool that prepares text for AI
```

---

## 2. Installation

```bash
# Install NLTK
pip install nltk

# Verify installation
python -c "import nltk; print(nltk.__version__)"
```

### Download Required Data

```python
import nltk

# Download everything (recommended for beginners)
nltk.download('all')  # ~3GB, takes time

# Or download only what you need
nltk.download('punkt')         # Tokenizer
nltk.download('stopwords')     # Common words to remove
nltk.download('wordnet')       # Dictionary for lemmatization
nltk.download('averaged_perceptron_tagger')  # POS tagging
nltk.download('maxent_ne_chunker')  # Named entity recognition
nltk.download('words')         # English words list
nltk.download('vader_lexicon') # Sentiment analysis
```

### Basic Import

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

print("NLTK ready!")
```

---

## 3. Core Concepts

### 3.1 NLP Terminology

| Term | Meaning | Example |
|------|---------|---------|
| **Token** | A single piece (word/punctuation) | "Hello" |
| **Tokenization** | Breaking text into tokens | "Hi there" → ["Hi", "there"] |
| **Corpus** | Collection of texts | All Wikipedia articles |
| **Stop Words** | Common words to ignore | "the", "is", "a", "an" |
| **Stemming** | Cut word to root | "running" → "run" |
| **Lemmatization** | Find dictionary form | "better" → "good" |
| **POS Tag** | Part of speech | "cat" → Noun |
| **NER** | Named Entity Recognition | "Apple" → Organization |

### 3.2 The NLP Pipeline

```
Raw Text: "The movie was really great! I loved it."
                    ↓
        ┌───────────────────┐
        │   1. Tokenize     │ → ["The", "movie", "was", ...]
        └─────────┬─────────┘
                  ↓
        ┌───────────────────┐
        │  2. Lowercase     │ → ["the", "movie", "was", ...]
        └─────────┬─────────┘
                  ↓
        ┌───────────────────┐
        │ 3. Remove Stops   │ → ["movie", "really", "great", "loved"]
        └─────────┬─────────┘
                  ↓
        ┌───────────────────┐
        │ 4. Lemmatize      │ → ["movie", "really", "great", "love"]
        └─────────┬─────────┘
                  ↓
           Clean tokens ready for ML!
```

---

## 4. Tokenization

### 4.1 Word Tokenization

```python
from nltk.tokenize import word_tokenize

text = "Hello, how are you? I'm doing great!"

# Tokenize into words
tokens = word_tokenize(text)
print(tokens)
# Output: ['Hello', ',', 'how', 'are', 'you', '?', 'I', "'m", 'doing', 'great', '!']

# Count tokens
print(f"Number of tokens: {len(tokens)}")
# Output: Number of tokens: 11
```

### 4.2 Sentence Tokenization

```python
from nltk.tokenize import sent_tokenize

text = """Natural language processing is fun.
It helps computers understand text.
NLTK makes it easy!"""

# Tokenize into sentences
sentences = sent_tokenize(text)
for i, sentence in enumerate(sentences, 1):
    print(f"Sentence {i}: {sentence}")

# Output:
# Sentence 1: Natural language processing is fun.
# Sentence 2: It helps computers understand text.
# Sentence 3: NLTK makes it easy!
```

### 4.3 Different Tokenizers

```python
from nltk.tokenize import (
    word_tokenize,
    TreebankWordTokenizer,
    WordPunctTokenizer,
    RegexpTokenizer
)

text = "Can't stop won't stop!"

# word_tokenize (recommended)
print("word_tokenize:", word_tokenize(text))
# Output: ['Ca', "n't", 'stop', 'wo', "n't", 'stop', '!']

# TreebankWordTokenizer (similar to word_tokenize)
treebank = TreebankWordTokenizer()
print("Treebank:", treebank.tokenize(text))

# WordPunctTokenizer (splits on punctuation)
wordpunct = WordPunctTokenizer()
print("WordPunct:", wordpunct.tokenize(text))
# Output: ['Can', "'", 't', 'stop', 'won', "'", 't', 'stop', '!']

# RegexpTokenizer (custom pattern)
regexp = RegexpTokenizer(r'\w+')  # Only words (no punctuation)
print("Regexp:", regexp.tokenize(text))
# Output: ['Can', 't', 'stop', 'won', 't', 'stop']
```

---

## 5. Stop Words

### 5.1 What are Stop Words?

```
Stop words = Common words that don't add much meaning

Examples:
- "the", "a", "an", "is", "are", "was", "were"
- "in", "on", "at", "to", "for", "of"
- "I", "you", "he", "she", "it", "we", "they"

Why remove them?
- Reduce noise in data
- Focus on meaningful words
- Smaller vocabulary
- Faster processing
```

### 5.2 Using Stop Words

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Get English stop words
stop_words = set(stopwords.words('english'))
print(f"Number of stop words: {len(stop_words)}")
# Output: Number of stop words: 179

# See some examples
print("Sample stop words:", list(stop_words)[:10])
# Output: ['ourselves', 'hers', 'between', 'yourself', ...]

# Remove stop words from text
text = "This is a sample sentence showing off the stop words filtration."
tokens = word_tokenize(text.lower())

# Filter out stop words
filtered = [word for word in tokens if word not in stop_words]

print(f"Original: {tokens}")
print(f"Filtered: {filtered}")
# Output:
# Original: ['this', 'is', 'a', 'sample', 'sentence', ...]
# Filtered: ['sample', 'sentence', 'showing', 'stop', 'words', 'filtration', '.']
```

### 5.3 Custom Stop Words

```python
from nltk.corpus import stopwords

# Start with default stop words
stop_words = set(stopwords.words('english'))

# Add custom stop words
custom_stops = {'movie', 'film', 'watch'}
stop_words = stop_words.union(custom_stops)

# Remove specific stop words
stop_words.discard('not')  # Keep "not" (important for sentiment)

print(f"Custom stop words count: {len(stop_words)}")
```

---

## 6. Stemming and Lemmatization

### 6.1 Stemming (Fast but Crude)

```python
from nltk.stem import PorterStemmer, SnowballStemmer

# Porter Stemmer (most common)
porter = PorterStemmer()

words = ['running', 'runs', 'ran', 'runner', 'easily', 'fairly']

print("Porter Stemmer:")
for word in words:
    print(f"  {word} → {porter.stem(word)}")

# Output:
# running → run
# runs → run
# ran → ran
# runner → runner
# easily → easili (not a real word!)
# fairly → fairli (not a real word!)

# Snowball Stemmer (improved Porter)
snowball = SnowballStemmer('english')

print("\nSnowball Stemmer:")
for word in words:
    print(f"  {word} → {snowball.stem(word)}")
```

### 6.2 Lemmatization (Slower but Better)

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Lemmatize with default (noun)
words = ['running', 'runs', 'ran', 'better', 'studies', 'studying']

print("Default lemmatization (noun):")
for word in words:
    print(f"  {word} → {lemmatizer.lemmatize(word)}")
# Output: running → running (wrong! it's treating as noun)

# Lemmatize with correct POS (part of speech)
# v = verb, n = noun, a = adjective, r = adverb
print("\nWith correct POS:")
print(f"  running (v) → {lemmatizer.lemmatize('running', 'v')}")  # run
print(f"  better (a) → {lemmatizer.lemmatize('better', 'a')}")    # good
print(f"  studies (v) → {lemmatizer.lemmatize('studies', 'v')}")  # study
print(f"  studies (n) → {lemmatizer.lemmatize('studies', 'n')}")  # study
```

### 6.3 Stemming vs Lemmatization

| Feature | Stemming | Lemmatization |
|---------|----------|---------------|
| Speed | Fast | Slower |
| Accuracy | Lower | Higher |
| Output | May not be real word | Always real word |
| Uses dictionary | No | Yes |
| When to use | Large datasets, speed needed | When accuracy matters |

```python
from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ['caring', 'better', 'studies', 'wolves']

print("Comparison:")
print(f"{'Word':<10} {'Stemmed':<10} {'Lemmatized':<10}")
print("-" * 30)
for word in words:
    stemmed = stemmer.stem(word)
    lemmatized = lemmatizer.lemmatize(word)
    print(f"{word:<10} {stemmed:<10} {lemmatized:<10}")

# Output:
# Word       Stemmed    Lemmatized
# ------------------------------
# caring     care       caring
# better     better     better
# studies    studi      study
# wolves     wolv       wolf
```

---

## 7. Part-of-Speech Tagging

### 7.1 What is POS Tagging?

```
POS = Part of Speech

Identifies the grammatical role of each word:
- Noun (NN): person, place, thing
- Verb (VB): action
- Adjective (JJ): describes noun
- Adverb (RB): describes verb
- Pronoun (PRP): he, she, it
```

### 7.2 Using POS Tagger

```python
import nltk
from nltk.tokenize import word_tokenize

text = "The quick brown fox jumps over the lazy dog"
tokens = word_tokenize(text)

# Get POS tags
tagged = nltk.pos_tag(tokens)
print(tagged)
# Output: [('The', 'DT'), ('quick', 'JJ'), ('brown', 'JJ'),
#          ('fox', 'NN'), ('jumps', 'VBZ'), ('over', 'IN'),
#          ('the', 'DT'), ('lazy', 'JJ'), ('dog', 'NN')]

# Pretty print
print("\nPOS Tags:")
for word, tag in tagged:
    print(f"  {word}: {tag}")
```

### 7.3 Common POS Tags

| Tag | Meaning | Example |
|-----|---------|---------|
| NN | Noun (singular) | dog, car |
| NNS | Noun (plural) | dogs, cars |
| VB | Verb (base) | run, eat |
| VBD | Verb (past tense) | ran, ate |
| VBG | Verb (gerund) | running, eating |
| VBZ | Verb (3rd person) | runs, eats |
| JJ | Adjective | big, red |
| RB | Adverb | quickly, very |
| DT | Determiner | the, a |
| IN | Preposition | in, on, at |
| PRP | Pronoun | I, you, he |

### 7.4 Filter by POS Tag

```python
import nltk
from nltk.tokenize import word_tokenize

text = "The beautiful princess quickly kissed the ugly frog"
tokens = word_tokenize(text)
tagged = nltk.pos_tag(tokens)

# Get only nouns
nouns = [word for word, tag in tagged if tag.startswith('NN')]
print(f"Nouns: {nouns}")
# Output: Nouns: ['princess', 'frog']

# Get only adjectives
adjectives = [word for word, tag in tagged if tag.startswith('JJ')]
print(f"Adjectives: {adjectives}")
# Output: Adjectives: ['beautiful', 'ugly']

# Get only verbs
verbs = [word for word, tag in tagged if tag.startswith('VB')]
print(f"Verbs: {verbs}")
# Output: Verbs: ['kissed']
```

---

## 8. Named Entity Recognition

### 8.1 What is NER?

```
NER = Named Entity Recognition

Finds and classifies named entities in text:
- PERSON: People names
- ORGANIZATION: Companies, institutions
- GPE: Countries, cities (Geo-Political Entity)
- DATE: Dates and times
- MONEY: Monetary values
- PERCENT: Percentages
```

### 8.2 Using NER

```python
import nltk
from nltk.tokenize import word_tokenize

text = "Apple Inc. was founded by Steve Jobs in California. The company is worth $2 trillion."

# Tokenize and POS tag
tokens = word_tokenize(text)
tagged = nltk.pos_tag(tokens)

# Named Entity Recognition
entities = nltk.ne_chunk(tagged)
print(entities)

# Extract named entities
print("\nNamed Entities:")
for chunk in entities:
    if hasattr(chunk, 'label'):
        entity_name = ' '.join(c[0] for c in chunk)
        entity_type = chunk.label()
        print(f"  {entity_name}: {entity_type}")

# Output:
# Apple Inc.: ORGANIZATION
# Steve Jobs: PERSON
# California: GPE
```

### 8.3 Extract Specific Entities

```python
import nltk
from nltk.tokenize import word_tokenize

def extract_entities(text, entity_type='PERSON'):
    """Extract specific entity types from text"""
    tokens = word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.ne_chunk(tagged)

    found = []
    for chunk in entities:
        if hasattr(chunk, 'label') and chunk.label() == entity_type:
            entity = ' '.join(c[0] for c in chunk)
            found.append(entity)

    return found

text = """
Elon Musk is the CEO of Tesla and SpaceX.
He was born in South Africa.
Bill Gates founded Microsoft in Seattle.
"""

print("People:", extract_entities(text, 'PERSON'))
print("Organizations:", extract_entities(text, 'ORGANIZATION'))
print("Locations:", extract_entities(text, 'GPE'))

# Output:
# People: ['Elon Musk', 'Bill Gates']
# Organizations: ['Tesla', 'SpaceX', 'Microsoft']
# Locations: ['South Africa', 'Seattle']
```

---

## 9. Sentiment Analysis

### 9.1 Using VADER Sentiment

```python
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# Analyze sentiment
texts = [
    "I love this product! It's amazing!",
    "This is the worst experience ever.",
    "The movie was okay, nothing special.",
    "Not bad, but not great either."
]

for text in texts:
    scores = sia.polarity_scores(text)
    print(f"\nText: {text}")
    print(f"  Scores: {scores}")

    # Interpret compound score
    compound = scores['compound']
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    print(f"  Sentiment: {sentiment}")

# Output example:
# Text: I love this product! It's amazing!
#   Scores: {'neg': 0.0, 'neu': 0.286, 'pos': 0.714, 'compound': 0.8516}
#   Sentiment: Positive
```

### 9.2 Understanding VADER Scores

```python
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
scores = sia.polarity_scores("I really love this amazing product!")

print("Score breakdown:")
print(f"  Negative: {scores['neg']}")   # 0.0 to 1.0
print(f"  Neutral: {scores['neu']}")    # 0.0 to 1.0
print(f"  Positive: {scores['pos']}")   # 0.0 to 1.0
print(f"  Compound: {scores['compound']}")  # -1.0 to 1.0

# Compound score interpretation:
# >= 0.05: Positive
# <= -0.05: Negative
# Between: Neutral
```

### 9.3 Batch Sentiment Analysis

```python
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

sia = SentimentIntensityAnalyzer()

# Sample reviews
reviews = [
    "Great product, fast shipping!",
    "Terrible quality, waste of money.",
    "It's okay, does the job.",
    "Absolutely love it! Best purchase ever!",
    "Not what I expected, disappointed."
]

# Analyze all reviews
results = []
for review in reviews:
    scores = sia.polarity_scores(review)
    results.append({
        'review': review,
        'compound': scores['compound'],
        'sentiment': 'Positive' if scores['compound'] >= 0.05 else
                    ('Negative' if scores['compound'] <= -0.05 else 'Neutral')
    })

# Create DataFrame
df = pd.DataFrame(results)
print(df)

# Summary
print(f"\nSentiment Summary:")
print(df['sentiment'].value_counts())
```

---

## 10. Text Preprocessing Pipeline

### 10.1 Complete Pipeline

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import re

def preprocess_text(text):
    """
    Complete text preprocessing pipeline
    """
    # 1. Lowercase
    text = text.lower()

    # 2. Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)

    # 3. Remove emails
    text = re.sub(r'\S+@\S+', '', text)

    # 4. Remove numbers (optional)
    text = re.sub(r'\d+', '', text)

    # 5. Tokenize
    tokens = word_tokenize(text)

    # 6. Remove punctuation
    tokens = [token for token in tokens if token not in string.punctuation]

    # 7. Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # 8. Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # 9. Remove short words (optional)
    tokens = [token for token in tokens if len(token) > 2]

    return tokens

# Test
raw_text = """
Check out this website: https://example.com
The movies were absolutely AMAZING!!! I've been watching them for 5 years.
Contact me at test@email.com for more info.
"""

cleaned = preprocess_text(raw_text)
print(f"Original:\n{raw_text}")
print(f"\nCleaned tokens:\n{cleaned}")

# Output:
# Cleaned tokens:
# ['check', 'website', 'movie', 'absolutely', 'amazing', 'watching', 'year', 'contact', 'info']
```

### 10.2 Pipeline as a Class

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import re

class TextPreprocessor:
    def __init__(self, remove_stopwords=True, lemmatize=True, min_word_length=2):
        self.remove_stopwords = remove_stopwords
        self.lemmatize = lemmatize
        self.min_word_length = min_word_length
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def clean(self, text):
        """Clean a single text"""
        # Lowercase
        text = text.lower()

        # Remove URLs, emails, numbers
        text = re.sub(r'http\S+|www\S+|https\S+', '', text)
        text = re.sub(r'\S+@\S+', '', text)
        text = re.sub(r'\d+', '', text)

        # Tokenize
        tokens = word_tokenize(text)

        # Remove punctuation
        tokens = [t for t in tokens if t not in string.punctuation]

        # Remove stop words
        if self.remove_stopwords:
            tokens = [t for t in tokens if t not in self.stop_words]

        # Lemmatize
        if self.lemmatize:
            tokens = [self.lemmatizer.lemmatize(t) for t in tokens]

        # Remove short words
        tokens = [t for t in tokens if len(t) >= self.min_word_length]

        return tokens

    def clean_batch(self, texts):
        """Clean multiple texts"""
        return [self.clean(text) for text in texts]

# Usage
preprocessor = TextPreprocessor()

texts = [
    "I love this amazing product!",
    "The service was terrible and slow.",
    "Check out https://example.com for deals!"
]

cleaned = preprocessor.clean_batch(texts)
for original, clean in zip(texts, cleaned):
    print(f"Original: {original}")
    print(f"Cleaned:  {clean}\n")
```

---

## 11. Frequency Analysis

### 11.1 Word Frequency

```python
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

text = """
Natural language processing is a field of artificial intelligence.
It helps computers understand human language.
NLP is used in many applications like chatbots and translation.
Machine learning is often used in natural language processing.
"""

# Tokenize and clean
tokens = word_tokenize(text.lower())
tokens = [t for t in tokens if t not in string.punctuation]
tokens = [t for t in tokens if t not in stopwords.words('english')]

# Create frequency distribution
fdist = FreqDist(tokens)

# Most common words
print("Most common words:")
for word, count in fdist.most_common(10):
    print(f"  {word}: {count}")

# Total words
print(f"\nTotal unique words: {len(fdist)}")
print(f"Total words: {fdist.N()}")

# Frequency of specific word
print(f"\nFrequency of 'language': {fdist['language']}")
```

### 11.2 N-grams (Word Combinations)

```python
from nltk import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

text = "I love natural language processing and machine learning"
tokens = word_tokenize(text.lower())

# Bigrams (2 words)
bigrams = list(ngrams(tokens, 2))
print("Bigrams:")
for bg in bigrams:
    print(f"  {bg}")

# Trigrams (3 words)
trigrams = list(ngrams(tokens, 3))
print("\nTrigrams:")
for tg in trigrams:
    print(f"  {tg}")

# Count n-grams
bigram_counts = Counter(bigrams)
print("\nMost common bigrams:")
for bg, count in bigram_counts.most_common(5):
    print(f"  {' '.join(bg)}: {count}")
```

### 11.3 Visualize Frequency

```python
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import string

text = """
Python is a great programming language. Python is easy to learn.
Machine learning with Python is powerful. Python has many libraries.
Data science uses Python extensively. Python is popular.
"""

# Clean and tokenize
tokens = word_tokenize(text.lower())
tokens = [t for t in tokens if t not in string.punctuation]
tokens = [t for t in tokens if t not in stopwords.words('english')]

# Frequency distribution
fdist = FreqDist(tokens)

# Plot
plt.figure(figsize=(10, 5))
fdist.plot(15, title='Word Frequency Distribution')
plt.savefig('word_frequency.png')
plt.show()
```

---

## 12. Real-World Examples

### Example 1: Spam Detection Preprocessing

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import re

def preprocess_for_spam_detection(text):
    """Preprocess text for spam classification"""
    # Lowercase
    text = text.lower()

    # Remove URLs (common in spam)
    text = re.sub(r'http\S+', '[URL]', text)

    # Remove emails
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)

    # Remove phone numbers
    text = re.sub(r'\d{10,}', '[PHONE]', text)

    # Keep some spam indicators
    text = re.sub(r'\$+', ' [MONEY] ', text)
    text = re.sub(r'!{2,}', ' [EXCLAIM] ', text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove punctuation (except special tokens)
    tokens = [t for t in tokens if t not in string.punctuation or t.startswith('[')]

    # Remove stop words (but keep negations)
    stop_words = set(stopwords.words('english')) - {'not', 'no', 'never'}
    tokens = [t for t in tokens if t not in stop_words]

    return ' '.join(tokens)

# Test
spam_examples = [
    "CONGRATULATIONS!!! You won $1000!!! Click here: http://spam.com",
    "Hey, are you free for lunch tomorrow?",
    "FREE iPhone!!! Call 1234567890 NOW!!!"
]

for text in spam_examples:
    cleaned = preprocess_for_spam_detection(text)
    print(f"Original: {text}")
    print(f"Cleaned:  {cleaned}\n")
```

### Example 2: Review Analyzer

```python
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

class ReviewAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords.words('english'))

    def analyze(self, review):
        """Analyze a single review"""
        # Sentiment
        sentiment_scores = self.sia.polarity_scores(review)
        compound = sentiment_scores['compound']

        if compound >= 0.05:
            sentiment = 'Positive'
        elif compound <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        # Key words
        tokens = word_tokenize(review.lower())
        tokens = [t for t in tokens if t not in string.punctuation]
        tokens = [t for t in tokens if t not in self.stop_words]

        return {
            'review': review,
            'sentiment': sentiment,
            'score': compound,
            'key_words': tokens[:5]
        }

    def analyze_batch(self, reviews):
        """Analyze multiple reviews"""
        results = [self.analyze(r) for r in reviews]

        # Summary
        sentiments = [r['sentiment'] for r in results]
        positive = sentiments.count('Positive')
        negative = sentiments.count('Negative')
        neutral = sentiments.count('Neutral')

        summary = {
            'total': len(reviews),
            'positive': positive,
            'negative': negative,
            'neutral': neutral,
            'positive_pct': positive / len(reviews) * 100
        }

        return results, summary

# Test
analyzer = ReviewAnalyzer()

reviews = [
    "Absolutely love this product! Best purchase ever!",
    "Terrible quality, complete waste of money.",
    "It's okay, nothing special but does the job.",
    "Amazing customer service, very helpful!",
    "Would not recommend, very disappointed."
]

results, summary = analyzer.analyze_batch(reviews)

print("Individual Analysis:")
for r in results:
    print(f"  {r['sentiment']}: {r['review'][:50]}...")

print(f"\nSummary:")
print(f"  Total reviews: {summary['total']}")
print(f"  Positive: {summary['positive']} ({summary['positive_pct']:.0f}%)")
print(f"  Negative: {summary['negative']}")
print(f"  Neutral: {summary['neutral']}")
```

### Example 3: Text Similarity

```python
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

def jaccard_similarity(text1, text2):
    """Calculate Jaccard similarity between two texts"""
    # Tokenize and clean
    stop_words = set(stopwords.words('english'))

    tokens1 = set(word_tokenize(text1.lower()))
    tokens1 = {t for t in tokens1 if t not in string.punctuation and t not in stop_words}

    tokens2 = set(word_tokenize(text2.lower()))
    tokens2 = {t for t in tokens2 if t not in string.punctuation and t not in stop_words}

    # Calculate Jaccard
    intersection = tokens1.intersection(tokens2)
    union = tokens1.union(tokens2)

    if len(union) == 0:
        return 0

    return len(intersection) / len(union)

# Test
text1 = "Machine learning is a subset of artificial intelligence"
text2 = "Deep learning is part of machine learning and AI"
text3 = "The weather today is sunny and warm"

print(f"Text 1 vs Text 2: {jaccard_similarity(text1, text2):.2f}")
print(f"Text 1 vs Text 3: {jaccard_similarity(text1, text3):.2f}")
print(f"Text 2 vs Text 3: {jaccard_similarity(text2, text3):.2f}")

# Output:
# Text 1 vs Text 2: 0.33 (similar topic)
# Text 1 vs Text 3: 0.00 (different topics)
```

---

## 13. Quick Reference

### Common Imports

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import pos_tag, ne_chunk, ngrams
```

### Download Commands

```python
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')
```

### Quick Operations

| Task | Code |
|------|------|
| Word tokenize | `word_tokenize(text)` |
| Sentence tokenize | `sent_tokenize(text)` |
| Get stop words | `stopwords.words('english')` |
| Stem word | `PorterStemmer().stem(word)` |
| Lemmatize word | `WordNetLemmatizer().lemmatize(word)` |
| POS tag | `pos_tag(tokens)` |
| Named entities | `ne_chunk(pos_tag(tokens))` |
| Sentiment | `SentimentIntensityAnalyzer().polarity_scores(text)` |
| Frequency | `FreqDist(tokens)` |
| N-grams | `ngrams(tokens, n)` |

### Preprocessing Template

```python
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

def preprocess(text):
    # Lowercase
    text = text.lower()

    # Tokenize
    tokens = word_tokenize(text)

    # Remove punctuation
    tokens = [t for t in tokens if t not in string.punctuation]

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words]

    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return tokens
```

---

## Summary

NLTK is the foundation for text processing in Python:

1. **Tokenization** - Break text into words/sentences
2. **Stop Words** - Remove common words
3. **Stemming/Lemmatization** - Get root forms
4. **POS Tagging** - Identify word types
5. **NER** - Find named entities
6. **Sentiment** - Analyze opinion/emotion
7. **Frequency** - Count word occurrences

Master preprocessing before moving to advanced NLP models!
