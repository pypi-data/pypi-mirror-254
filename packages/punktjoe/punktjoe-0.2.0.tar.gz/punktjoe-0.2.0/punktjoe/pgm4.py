def print_prog():
    print(
        """
import spacy 


nlp=spacy.load("en_core_web_sm")
Text="I am a Fan of Mahendra Singh Dhoni  The "
#sentence tokeni
doc=nlp(Text)

print(doc)
#sent token

sents=list(doc.sents)

print(sents)

#word token
word1=[]
for word in Text.split():
  word1.append(word)
print(word1)

#is_stop
word2=[]
for token in doc:
  if not token.is_stop :
   word2.append(token.text)
print(word2)

#is_punt
word3=[]
for token in doc:
  if not token.is_punct:
    word3.append(token.text)
print(word3)

#pos
word4=[]
for token in doc:
  word4.append((token.text,token.pos_))
print(word4)

#lemma
word5=[]
for token in doc:
  word5.append((token.text,token.lemma_))
print(word5)
"""
    )
