#!/usr/bin/env python3

from __future__ import print_function
import random

NO_PEOPLE=8
NO_SIM=100

def main():
    sim()

def sim():
    print("people_scores: ")
    people_scores = [None]*NO_PEOPLE
    people_scores[0] = [0,4,7,6,1,5,3,2]
    people_scores[1] = [3,0,5,1,7,4,6,2]
    people_scores[2] = [6,3,0,2,1,4,5,7]
    people_scores[3] = [1,7,4,0,3,6,5,2]
    people_scores[4] = [7,6,2,3,0,5,4,1]
    people_scores[5] = [7,5,4,3,2,0,6,1]
    people_scores[6] = [7,3,5,6,1,4,0,2]
    people_scores[7] = [6,5,2,3,4,7,1,0]
    for i in range(NO_PEOPLE):
        """
        people_scores[i] = (list(range(0, NO_PEOPLE)))
        random.shuffle(people_scores[i])
        zero_pos = people_scores[i].index(0)
        if zero_pos != i:
            people_scores[i][zero_pos], people_scores[i][i] = people_scores[i][i], people_scores[i][zero_pos]
        """
        print(people_scores[i])
    
    print("gift_scores: ") # The transport of people_scores
    gift_scores = [0]*NO_PEOPLE
    for i in range(NO_PEOPLE):
        gift_scores[i] = [people_scores[x][i] for x in range(0, NO_PEOPLE)]
        print(gift_scores[i])
    
    gift_taken = [None]*NO_PEOPLE
    for score in range(NO_PEOPLE-1, 0, -1):
        #print("Score == "+str(score))
        for gid in range(0, NO_PEOPLE):
            #print("\tGift ID == "+str(gid))
            if gift_taken[gid] == None: # The gift is not taken
                if gift_scores[gid].count(score) == 0:
                    pass
                elif gift_scores[gid].count(score) == 1: # Only 1 person gives the highest score
                    pid = gift_scores[gid].index(score)
                    gift_taken[gid] = pid
                    for scores in gift_scores:
                        scores[pid] = 0
                    #print("\tThe gitf "+str(gid)+" is taken by #"+str(pid))
                else:
                    indices = [i for i, x in enumerate(gift_scores[gid]) if x == score]
                    tokens = [0]*NO_PEOPLE
                    for i in indices:
                        tokens[i] = sum(gift_scores[i])
                    #print("\tCandidates == "+str(tokens))
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
                    #print("\tThe gitf "+str(gid)+" is taken by #"+str(pid))
    if gift_taken.count(None) > 1:
        print("Error!")
    print("gift_taken: "+str(gift_taken))


if __name__ == "__main__":
    main()
