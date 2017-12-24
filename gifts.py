#!/usr/bin/env python3

from __future__ import print_function
import random

NO_PEOPLE=10

def main():
    print("people_scores: ")
    people_scores = [None]*NO_PEOPLE
    for i in range(NO_PEOPLE):
        people_scores[i] = (list(range(0, NO_PEOPLE)))
        random.shuffle(people_scores[i])
        zero_pos = people_scores[i].index(0)
        if zero_pos != i:
            people_scores[i][zero_pos], people_scores[i][i] = people_scores[i][i], people_scores[i][zero_pos]
        print(people_scores[i])
    
    print("gift_scores: ") # The transport of people_scores
    gift_scores = [0]*NO_PEOPLE
    for i in range(NO_PEOPLE):
        gift_scores[i] = [people_scores[x][i] for x in range(0, NO_PEOPLE)]
        print(gift_scores[i])
    
    gift_taken = [None]*NO_PEOPLE
    for score in range(NO_PEOPLE-1, 0, -1):
        print("Score == "+str(score))
        for gid in range(0, NO_PEOPLE):
            print("\tGift ID == "+str(gid))
            if gift_taken[gid] == None: # The gift is not taken
                if gift_scores[gid].count(score) == 0:
                    pass
                elif gift_scores[gid].count(score) == 1: # Only 1 person gives the highest score
                    pid = gift_scores[gid].index(score)
                    gift_taken[gid] = pid
                    for scores in gift_scores:
                        scores[pid] = 0
                    print("\tThe gitf "+str(gid)+" is taken by #"+str(pid))
                else:
                    indices = [i for i, x in enumerate(gift_scores[gid]) if x == score]
                    tokens = [0]*NO_PEOPLE
                    for i in indices:
                        tokens[i] = sum(gift_scores[i])
                    print("\tCandidates == "+str(tokens))
                    max_token = max(tokens)
                    pid = -1
                    if tokens.count(max_token) == 1:
                        pid = tokens.index(max_token)
                    else:
                        candidates = [i for i, x in enumerate(tokens) if x == max_token]
                        pid = random.choice(candidates)
                    gift_taken[gid] = pid
                    for scores in gift_scores:
                        scores[pid] = 0
                    print("\tThe gitf "+str(gid)+" is taken by #"+str(pid))
    print("gift_taken: ")
    print(gift_taken)


if __name__ == "__main__":
    main()
