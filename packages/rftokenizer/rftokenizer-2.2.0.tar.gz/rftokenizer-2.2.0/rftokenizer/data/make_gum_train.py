from glob import glob
import os
import re
from collections import defaultdict

ud_dev = ["GUM_interview_cyclone", "GUM_interview_gaming",
          "GUM_news_iodine", "GUM_news_homeopathic",
          "GUM_voyage_athens", "GUM_voyage_coron",
          "GUM_whow_joke", "GUM_whow_overalls",
          "GUM_bio_byron", "GUM_bio_emperor",
          "GUM_fiction_lunre", "GUM_fiction_beast",
          "GUM_academic_exposure", "GUM_academic_librarians",
          "GUM_reddit_macroeconomics", "GUM_reddit_pandas",
          "GUM_speech_impeachment", "GUM_textbook_labor",
          "GUM_vlog_radiology", "GUM_conversation_grounded",
          "GUM_textbook_governments", "GUM_vlog_portland",
          "GUM_conversation_risk", "GUM_speech_inauguration"]
ud_test = ["GUM_interview_libertarian", "GUM_interview_hill",
           "GUM_news_nasa", "GUM_news_sensitive",
           "GUM_voyage_oakland", "GUM_voyage_vavau",
           "GUM_whow_mice", "GUM_whow_cactus",
           "GUM_fiction_falling", "GUM_fiction_teeth",
           "GUM_bio_jespersen", "GUM_bio_dvorak",
           "GUM_academic_eegimaa", "GUM_academic_discrimination",
           "GUM_reddit_escape", "GUM_reddit_monsters",
           "GUM_speech_austria", "GUM_textbook_chemistry",
           "GUM_vlog_studying", "GUM_conversation_retirement",
           "GUM_textbook_union", "GUM_vlog_london",
           "GUM_conversation_lambada", "GUM_speech_newzealand"]

files = glob("C:\\Uni\\Corpora\\GUM\\github\\_build\\target\\dep\\not-to-release\\*.conllu")

output = defaultdict(list)
sents = defaultdict(list)
chars = defaultdict(int)

for file_ in files:
    lines = open(file_,encoding="utf8").read().split("\n")

    docname = os.path.basename(file_).replace(".conllu","")
    partition="train"
    if docname in ud_test:
        partition="test"
    elif docname in ud_dev:
        partition="dev"

    seg = []
    mwt = 0
    for line in lines:
        if "Gonna" in line:
            a=3
        if "SpaceA" in line:
            a=4
        if "\t" in line:
            fields = line.split("\t")
            if "." in fields[0]:
                continue
            if "-" in fields[0]:
                ids = fields[0].split("-")
                mwt = int(ids[1]) - int(ids[0])
                if "SpaceAfter=No" in line:
                    mwt += 1
                continue
            seg.append(fields[1])
            for c in fields[1]:
                chars[c] +=1
            if "SpaceAfter=No" in line:
                mwt += 1
            if mwt == 0:
                output[partition].append("".join(seg) + "\t" + "|".join(seg))
                seg = []
            if mwt > 0:
                mwt -= 1
        elif line.startswith("# text"):
            _, s = line.split("=",maxsplit=1)
            sents[partition].append(s.strip())

for partition in output:
    with open("eng_"+partition + ".tab",'w',encoding="utf8",newline="\n") as f:
        f.write("\n".join(output[partition]).strip()+"\n")
    with open("eng_"+partition + "_plain.tab",'w',encoding="utf8",newline="\n") as f:
        f.write("\n".join([re.sub(r'\t[^\n]+','',l) for l in output[partition]]).strip()+"\n")
    with open("eng_"+partition + "_sents.tab",'w',encoding="utf8",newline="\n") as f:
        f.write("\n".join(sents[partition]).strip()+"\n")

for c in sorted(chars.keys(),key=lambda x: chars[x],reverse=True):
    print(c + "\t" + str(chars[c]))


output =[]
with open("eng_big.frq",encoding="utf8") as f:
    for line in f.readlines():
        line = line.strip()
        if line[-2:] in ["\t1","\t2","\t3","\t4"]:
            continue
        output.append(line)

with open("eng.frq",'w',encoding="utf8",newline="\n") as f:
    f.write("\n".join(output).strip()+"\n")
