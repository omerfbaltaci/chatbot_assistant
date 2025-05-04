from sentence_transformers import SentenceTransformer, util
from data import dataset as data

# After preparing the questions in my dataset as a list, I used the MiniLM-L12 model to vectorize this list and 
# compare it more consistently with user input. Also i saved these embeddings as a PyTorch tensor instead of Numpy
# array, that makes them much more useful for future.
model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
questions = list(data.keys())
question_embeddings = model.encode(questions, convert_to_tensor = True)

def chatbot(user_input):
    # I do the same vectorization process as above for the user input. Then I compare the vector versions of the 
    # user input with the questions in the dataset and save the similarity scores as a list in "similarities".
    input_embedding = model.encode(user_input, convert_to_tensor = True)
    similarities = util.pytorch_cos_sim(input_embedding, question_embeddings)[0]
    
    # Then, I save the index of the question with the highest similarity score in the data set as 
    # "best_guess_index" in the list, and this time I save only the similarity score of this question to the 
    # "best_score" variable.
    best_guess_index = similarities.argmax().item()
    best_score = similarities[best_guess_index].item()
    print(best_score) # The problem why the code not working is the embedding score is always too low.
                      #Don't know why. It's always something like "0.10627515614032745" etc.
    
    # Here, if the score of the question with the highest similarity score is higher than the specified value, 
    # the answer to this question is found from the dataset and printed on the screen. If the score is lower 
    # than the specified value, the specified sentence is printed on the screen.
    if best_score >= 0.4:
        supposed_question = question_embeddings[best_guess_index]
        return[supposed_question]
    else:
        return "Sorulan soruya dair uygun yanıt bulunamadı.\n"
    
# Test loop
while True:
    test_user_input = input("Sorunuzu yazınız (çıkmak için 'çık'): ")

    if test_user_input.lower() == 'çık':
        break

    print("Chatbot:", chatbot(test_user_input))
