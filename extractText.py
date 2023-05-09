from PyPDF2 import PdfReader
import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
import re

def clean_data(data):
  text = re.sub(r"\[[0-9]*\]"," ",data)
  text = text.lower()
  text = re.sub(r'\s+'," ",text)
  text = re.sub(r","," ",text)
  return text

# replace double-space with commas
def cleanup(text):
    text = text.replace("  ", ", ")
    text = text + ". \n"
    return text

async def extractSummary(file, num_sentences):
    reader = PdfReader(file)
    text = ''
    final_text = ''
    for i in range(len(reader.pages)): # iterate through pages
        text += reader.pages[i].extract_text()
    text = clean_data(text) # clean text
    parser = PlaintextParser.from_string(text,Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences) # replace with number of sentences wanted in summary
    for sentence in summary:
        sentence = cleanup(str(sentence))
        final_text += sentence
    return final_text  

