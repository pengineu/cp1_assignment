def phonetic(value: str) -> str:
    alphabet = {"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo",
                "F":"Foxstrot","G":"Golf","H":"Hotel","I":"India","J":"Juliet",
                "K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar",
                "P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango",
                "U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray","Y":"Yankee","Z":"Zulu" }
    li = []
    for i in value:
        li.append(alphabet[i])
    result = ' '.join(li)
    return result

print(phonetic('GETIT'))