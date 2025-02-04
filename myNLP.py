import scispacy
import spacy
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import re 

# Load a SciSpaCy model for better NER
nlp = spacy.load('en_core_web_tr')  # Use a specialized medical NER model

# Load a specialized BERT model (e.g., BioBERT, ClinicalBERT)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')  # Or any specialized model
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')  # Or any specialized model

classifier = pipeline('text-classification', model=model, tokenizer=tokenizer)

def extract_symptoms(text):
    doc = nlp(text)
    symptoms = []
    for ent in doc.ents:
        # Check for symptoms or disease-related labels
        if ent.label_ in ["SYMPTOM", "DISEASE"]:
            symptoms.append(ent.text)
    return symptoms

def classify_severity(text):
    result = classifier(text)
    return result[0]['label']  # Could return 'MILD', 'SEVERE', etc.

def extract_duration(text):
    duration_pattern = r"(\d+)\s*(hours?|days?|weeks?|months?)"  # Added weeks and months
    matches = re.findall(duration_pattern, text)
    if matches:
        return matches  # Return all matched durations
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

# Get user input and track symptoms
user_input = input("Enter symptoms: ")
output = track_symptoms(user_input)

print("Extracted Symptom Data:")
print(output)
