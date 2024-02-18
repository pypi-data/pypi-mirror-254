import stanza

nlp = stanza.Pipeline(lang='en', package="ewt",processors='tokenize', tokenize_no_ssplit=True)
data =[]

data.append(("dev",open("eng_dev_sents.tab",encoding="utf8").read()))
data.append(("test",open("eng_test_sents.tab",encoding="utf8").read()))
for partition, d in data:
    doc = nlp(d)
    toks = []
    for i, sentence in enumerate(doc.sentences):
        toks += [token.text for token in sentence.tokens]
    with open("eng_" + partition + "_stanza_ewt.tab",'w',encoding="utf8",newline="\n") as f:
        f.write("\n".join(toks).strip() + "\n")