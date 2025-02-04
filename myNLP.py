import spacy
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import torch
import re 

nlp = spacy.load('en_core_web_sm')


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')


classifier = pipeline('text-classification', model=model, tokenizer=tokenizer)


user_input = input("Enter symptoms: ")


def extract_symptoms(text):
    doc = nlp(text)
    symptoms = []
    for ent in doc.ents:
        
        if ent.label_ in ["SYMPTOM"]: 
            symptoms.append(ent.text)
    return symptoms


def classify_severity(text):
    
    result = classifier(text)
    return result[0]['label']  


def extract_duration(text):
    
    duration_pattern = r"(\d+)\s*(hours?|days?)"
    match = re.search(duration_pattern, text)
    if match:
        
        return match.group(0)
    return None  


def track_symptoms(user_input):
    symptoms = extract_symptoms(user_input)
    
   
    severity = classify_severity(user_input)
    
   
    duration = extract_duration(user_input)

   
    symptom_data = {
        "symptoms": symptoms,
        "severity": severity,
        "duration": duration,
    }

    return symptom_data


output = track_symptoms(user_input)


print("Extracted Symptom Data:")
print(output)
