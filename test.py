import textacy 
text = unicode('many language-processing tasks typically involved the direct hand coding')
#print(text)
#print(textacy.text_utils.KWIC(text, "revolution", window_width=2))
doc = textacy.make_spacy_doc(text)
print(textacy.extract.subject_verb_object_triples(doc))