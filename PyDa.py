import wolframalpha
import wikipedia

while(True):
    inp = input("Question: ")
    try:
        #wolframalpha
        app_id = "XJ3PJW-WJHQH7UTQG"
        client = wolframalpha.Client(app_id)
        res = client.query(inp)
        answer = next(res.results).text
        print (answer)
    except:
        #wikipedia
        try:
            print(wikipedia.summary(inp))
        except:
            print("Could not find anything related, Sorry, i am not that powerful.")
