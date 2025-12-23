import pdfplumber


def extract_text_from_pdf(file):
    text=""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text+=page.extract_text()+"\n"
    return text


def chunck_text(text,max_words=600):
    words= text.split()
    chuncks=[]

    for i in range(0,len(words),max_words):
        chuncks.append(" ".join(words[i:i+max_words]))

    return chuncks;    