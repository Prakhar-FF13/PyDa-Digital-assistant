import wolframalpha
import wikipedia
input = input("Question: ")
app_id = "XJ3PJW-WJHQH7UTQG"
client = wolframalpha.Client(app_id)
'''
res = client.query(input)
answer = next(res.results).text

print (answer)
'''

print(wikipedia.summary(input))
