import nltk
from nltk.corpus import wordnet as wn
import spacy

nltk.download("wordnet")
nltk.download("omw-1.4")

nlp = spacy.load("en_core_web_sm")

def get_word_data(word: str):
    synsets = wn.synsets(word)

    if not synsets:
        return {
            "word": word,
            "meaning": "Meaning not found",
            "pos": "",
            "synonyms": [],
            "antonyms": [],
            "examples": [],
            "pronunciation": ""
        }

    syn = synsets[0]

    synonyms = list(set(
        l.name().replace("_", " ")
        for s in synsets for l in s.lemmas()
    ))[:6]

    antonyms = list(set(
        a.name().replace("_", " ")
        for s in synsets for l in s.lemmas()
        for a in l.antonyms()
    ))[:6]

    return {
        "word": word,
        "meaning": syn.definition(),
        "pos": nlp(word)[0].pos_,
        "synonyms": synonyms,
        "antonyms": antonyms,
        "examples": syn.examples(),
        "pronunciation":
            f"https://api.dictionaryapi.dev/media/pronunciations/en/{word}-us.mp3"
    }
