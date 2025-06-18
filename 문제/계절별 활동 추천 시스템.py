t = int(input())
s = input()

def suggest(temperature, season):
    if season == "summer":
        if temperature >= 30:
            return "Swimming"
        else:
            return "Trekking"
    elif season == "winter":
        if temperature <= 0:
            return "Skiing"
        else:
            return "Winter walk"
    else:
        if temperature >= 20:
            return "Biking"
        else:
            return "Visit the library"

print(suggest(t, s))