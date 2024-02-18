# doctext

Extract text from all kinds of documents.
Delegates the heavylifting to other libraries and tools like [Apache Tika](https://tika.apache.org/), [tesseract](https://github.com/tesseract-ocr/tesseract) and many more.

## Usage
    
 ```python
#!/usr/bin/env python
from doctext.Processor import Processor
import logging

# set logging level to INFO to see what's going on
logging.basicConfig(level=logging.INFO)

p = Processor()
print(p.run('/Users/me/some.pptx'))

# specify the language for tesseract
p = Processor()
print(p.run('/Users/me/some-german.png', tesseract_lang='deu'))

# or with Whisper (see https://openai.com/pricing)
p = Processor(openai_api_key='your-openai-api-key')
print(p.run('/Users/me/some.m4a'))
```

## Introduction

Why yet another library for extracting text from documents?
Because [textract](https://github.com/deanmalmgren/textract) seems to be more or less abandoned and requires some outdated versions of dependencies. Also it does not support all the file formats I need. [Apache Tika](https://tika.apache.org/) is great but surprisingly did not support some of the file formats I needed. So I decided to write a wrapper around a [wrapper](https://github.com/chrismattmann/tika-python).

## Installation

```bash
pip install doctext
```

```bash
brew install ffmpeg imagemagick poppler libheif dcraw
```