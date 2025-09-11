print("Welcome to Manga Reader of Temperature!")
print("Answer a few questions to get started!\n")

genre = input("What genre are you? (action, romance, horror): ").lower()
duration = input("How long should a manga volume be? (long, medium, short): ").lower()
time = input("Which decade? (2000s, 2010s): ").lower()

print("\nThe available mangas are:")


if genre == "action":
    if duration == "long":
        if time in ("2000s", "2000"):
            print("- Naruto")
        elif time in ("2010s", "2010"):
            print("- Attack on Titan")
    elif duration == "medium":
        if time in ("2000s", "2000"):
            print("- Fullmetal Alchemist")
        elif time in ("2010s", "2010"):
            print("- My Hero Academia")
    elif duration == "short":
        if time in ("2000s", "2000"):
            print("- Gantz")
        elif time in ("2010s", "2010"):
            print("- One Punch Man")


elif genre == "romance":
    if duration == "long":
        if time in ("2000s", "2000"):
            print("- Boys Over Flowers")
        elif time in ("2010s", "2010"):
            print("- Ao Haru Ride")
    elif duration == "medium":
        if time in ("2000s", "2000"):
            print("- Lovely★Complex")
        elif time in ("2010s", "2010"):
            print("- Kimi ni Todoke")
    elif duration == "short":
        if time in ("2000s", "2000"):
            print("- Paradise Kiss")
        elif time in ("2010s", "2010"):
            print("- Horimiya")

elif genre == "horror":
    if duration == "long":
        if time in ("2000s", "2000"):
            print("- Hellsing")
        elif time in ("2010s", "2010"):
            print("- Ajin")
    elif duration == "medium":
        if time in ("2000s", "2000"):
            print("- Goth")
        elif time in ("2010s", "2010"):
            print("- The Promised Neverland")
    elif duration == "short":
        if time in ("2000s", "2000"):
            print("- Uzumaki")
        elif time in ("2010s", "2010"):
            print("- I Am a Hero")

else:
    print("Sorry, no results found for your selection.")