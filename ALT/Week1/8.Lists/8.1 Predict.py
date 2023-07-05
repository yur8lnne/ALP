'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
print(Sentence) #it will print ["Always", "look", "on", "the", "bright", "side", "of",]
print(Sentence[1]) #it will print look
Sentence.append("life") #it will add "sunny" to the Sentence list, so the list will change to ["Always", "look", "on", "the", "bright", "side", "of", "life"]
Sentence[4] = "sunny" #The fifth item "bright" will be changed into "sunny"
print(Sentence[4]) #it will print out sunny
print(Sentence[0] + " " + Sentence[3]) #it will print Always the
print(Sentence) #it will print ["Always", "look", "on", "the", "sunny", "side", "of", "life"]