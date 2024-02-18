================
Basic Usage
================

Overview
---------

This module contains functionality for anlyzing coalitional games.
A coalitional game is a structure including a set of players and a value (or cost)
for each subset of the players, called a coalition. In general the players can increase value
(or decrease cost) by forming coalitions as opposed to the individual players going their own way.
The coalition conating all players is called the grand coalition.
An assignment of value to players is called an imputation.

Reference
-----------
I used Game Theory by Michael Maschler, Elion Solan, and Shmuel Zamir (second edition) as my reference for definitions 
of game theory concepts. Page and chapter numbers below refer to the work. Any errors here are my own.

Coalition Properties
---------------------

Simple
~~~~~~~

A coalitional game is called "simple" if all coalitons have the value 0 or 1. It's pretty
simple to check if a coalitional structure is simple. Maschler p 713.

Monotonic
~~~~~~~~~~
A coalitional game is monotonic if the value of a coalition is always greater than or equal to
that of any subcoalitions.

Superadditive
~~~~~~~~~~~~
A coalitional game is called superadditive if the value of a coalition formed by the union of two disjoint subcoalitions is always greater than or equal to the sum of the values of the subcoalitions.

Shapley Value
~~~~~~~~~~~~~~
The Shapley Value is a particular imputation which is defined for all coalitional games. See Maschler Chapter 19.

Banhzhaf Value
~~~~~~~~~~~~~~~
The Banzhaf values is an imputation which is only defined for simple games. It effectively measures voting strength.

The Core
~~~~~~~~~
The core is the set of imputations which for all coalitions the total amount recived by the members is at least
the value of the coalition. The core may be empty. See Mascheler Chaper 18.

Strategic Equivalence
----------------------

Two coalitional games are considered strategically equivalent if you can transform one into the other by
adding a constant sum to all coaitions containing a player and then mutliplying the overall value by a constant.
See Maschler p 719.


Zero Normalize
---------------
A game is zero normalized by adding a set of offsets xi to all coalitions contating player i. We then multiply by some
(positive) factor to make the value of the grand coalition 1, 0, or -1 as appropriate.





