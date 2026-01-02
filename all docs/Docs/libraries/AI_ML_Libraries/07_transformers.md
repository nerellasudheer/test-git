# Hugging Face Transformers - Pre-trained AI Models

> **What is it?** Library for using state-of-the-art pre-trained AI models
> **Install:** `pip install transformers`
> **Import as:** `from transformers import pipeline`

---

## Table of Contents

1. [What is Hugging Face Transformers?](#1-what-is-hugging-face-transformers)
2. [Installation](#2-installation)
3. [Quick Start with Pipelines](#3-quick-start-with-pipelines)
4. [Text Classification](#4-text-classification)
5. [Named Entity Recognition](#5-named-entity-recognition)
6. [Question Answering](#6-question-answering)
7. [Text Generation](#7-text-generation)
8. [Summarization](#8-summarization)
9. [Translation](#9-translation)
10. [Zero-Shot Classification](#10-zero-shot-classification)
11. [Image Classification](#11-image-classification)
12. [Using Specific Models](#12-using-specific-models)
13. [Quick Reference](#13-quick-reference)

---

## 1. What is Hugging Face Transformers?

### Simple Explanation

Hugging Face Transformers gives you access to **thousands of pre-trained AI models** that you can use instantly.

```
Traditional ML approach:
1. Collect massive data (millions of examples)
2. Train for days/weeks on expensive GPUs
3. Fine-tune and optimize
4. Finally get a working model

Hugging Face approach:
1. pip install transformers
2. Load pre-trained model
3. Use it! (3 lines of code)

It's like having access to models trained on:
- All of Wikipedia
- Millions of books
- Billions of web pages
- Without doing the training yourself!
```

### What Can It Do?

| Task | Example |
|------|---------|
| **Sentiment Analysis** | "I love this!" → Positive |
| **Text Generation** | "Once upon a time..." → Complete story |
| **Question Answering** | Context + Question → Answer |
| **Translation** | English → French, Spanish, etc. |
| **Summarization** | Long article → Short summary |
| **Named Entity Recognition** | Find people, places, organizations |
| **Image Classification** | What's in this image? |
| **Speech Recognition** | Audio → Text |

### Why Use Transformers?

```
Before Transformers (2017):
- Train separate model for each task
- Need lots of data per task
- Models didn't understand context well

After Transformers:
- One architecture, many tasks
- Pre-trained on massive data
- Understands context deeply
- State-of-the-art results

Famous Transformer Models:
- BERT (Google) - Understanding text
- GPT (OpenAI) - Generating text
- T5 (Google) - Text-to-text
- CLIP (OpenAI) - Images + Text
```

---

## 2. Installation

```bash
# Basic installation
pip install transformers

# With PyTorch (recommended)
pip install transformers torch

# With TensorFlow
pip install transformers tensorflow

# Verify installation
python -c "from transformers import pipeline; print('Transformers ready!')"
```

### First Download Warning

```
When you first use a model, it downloads automatically.
Models can be 100MB - 10GB+ depending on size.

First run:
Downloading: 100%|██████████| 440M/440M
Model cached in ~/.cache/huggingface/

Subsequent runs:
Uses cached model (instant!)
```

---

## 3. Quick Start with Pipelines

### 3.1 What is a Pipeline?

A pipeline is the **easiest way** to use pre-trained models. One line to load, one line to use!

```python
from transformers import pipeline

# Create a sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Use it!
result = classifier("I love this product!")
print(result)
# Output: [{'label': 'POSITIVE', 'score': 0.9998}]
```

### 3.2 Available Pipelines

| Pipeline | Task | Example Input |
|----------|------|---------------|
| `sentiment-analysis` | Classify sentiment | "I love this!" |
| `text-classification` | Classify text | "This is a news article..." |
| `ner` | Named Entity Recognition | "Bill Gates founded Microsoft" |
| `question-answering` | Answer questions | context + question |
| `text-generation` | Generate text | "Once upon a time" |
| `summarization` | Summarize text | Long article |
| `translation_xx_to_yy` | Translate | "Hello world" |
| `fill-mask` | Fill in blanks | "Paris is the [MASK] of France" |
| `zero-shot-classification` | Classify without training | Any text + categories |
| `image-classification` | Classify images | Image file |

### 3.3 Basic Pipeline Usage

```python
from transformers import pipeline

# ═══════════════════════════════════════════════════════════
# Method 1: Default model
# ═══════════════════════════════════════════════════════════
classifier = pipeline("sentiment-analysis")
result = classifier("I really enjoyed this movie!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.9998}]

# ═══════════════════════════════════════════════════════════
# Method 2: Specific model
# ═══════════════════════════════════════════════════════════
classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
result = classifier("Das ist fantastisch!")  # German
print(result)

# ═══════════════════════════════════════════════════════════
# Method 3: Multiple inputs
# ═══════════════════════════════════════════════════════════
texts = [
    "I love this!",
    "This is terrible.",
    "It's okay, I guess."
]
results = classifier(texts)
for text, result in zip(texts, results):
    print(f"{text} → {result['label']} ({result['score']:.2%})")
```

---

## 4. Text Classification

### 4.1 Sentiment Analysis

```python
from transformers import pipeline

# Load sentiment analyzer
sentiment = pipeline("sentiment-analysis")

# Analyze texts
texts = [
    "I absolutely love this product! Best purchase ever!",
    "This is the worst experience I've ever had.",
    "The product is okay, nothing special.",
    "Amazing customer service, very helpful!",
]

print("Sentiment Analysis Results:")
print("-" * 50)
for text in texts:
    result = sentiment(text)[0]
    print(f"Text: {text[:50]}...")
    print(f"Sentiment: {result['label']} ({result['score']:.2%})")
    print()
```

### 4.2 Multi-label Classification

```python
from transformers import pipeline

# Using a multi-label model
classifier = pipeline("text-classification", model="cardiffnlp/tweet-topic-21-multi")

text = "Just watched an amazing basketball game! Lakers won!"

result = classifier(text)
print(f"Text: {text}")
print(f"Categories: {result}")
```

---

## 5. Named Entity Recognition

### 5.1 Basic NER

```python
from transformers import pipeline

# Load NER pipeline
ner = pipeline("ner", grouped_entities=True)

text = "Apple Inc. was founded by Steve Jobs in Cupertino, California. The company is worth $2 trillion."

# Extract entities
entities = ner(text)

print("Named Entities Found:")
print("-" * 50)
for entity in entities:
    print(f"  {entity['word']}: {entity['entity_group']} ({entity['score']:.2%})")

# Output:
# Apple Inc.: ORG (99.85%)
# Steve Jobs: PER (99.91%)
# Cupertino: LOC (99.72%)
# California: LOC (99.88%)
```

### 5.2 Extract Specific Entities

```python
from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)

def extract_entities_by_type(text, entity_type):
    """Extract specific entity types"""
    entities = ner(text)
    return [e['word'] for e in entities if e['entity_group'] == entity_type]

text = """
Elon Musk is the CEO of Tesla and SpaceX.
He was born in Pretoria, South Africa in 1971.
Tesla is headquartered in Austin, Texas.
"""

print("People:", extract_entities_by_type(text, 'PER'))
print("Organizations:", extract_entities_by_type(text, 'ORG'))
print("Locations:", extract_entities_by_type(text, 'LOC'))

# Output:
# People: ['Elon Musk']
# Organizations: ['Tesla', 'SpaceX', 'Tesla']
# Locations: ['Pretoria', 'South Africa', 'Austin', 'Texas']
```

---

## 6. Question Answering

### 6.1 Extractive QA

```python
from transformers import pipeline

# Load QA pipeline
qa = pipeline("question-answering")

# Context (the text containing the answer)
context = """
Python is a high-level programming language created by Guido van Rossum
and first released in 1991. Python's design philosophy emphasizes code
readability with its notable use of significant whitespace. It is
dynamically typed and garbage-collected. Python supports multiple
programming paradigms, including structured, object-oriented, and
functional programming.
"""

# Ask questions
questions = [
    "Who created Python?",
    "When was Python released?",
    "What does Python emphasize?",
]

print("Question Answering:")
print("=" * 60)
for question in questions:
    result = qa(question=question, context=context)
    print(f"Q: {question}")
    print(f"A: {result['answer']} (confidence: {result['score']:.2%})")
    print()

# Output:
# Q: Who created Python?
# A: Guido van Rossum (confidence: 97.45%)
#
# Q: When was Python released?
# A: 1991 (confidence: 95.23%)
```

### 6.2 QA with Your Own Documents

```python
from transformers import pipeline

qa = pipeline("question-answering")

def answer_from_document(document, question):
    """Answer a question based on a document"""
    result = qa(question=question, context=document)

    return {
        'answer': result['answer'],
        'confidence': result['score'],
        'start': result['start'],
        'end': result['end']
    }

# Your document
document = """
The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars
in Paris, France. It is named after the engineer Gustave Eiffel, whose
company designed and built the tower. Constructed from 1887 to 1889,
it was initially criticized by some of France's leading artists and
intellectuals. The tower is 330 metres tall and was the tallest
man-made structure in the world for 41 years until the Chrysler Building
in New York City was finished in 1930.
"""

# Interactive questioning
questions = [
    "Where is the Eiffel Tower located?",
    "Who designed the Eiffel Tower?",
    "How tall is the Eiffel Tower?",
    "When was it built?"
]

for q in questions:
    result = answer_from_document(document, q)
    print(f"Q: {q}")
    print(f"A: {result['answer']} ({result['confidence']:.1%})")
    print()
```

---

## 7. Text Generation

### 7.1 Basic Text Generation

```python
from transformers import pipeline

# Load text generator
generator = pipeline("text-generation", model="gpt2")

# Generate text
prompt = "Artificial intelligence is"
result = generator(prompt, max_length=50, num_return_sequences=1)

print(f"Prompt: {prompt}")
print(f"Generated: {result[0]['generated_text']}")
```

### 7.2 Control Generation

```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "The future of technology will"

# Generate multiple variations
results = generator(
    prompt,
    max_length=100,           # Maximum tokens
    num_return_sequences=3,   # Number of variations
    temperature=0.7,          # Creativity (0.1=safe, 1.0=creative)
    do_sample=True,           # Enable sampling
    top_k=50,                 # Consider top 50 tokens
    top_p=0.95,               # Nucleus sampling
)

print("Generated Texts:")
print("=" * 60)
for i, result in enumerate(results, 1):
    print(f"\n{i}. {result['generated_text']}")
```

### 7.3 Story Generation

```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2-medium")

def generate_story(start, length=200):
    """Generate a story from a starting sentence"""
    result = generator(
        start,
        max_length=length,
        num_return_sequences=1,
        temperature=0.8,
        do_sample=True,
        pad_token_id=50256  # GPT2's end token
    )
    return result[0]['generated_text']

# Generate story
story_start = "Once upon a time in a magical forest, there lived a young dragon who"
story = generate_story(story_start)
print(story)
```

---

## 8. Summarization

### 8.1 Basic Summarization

```python
from transformers import pipeline

# Load summarizer
summarizer = pipeline("summarization")

# Long article
article = """
The Amazon rainforest, also known as Amazonia, is a moist broadleaf tropical
rainforest in the Amazon biome that covers most of the Amazon basin of South
America. This basin encompasses 7,000,000 km2 (2,700,000 sq mi), of which
5,500,000 km2 (2,100,000 sq mi) are covered by the rainforest. This region
includes territory belonging to nine nations and 3,344 formally acknowledged
indigenous territories. The majority of the forest is contained within Brazil,
with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and
with minor amounts in Bolivia, Ecuador, French Guiana, Guyana, Suriname, and
Venezuela. The Amazon represents over half of the planet's remaining rainforests,
and comprises the largest and most biodiverse tract of tropical rainforest in
the world, with an estimated 390 billion individual trees divided into 16,000
species. The Amazon rainforest is critical for regulating global climate,
storing carbon, and maintaining biodiversity.
"""

# Summarize
summary = summarizer(article, max_length=100, min_length=30, do_sample=False)

print("Original length:", len(article.split()))
print("Summary length:", len(summary[0]['summary_text'].split()))
print("\nSummary:")
print(summary[0]['summary_text'])
```

### 8.2 Control Summary Length

```python
from transformers import pipeline

summarizer = pipeline("summarization")

article = """[Your long article here]"""

# Short summary
short = summarizer(article, max_length=50, min_length=20)
print("Short:", short[0]['summary_text'])

# Medium summary
medium = summarizer(article, max_length=100, min_length=50)
print("Medium:", medium[0]['summary_text'])

# Long summary
long = summarizer(article, max_length=200, min_length=100)
print("Long:", long[0]['summary_text'])
```

---

## 9. Translation

### 9.1 Basic Translation

```python
from transformers import pipeline

# English to French
translator = pipeline("translation_en_to_fr")

text = "Hello, how are you? I hope you are having a great day!"
result = translator(text)

print(f"English: {text}")
print(f"French: {result[0]['translation_text']}")
```

### 9.2 Multiple Languages

```python
from transformers import pipeline

# Different translation pipelines
en_to_de = pipeline("translation_en_to_de")  # English to German
en_to_es = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")  # English to Spanish
en_to_zh = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")  # English to Chinese

text = "Machine learning is transforming the world."

print(f"English: {text}")
print(f"German: {en_to_de(text)[0]['translation_text']}")
print(f"Spanish: {en_to_es(text)[0]['translation_text']}")
print(f"Chinese: {en_to_zh(text)[0]['translation_text']}")
```

### 9.3 Multi-language Model

```python
from transformers import pipeline

# Use mBART for many languages
translator = pipeline("translation", model="facebook/mbart-large-50-many-to-many-mmt")

def translate(text, src_lang, tgt_lang):
    """Translate between many languages"""
    result = translator(text, src_lang=src_lang, tgt_lang=tgt_lang)
    return result[0]['translation_text']

# Examples
text = "Hello, world!"
print(f"English: {text}")
print(f"French: {translate(text, 'en_XX', 'fr_XX')}")
print(f"German: {translate(text, 'en_XX', 'de_DE')}")
print(f"Japanese: {translate(text, 'en_XX', 'ja_XX')}")
```

---

## 10. Zero-Shot Classification

### 10.1 What is Zero-Shot?

Zero-shot classification lets you classify text into categories **without any training data**!

```python
from transformers import pipeline

# Load zero-shot classifier
classifier = pipeline("zero-shot-classification")

# Text to classify
text = "I just bought a new laptop and it's amazing for gaming!"

# Define categories (no training needed!)
categories = ["technology", "sports", "politics", "entertainment", "food"]

# Classify
result = classifier(text, categories)

print(f"Text: {text}")
print(f"\nCategories (ranked by probability):")
for label, score in zip(result['labels'], result['scores']):
    print(f"  {label}: {score:.2%}")

# Output:
# technology: 75.23%
# entertainment: 15.45%
# sports: 5.12%
# ...
```

### 10.2 Multi-label Classification

```python
from transformers import pipeline

classifier = pipeline("zero-shot-classification")

text = "The new iPhone has an amazing camera and the stock price went up!"

categories = ["technology", "business", "photography", "entertainment"]

# Allow multiple labels
result = classifier(text, categories, multi_label=True)

print(f"Text: {text}")
print(f"\nRelevant categories:")
for label, score in zip(result['labels'], result['scores']):
    if score > 0.5:  # Threshold
        print(f"  {label}: {score:.2%}")
```

### 10.3 Custom Classification Tasks

```python
from transformers import pipeline

classifier = pipeline("zero-shot-classification")

# Email classification
email = "Dear customer, your order #12345 has been shipped and will arrive tomorrow."
email_categories = ["shipping update", "promotional", "account", "support request"]
print("Email:", classifier(email, email_categories)['labels'][0])

# Intent detection
query = "How do I reset my password?"
intents = ["password reset", "account deletion", "billing inquiry", "general question"]
print("Intent:", classifier(query, intents)['labels'][0])

# Topic detection
article = "The central bank raised interest rates by 0.25% to combat inflation."
topics = ["economy", "politics", "sports", "technology", "health"]
print("Topic:", classifier(article, topics)['labels'][0])
```

---

## 11. Image Classification

### 11.1 Basic Image Classification

```python
from transformers import pipeline
from PIL import Image

# Load image classifier
classifier = pipeline("image-classification")

# Load and classify image
image = Image.open("cat.jpg")
result = classifier(image)

print("Image Classification Results:")
for item in result[:5]:  # Top 5
    print(f"  {item['label']}: {item['score']:.2%}")
```

### 11.2 Classify from URL

```python
from transformers import pipeline

classifier = pipeline("image-classification")

# Classify from URL
url = "https://example.com/image.jpg"
result = classifier(url)

for item in result[:3]:
    print(f"{item['label']}: {item['score']:.2%}")
```

### 11.3 Object Detection

```python
from transformers import pipeline
from PIL import Image

# Load object detector
detector = pipeline("object-detection")

image = Image.open("street.jpg")
results = detector(image)

print("Objects detected:")
for obj in results:
    print(f"  {obj['label']}: {obj['score']:.2%} at {obj['box']}")
```

---

## 12. Using Specific Models

### 12.1 Load Model Directly

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load tokenizer and model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare input
text = "I really enjoyed this movie!"
inputs = tokenizer(text, return_tensors="pt")

# Get prediction
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

# Print results
labels = ['NEGATIVE', 'POSITIVE']
for label, prob in zip(labels, predictions[0]):
    print(f"{label}: {prob:.2%}")
```

### 12.2 Popular Model Choices

| Task | Model | Description |
|------|-------|-------------|
| Sentiment | `distilbert-base-uncased-finetuned-sst-2-english` | Fast, accurate |
| NER | `dslim/bert-base-NER` | Good entity recognition |
| QA | `deepset/roberta-base-squad2` | Robust QA |
| Generation | `gpt2`, `gpt2-medium`, `gpt2-large` | Text generation |
| Summarization | `facebook/bart-large-cnn` | News summarization |
| Translation | `Helsinki-NLP/opus-mt-en-*` | Many language pairs |

### 12.3 Fine-tuning (Advanced)

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments
from datasets import Dataset

# This is just an overview - fine-tuning needs proper setup

# 1. Prepare your data
train_data = {
    'text': ['I love this!', 'This is terrible', ...],
    'label': [1, 0, ...]
}
dataset = Dataset.from_dict(train_data)

# 2. Load pre-trained model
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2
)

# 3. Set up training
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16,
)

# 4. Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)
trainer.train()

# 5. Save
model.save_pretrained("my_fine_tuned_model")
```

---

## 13. Quick Reference

### Common Pipelines

```python
from transformers import pipeline

# Text Tasks
sentiment = pipeline("sentiment-analysis")
ner = pipeline("ner")
qa = pipeline("question-answering")
generator = pipeline("text-generation")
summarizer = pipeline("summarization")
translator = pipeline("translation_en_to_fr")
classifier = pipeline("zero-shot-classification")
fill = pipeline("fill-mask")

# Vision Tasks
img_classifier = pipeline("image-classification")
obj_detector = pipeline("object-detection")

# Audio Tasks
speech = pipeline("automatic-speech-recognition")
```

### Pipeline Parameters

```python
# Common parameters
pipeline(
    task="sentiment-analysis",
    model="specific-model-name",  # Optional
    device=0,                      # GPU index (-1 for CPU)
)

# Generation parameters
generator(
    text,
    max_length=100,
    min_length=20,
    num_return_sequences=3,
    temperature=0.7,
    do_sample=True,
)
```

### Model Selection Guide

| Task | Recommended Model |
|------|-------------------|
| Quick sentiment | `pipeline("sentiment-analysis")` |
| Multilingual sentiment | `nlptown/bert-base-multilingual-uncased-sentiment` |
| Fast NER | `dslim/bert-base-NER` |
| QA | `deepset/roberta-base-squad2` |
| Text generation | `gpt2` or `gpt2-medium` |
| Summarization | `facebook/bart-large-cnn` |
| Translation | `Helsinki-NLP/opus-mt-*` |

### Common Imports

```python
# Pipelines (easiest)
from transformers import pipeline

# Direct model usage
from transformers import AutoTokenizer, AutoModel
from transformers import AutoModelForSequenceClassification
from transformers import AutoModelForQuestionAnswering
from transformers import AutoModelForCausalLM

# Training
from transformers import Trainer, TrainingArguments
```

### Tips

```python
# 1. First run downloads models (can be large!)
# Models cached in ~/.cache/huggingface/

# 2. Use GPU if available
pipeline("task", device=0)  # Use GPU 0

# 3. Batch processing for speed
results = pipeline(["text1", "text2", "text3"])

# 4. Check available models at
# https://huggingface.co/models
```

---

## Summary

Hugging Face Transformers makes state-of-the-art AI accessible:

1. **Pipelines** - One-line model loading
2. **Sentiment** - `pipeline("sentiment-analysis")`
3. **NER** - `pipeline("ner")`
4. **QA** - `pipeline("question-answering")`
5. **Generation** - `pipeline("text-generation")`
6. **Summarization** - `pipeline("summarization")`
7. **Translation** - `pipeline("translation_xx_to_yy")`
8. **Zero-shot** - Classify without training data

Start with pipelines, then explore specific models as needed!
