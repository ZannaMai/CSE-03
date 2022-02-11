import random
class Word:

    def __init__(self):
        # defining self for the word list
        self._words = ['wares','soup','mount','extend','brown',
                       'expert','tired','humidity','backpack','crust',
                       'dent','market','knock','smite','windy','coin','throw',
                       'silence','bluff','downfall','climb','lying','weaver',
                       'snob','kickoff','match','quaker','foreman','excite',
                       'thinking','mend','allergen','pruning','coat',
                       'emerald','coherent','manic','multiple','square',
                       'funded','funnel','sailing','dream','mutation',
                       'dinner','rabbit','chill','seed','born','shampoo','italian',
                       'cable','oily','official','abyss','schism','failing','guru',
                       'trim','alfalfa',
        ]
        return self

    def get_word(self):
        word = random.choice(self._words)
        return word.upper()
