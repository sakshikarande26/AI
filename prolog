# % facts
likes(john, pizza).
likes(mary, sushi).
likes(jane, pizza).

# % relationship
friend(X, Y) :- likes(X, Food), likes(Y, Food).

# query
likes(john, pizza),
likes(mary, pizza).
