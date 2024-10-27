from sentence_transformers import SentenceTransformer
import faiss
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
import torch

sentence_embedding_model = SentenceTransformer(
    'C:/Users/Dell/Documents/ML Project/Realm of Answers GOT Q&A Bot/models/sentence_embedding_model'
)
index = faiss.read_index('C:/Users/Dell/Documents/ML Project/Realm of Answers GOT Q&A Bot/models/faiss_index_file.index')
QA_model = BertForQuestionAnswering.from_pretrained('C:/Users/Dell/Documents/ML Project/Realm of Answers GOT Q&A Bot/models/Q&A_model')
QA_tokenizer = BertTokenizer.from_pretrained('C:/Users/Dell/Documents/ML Project/Realm of Answers GOT Q&A Bot/models/Q&A_tokenizer')


def content_gen(query):
    query_vector = sentence_embedding_model.encode([query])
    _, I = index.search(query_vector, k=4)
    paragraph = " ".join([doc_texts[i] for i in I[0]])
    return paragraph

with open("C:/Users/Dell/Documents/ML Project/Realm of Answers GOT Q&A Bot/data/doc_texts.txt", "r") as f:
    doc_texts = [line.strip() for line in f]

def generate_answer(query, paragraph):
    encoding = QA_tokenizer.encode_plus(text=query,text_pair=paragraph)
    inputs = encoding['input_ids'] 
    sentence_embedding = encoding['token_type_ids']  
    tokens = QA_tokenizer.convert_ids_to_tokens(inputs) 
    start_scores = QA_model(input_ids=torch.tensor([inputs]), token_type_ids=torch.tensor([sentence_embedding]))['start_logits']
    end_scores = QA_model(input_ids=torch.tensor([inputs]), token_type_ids=torch.tensor([sentence_embedding]))['end_logits']
    start_index = torch.argmax(start_scores)
    end_index = torch.argmax(end_scores)
    answer = ' '.join(tokens[start_index:end_index+1])
    return answer

def define_query(query):
    content = content_gen(query)
    answer = generate_answer(query, content)
    return answer

query = input("What do you want to know? \n")
print("The answer is :", define_query(query))