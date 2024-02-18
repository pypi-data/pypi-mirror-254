=====================
TypedCoalitionalGame
=====================

Introduction
-------------
A TypedCoalitionalGame represents a coalitional game where the players are grouped into "types". The
value of a coalition depends only on the number of players of each type, individual players of a type are
considered indistinguishable. This allows calculating certain values for large coalitions where the calculation
would not be feasible using brute force methods.

Constructor
------------
TypedCoalitionalGame object takes as parameters a player_types dictionary, a coalition_valuation function,
and optionally an isCost boolean indicating the game is a cost game (defaults to False).
The player_types dictionary takes as key the label for the type, and as value the number of players of that type.
The coalition_valuation function takes a player_counts dictionary as an argument and returns the value of the
corresponding coalition::

        def un_security_old(player_counts):
            """According to "old" security council rules for a ruling to pass it needs supprt of all
               5 permanent 'P' members and 2 temporary '2' Members.
               Argument pass to fun will look like (('P', 4), ('T':2))"""
            perms = 0
            temps = 0
            for elm in player_counts:
                if elm[0] == 'P':
                    perms = elm[1]
                elif elm[0] == 'T':
                    temps = elm[1]
            if perms >= 5 and temps >= 2:
                return 1
            return 0

        tg_un = TypedCoalitionalGame(player_types = {'T':6, 'P':5}, coalition_valuation=un_security_old)
        print('un security old shapeley', tg_un.get_shapley_values())
        print('un security old banzhaf', tg_un.get_banzhaf_values())




Methods
---------

def get_valuation(self):
~~~~~~~~~~~~~~~~~~~~~~~~
Return the valuation function as a dictionary.

get_is_additive(self)
~~~~~~~~~~~~~~~~~~~~~~
Returns a boolean.


get_is_simple(self)
~~~~~~~~~~~~~~~~~~~~
Returns a boolean


get_banzhaf_values(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~
Returns a dict where the key is the player_type label and the value is the Banzhaf value for one player of
that type. The sums of all Banzhaf values of a type multiplied by the number of players of that type must be 1.


get_shapley_values(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~
Returns a dict where the key is the playeri_type label and the value is the Shapley value for one player of that type.

simulate_shapley_values(self, perms)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For large player sets it may not be feasible to calculate the Shapley values precisely, since this requires
checking the values of all subcoalitions. This method calculates an approximate Shapley value using a fixed number
of permutations.
Returns a dict where the key is the player_type label and the value is the Shapley value for one player of that type.

zero_normalize(self)
~~~~~~~~~~~~~~~~~~~~~
return a pair theGame, newgrand where game is the zero-normalized new game and newgrand is the value of the
grand coalition in the new game ( 1, 0 or -1).


is_equivaluent(self, game):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Check whether the the passed game is stratgeically equivalent to this game. returns a boolean.

get_is_monotonic(self)
~~~~~~~~~~~~~~~~~~~~~~~~
returns a boolean

get_is_superadditive(self)
~~~~~~~~~~~~~~~~~~~~~~~~~~
Returns a boolean



create_typed_voting_game(player_types, type_strengths, crit)
--------------------------------------------------------------

For a voting game, the colition is considered to be of value 1 if the sum of number of players of
players of a given type times the voting strength of the type is greater than or equal to some critical value.
Otherwise the value of the coalition is zero.
For this construction method, player_tiypes is a dictionary with key player_type and a value
which is the number of players of that type.
The type_strengths parameter is a dictionary with key being the player type and value the number of votes of
that type. Crit is the critical value. It defaults to 1/2 the total strength + epsilon


create_typed_game(player_types, coalition_values)
---------------------------------------------------
This factory method allows creating a TypedCoalitionalGame by specifying the player_types and coalition values.
player_types is a dictionary where the key is the type label and the value is the number of players of that type.
coalition_values is a dictionary where the key is a tuple of tuples, the first element of the inner
tuple is the tupe label and the second is the number of players in the coalition of that type. 
The function will fill in values not given according to the rule that the implied value of a coalition is the
value of the highest valued subcoalition with an explict value. ::

    vals = {(('L', 1), ('R',1)):1}
    tgp = {'L':2, 'R':1}
    tgg = create_typed_game(player_types=tgp, coalition_values=vals)
    print('typed gloves game valuation', tgg.get_valuation())


