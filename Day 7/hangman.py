import random

"""
while lives_remaining >0 OR guesses_correctly != True:

"""

def choose_word():
    #returns a random word from a list
    word_library = ["The Shawshank Redemption","The Godfather","The Godfather: Part II","Pulp Fiction","Inception","Schindler's List","Angry Men","One Flew Over the Cuckoo's Nest","The Dark Knight","Star Wars: Episode V - The Empire Strikes Back","The Lord of the Rings: The Return of the King","Star Wars","Goodfellas","Casablanca","Fight Club","Cidade de Deus","The Lord of the Rings: The Fellowship of the Ring","Rear Window","Raiders of the Lost Ark","Toy Story 3","Psycho","The Usual Suspects","The Matrix","The Silence of the Lambs","Se7en","Memento","It's a Wonderful Life","The Lord of the Rings: The Two Towers","Sunset Blvd.","Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb","Forrest Gump","Citizen Kane","Apocalypse Now","North by Northwest","American Beauty","American History X","Taxi Driver","Terminator 2: Judgment Day","Saving Private Ryan","Vertigo","Alien","Lawrence of Arabia","The Shining","Paths of Glory","A Clockwork Orange","Double Indemnity","To Kill a Mockingbird","The Pianist","Das Leben der Anderen","The Departed","M","City Lights","Aliens","Eternal Sunshine of the Spotless Mind","Requiem for a Dream","Das Boot","The Third Man","L.A. Confidential","Reservoir Dogs","Chinatown","The Treasure of the Sierra Madre","Modern Times","Monty Python and the Holy Grail","Back to the Future","The Prestige","Raging Bull","Singing in the Rain","Some Like It Hot","The Bridge on the River Kwai","All About Eve","Amadeus","Once Upon a Time in America","The Green Mile","Full Metal Jacket","Inglourious Basterds","A Space Odyssey","The Great Dictator","Braveheart","The Apartment","Up","Gran Torino","Metropolis","The Sting","Gladiator","The Maltese Falcon","Unforgiven","Sin City","The Elephant Man","Mr. Smith Goes to Washington","On the Waterfront","Indiana Jones and the Last Crusade","Star Wars: Episode VI - Return of the Jedi","Rebecca","The Great Escape","Die Hard","Batman Begins","Jaws","Hotel Rwanda","Slumdog Millionaire","Blade Runner","Fargo","No Country for Old Men","Heat","The General","The Wizard of Oz","Touch of Evil","Ran","District 9","The Sixth Sense","Snatch.","Donnie Darko","Annie Hall","Witness for the Prosecution","The Deer Hunter","Avatar","The Social Network","Cool Hand Luke","Strangers on a Train","High Noon","The Big Lebowski","Hotaru no haka","Kill Bill: Vol. 1","It Happened One Night","Platoon","The Lion King","Into the Wild","There Will Be Blood","Notorious","Million Dollar Baby","Toy Story","Butch Cassidy and the Sundance Kid","Gone with the Wind","Sunrise: A Song of Two Humans","The Wrestler","The Manchurian Candidate","Trainspotting","Ben-Hur","Scarface","The Grapes of Wrath","The Graduate","The Big Sleep","Groundhog Day","Life of Brian","The Gold Rush","The Bourne Ultimatum","Finding Nemo","The Terminator","Stand by Me","How to Train Your Dragon","The Best Years of Our Lives","Lock, Stock and Two Smoking Barrels","The Thing","The Kid","V for Vendetta","Casino","Twelve Monkeys","Dog Day Afternoon","Ratatouille","Gandhi","Star Trek","The Princess Bride","The Night of the Hunter","Judgment at Nuremberg","The Incredibles","Tonari no Totoro","The Hustler","Good Will Hunting","The Killing","In Bruges","The Wild Bunch","Network","A Streetcar Named Desire","The Exorcist","Children of Men","Stalag 17","Persona","Who's Afraid of Virginia Woolf?","Ed Wood","Dial M for Murder","All Quiet on the Western Front","Big Fish","Magnolia","Rocky","La passion de Jeanne d'Arc","Kind Hearts and Coronets","Fanny och Alexander","Mystic River","Manhattan","Barry Lyndon","Kill Bill: Vol. 2","Mary and Max","Patton","Rosemary's Baby","Duck Soup","Festen","Kick-Ass","Letters from Iwo Jima","Roman Holiday","Pirates of the Caribbean: The Curse of the Black Pearl","The Truman Show","Crash","His Girl Friday","Arsenic and Old Lace","Harvey","The Philadelphia Story","A Christmas Story","Sleuth","King Kong","Rope","Monsters, Inc.","Mulholland Dr."]
    random_word = random.choice(word_library)
    print(random_word)
    return random_word

random_word = choose_word()

#generate as many blank spaces as letters in the word
blanks = 0
for i in random_word:
    blanks +=1

#for range(blanks, -1):
#
#     print(_)

#guess letter
guess = input("Guess a letter:> ")
if guess in random_word:
    pass
    #show letter in blank space
else:
    pass
    #minus a life
    #show as incorrect guess


lives_remaining = (len(random_word))
print(f"Lives remaining: {lives_remaining}")