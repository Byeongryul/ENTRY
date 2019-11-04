import json

diary = {
    'id' :3,
    'title' : 'my name is euiyeon',
    'body' : 'what is your name?',
}

print(diary)
print(type(diary))

diary_s= json.dumps(diary) # dumps : dictionary --> json

print(diary_s)
print(type(diary_s))

diary_back = json.loads(diary_s)

print(type(diary_back))