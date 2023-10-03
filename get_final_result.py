from transformers import RobertaForSequenceClassification
from transformers import RobertaTokenizer
from torch.utils.data import TensorDataset, DataLoader
import numpy as np
import unicodedata as ud

def get_final_result(text):
    tokenizer = RobertaTokenizer.from_pretrained("roberta-large")
    classifier = RobertaForSequenceClassification.from_pretrained('timoneda/detect_it', num_labels=2)
    classifier.eval()
    label_dict = {0: "Student", 1: "ChatGPT"}
    text = ud.normalize("NFKD", text)
    text = text.strip()
    text = text.replace("\n", ". ")
    text = text.replace("\t", "")
    text = text.replace("  ", "")
    text = tokenizer.encode_plus(text, 
                                     return_tensors='pt', 
                                     max_length=512, 
                                     truncation=True)
    outputs = classifier(text["input_ids"],
                    attention_mask=text["attention_mask"])
    outputs = outputs[0].detach().numpy()
    predicted_label = np.argmax(outputs)
    label = label_dict[predicted_label]
    return predicted_label, label

