# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
    'Dire Straits' : ['Brothers in Arms', 'Telegraph Road'], 
    'Yuka Kitamura' : ['Soul of Cinder', 'DS3'],
    'Jan Hammer' : ["Crockett's Theme"]
}

# Pretty-print the data structure
pprint(music)
# Display details of one album recorded by a specific artist
pprint(music['Dire Straits'])
#Experiment
i=0
while i < 3:
     pprint(list(music.values())[i])
     i+=1
print(min(music),max(music))