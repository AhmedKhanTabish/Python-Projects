from transformers import AutoTokenizer, AutoModelForQuestionAnswering, Trainer, TrainingArguments, DefaultDataCollator 
import torch
from datasets import Dataset
from evaluate import load as load_metric
from tqdm import tqdm
import os
import PyPDF2
from docx import Document
import nltk

# Download the punkt tokenizer
nltk.download('punkt')

# Load the model and tokenizer
model_name = "distilbert-base-uncased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Function to extract text from PDF files
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to extract text from DOC files
def extract_text_from_doc(doc_path):
    doc = Document(doc_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

# Function to create training examples
def create_training_examples(text):
    chunk_size = 512
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    examples = []
    for chunk in chunks:
        sentences = nltk.sent_tokenize(chunk)
        for i in range(len(sentences) - 1):
            question = sentences[i]
            answer = sentences[i+1]
            examples.append({"question": question, "answer": answer})
    return examples

# Folder and file paths
folder_path = "G:/Rosenheim/Studies/Programming/Python/Doc Search Project"
output_file_path = "combined_text.txt"

# Extract text from PDF and DOC files and write to combined_text.txt
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
            output_file.write(text + '\n')
        elif filename.endswith('.doc'):
            text = extract_text_from_doc(file_path)
            output_file.write(text + '\n')

# Load the combined text
with open(output_file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Create training examples
train_examples = create_training_examples(text)

# Create the dataset
train_dataset = Dataset.from_dict({"question": [e["question"] for e in train_examples], "answers": [e["answer"] for e in train_examples]})

# Tokenize the dataset
def preprocess_function(examples):
    questions = [q.strip() for q in examples["question"]]
    answers = [a.strip() for a in examples["answers"]]
    tokenized_examples = tokenizer(questions, answers, truncation=True, padding="max_length", max_length=384)
    return tokenized_examples

tokenized_datasets = train_dataset.map(preprocess_function, batched=True)

# Data collator that will dynamically pad inputs for the batch
data_collator = DefaultDataCollator()

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",          # output directory
    evaluation_strategy="epoch",     # evaluate every epoch
    learning_rate=2e-5,              # learning rate
    per_device_train_batch_size=16,  # batch size for training
    per_device_eval_batch_size=16,   # batch size for evaluation
    num_train_epochs=3,              # total number of training epochs
    weight_decay=0.01,               # strength of weight decay
    logging_dir="./logs",            # directory for storing logs
    logging_steps=10,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,   # use the tokenized dataset
    eval_dataset=tokenized_datasets,    # optionally, same as train for simplicity
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# Start training
trainer.train()

# Save the fine-tuned model and tokenizer
model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")
