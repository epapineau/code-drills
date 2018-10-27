# we're going to be importing the shows dictionary from the show_data.py file, you can look into that file to view all the show data for this activity
from show_data import shows

# Hint: You may find that you're repeating yourself a lot. It may be helpful to create variables that point to different locations within the dictionary. 

    # For Example : drama = shows["genre"]["drama"]
    #Then to get the actor who plays Rick in Walking Dead, we would simply write drama["the_walking_dead"]["cast"][0]["actor"] as opposed to shows["genre"]["drama"]["the_walking_dead"]["cast"][0]["actor"]  

# ========================================= SHORTCUTS =========================================
drama = shows["genre"]["drama"]

#======================== QUESTION 1 ==========================
#QUESTION: Who is the actor that plays Squidward in Spongebob (kids)?
#ANSWER: 
print(shows["genre"]["kids"]["Spongebob"]["cast"][3]["actor"])
#==============================================================

#======================== QUESTION 2 ==========================
#QUESTION: Patrick Warburton plays Joe Swanson in Family Guy (comedy). What is the link to his imdb page?
#ANSWER: 
print(shows["genre"]["comedy"]["family_guy"]["cast"][4]["imdb"])
#==============================================================

#======================== QUESTION 3 ==========================
#QUESTION: Is the Walking Dead still running?
#ANSWER: 
print(shows["genre"]["drama"]["the_walking_dead"]["still_running"]) 
#==============================================================

#======================== QUESTION 4 ==========================
#QUESTION: Who plays Dexter in Dexter (drama) and who plays Dexter in Dexter's Lab (kids)?
#HINT: You can print multiple items at once by using a comma like this: print(thing1, thing2)
#ANSWER: 
print(shows["genre"]["drama"]["dexter"]["cast"][0]["actor"],
      shows["genre"]["kids"]["dexters_lab"]["cast"][0]["actor"]) 
#==============================================================

#======================== QUESTION 5 ==========================
#QUESTION: Who are the creators of Stranger Things (drama)?
#ANSWER: 
print(shows["genre"]["drama"]["stranger_things"]["creators"]) 
#==============================================================

#======================== QUESTION 6 ==========================
#QUESTION: Who hosts the Daily Show (talk)?
#ANSWER: 
print(shows["genre"]["talk"]["the_daily_show"]["host"]) 
#==============================================================

#======================== QUESTION 7 ==========================
#QUESTION: Who are all the hosts of the view (talk)
#Hint: You will need to use a loop for this one. You may not simply log the entire list, but must log each name individually
#ANSWER: 
for host in shows["genre"]["talk"]["the_view"]["host"]:
    print(host)

#==============================================================

#======================== QUESTION 8 ==========================
#QUESTION: What are the show names of the Impractical Jokers (comedy)
#Hint: You will need to use a loop for this one. You may not simply log the entire list, but must log each name individually
#ANSWER: 
for name in shows["genre"]["comedy"]["impractical_jokers"]["cast"]:
    print(name["showName"])
#==============================================================

#======================== QUESTION 9 ==========================
#QUESTION: Who does Will Arnett play in Arrested Development (comedy)
#ANSWER: 
print(shows["genre"]["comedy"]["arrested_development"]["cast"][2]["character"]) 
#==============================================================

#======================== QUESTION 10 ==========================
#QUESTION: Who plays Yami Yugi in Yu-Gi-Oh (kids)?
#ANSWER: 
print(shows["genre"]["kids"]["yu_gi_oh"]["cast"][0]["actor"]) 
#==============================================================

#======================== QUESTION 11 ==========================
#QUESTION: How many seasons did the Office (comedy) run?
#ANSWER: 
print(shows["genre"]["comedy"]["the_office"]["num_seasons"]) 
#==============================================================

#======================== QUESTION 12 ==========================
#QUESTION: Who are the main characters of the Office (comedy) (not the actors, but the actual character names)?
#ANSWER: 
for character in shows["genre"]["comedy"]["the_office"]["cast"]:
    print(character["character"])
#==============================================================

#======================== QUESTION 13 ==========================
#QUESTION: List the characters in Teen Titans (kids)
#ANSWER: 
for character in shows["genre"]["kids"]["teen_titans"]["cast"]:
    print(character["character"])
#==============================================================

#======================== QUESTION 14 ==========================
#QUESTION: What is the link to the IMDB page for the actor who plays Mr. Krabs (Spongebob, kids)?
#ANSWER: 
print(shows["genre"]["kids"]["Spongebob"]["cast"][0]["imdb"]) 
#==============================================================

#======================== QUESTION 15 ==========================
#QUESTION: Who plays Negan in The Walking Dead?
#ANSWER: 
print(shows["genre"]["drama"]["the_walking_dead"]["cast"][2]["actor"]) 
#==============================================================

#======================== QUESTION 16 ==========================
#QUESTION: List the main cast of Dexter (drama) (the actors, not the characters)
#ANSWER: 
for actor in shows["genre"]["drama"]["dexter"]["cast"]:
    print(actor["actor"])
#==============================================================

#======================== QUESTION 17 ==========================
#QUESTION: Is Game of Thrones(drama) still running?
#ANSWER: 
print(shows["genre"]["drama"]["game_of_thrones"]["still_running"]) 
#==============================================================

#======================== QUESTION 18 ==========================
#QUESTION: Who does Peter Dinklage play in Game of Thrones (drama)?
#ANSWER: 
print(shows["genre"]["drama"]["game_of_thrones"]["cast"][1]["character"]) 
#==============================================================

#======================== QUESTION 19 ==========================
#QUESTION: List the American Idol Judges
#ANSWER: 
for judge in shows["genre"]["reality"]["american_idol"]["judges"]:
    print(judge)
#==============================================================

#======================== QUESTION 20 ==========================
#QUESTION: Who plays Dustin in Stanger Things (drama)?
#ANSWER: 
print(shows["genre"]["drama"]["stranger_things"]["cast"][3]["actor"]) 
#==============================================================