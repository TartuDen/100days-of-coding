# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"},
# {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
# {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
# {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# {"text": "Google was originally called 'Backrub'.", "answer": "True"},
# {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"},
# {'text': '&quot;Typewriter&quot; is the longest word that can be typed using only the first row on a QWERTY keyboard.', 'answer': 'True'},
# {'text': 'Coca-Cola&#039;s original colour was green.', 'answer': 'False'},
# {'text': 'The sum of all the numbers on a roulette wheel is 666.', 'answer': 'True'},
# {'text': 'Furby was released in 1998.', 'answer': 'True'},
# {'text': 'There are 86400 seconds in a day.', 'answer': 'True'},
# {'text': 'An eggplant is a vegetable.', 'answer': 'False'},
# {'text': 'The bikini is named after the &quot;Bikini Atoll&quot;, an island where the United States conducted tests on atomic bombs.', 'answer': 'True'},
# {'text': 'Cucumbers are usually more than 90% water.', 'answer': 'True'},
# {'text': 'You are allowed to sell your soul on eBay.', 'answer': 'False'},
# {'text': 'The average woman is 5 inches \\/ 13 centimeters shorter than the average man.', 'answer': 'True'},
# {'text': 'The term &quot;Spam&quot; came before the food product &quot;Spam&quot;.', 'answer': 'False'},
# {'text': 'Sitting for more than three hours a day can cut two years off a person&#039;s life expectancy.', 'answer': 'True'},
# {'text': 'The French word to travel is &quot;Travail&quot;', 'answer': 'False'},
# {'text': 'Fast food restaurant chains Carl&#039;s Jr. and Hardee&#039;s are owned by the same company.', 'answer': 'True'},
# {'text': 'The scientific name for the Southern Lights is Aurora Australis?', 'answer': 'True'},
# {'text': 'Haggis is traditionally ate on Burns Night.', 'answer': 'True'},
# {'text': 'Francis Bacon died from a fatal case of pneumonia while he was attempting to preserve meat by stuffing a chicken with snow.', 'answer': 'True'},
# {'text': 'Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago.', 'answer': 'False'},
# {'text': 'The pickled gherkin was first added to hamburgers because a US health law required all fast-food to include a source of Vitamin C.', 'answer': 'False'},
# {'text': '&quot;Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.&quot; is a grammatically correct sentence.', 'answer': 'True'}
# ]


import requests

# Set up the API endpoint URL
url = "https://opentdb.com/api.php"

# Set up the parameters for the API request
amount_of_questions=10

params = {
    "amount": 10,       # number of questions to retrieve
    "category": 9,      # category ID (9 = General Knowledge)
    "difficulty": "easy",  # difficulty level (easy, medium, or hard)
    "type": "boolean"  # type of question (True/False)
}

# Send the API request and get the JSON response
response = requests.get(url, params=params).json()

# Print the JSON response
# x=(response)





# x={"response_code":0,"results":[{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"&quot;Typewriter&quot; is the longest word that can be typed using only the first row on a QWERTY keyboard.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Coca-Cola&#039;s original colour was green.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The sum of all the numbers on a roulette wheel is 666.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Furby was released in 1998.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"There are 86400 seconds in a day.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"An eggplant is a vegetable.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The bikini is named after the &quot;Bikini Atoll&quot;, an island where the United States conducted tests on atomic bombs.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Cucumbers are usually more than 90% water.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"You are allowed to sell your soul on eBay.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The average woman is 5 inches \/ 13 centimeters shorter than the average man.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The term &quot;Spam&quot; came before the food product &quot;Spam&quot;.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Sitting for more than three hours a day can cut two years off a person&#039;s life expectancy.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The French word to travel is &quot;Travail&quot;","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Fast food restaurant chains Carl&#039;s Jr. and Hardee&#039;s are owned by the same company.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The scientific name for the Southern Lights is Aurora Australis?","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Haggis is traditionally ate on Burns Night.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Francis Bacon died from a fatal case of pneumonia while he was attempting to preserve meat by stuffing a chicken with snow.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The pickled gherkin was first added to hamburgers because a US health law required all fast-food to include a source of Vitamin C.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"&quot;Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.&quot; is a grammatically correct sentence.","correct_answer":"True","incorrect_answers":["False"]}]}
question_data=[]
# print(x["results"][0])
# print(len(x["results"]))

for i in range(amount_of_questions):
    # print(x["results"][i]["question"])
    # print(x["results"][i]["correct_answer"])

    question_data.append({"text":response["results"][i]["question"],"answer":response["results"][i]["correct_answer"]})

# for k in y:
#     print(k)