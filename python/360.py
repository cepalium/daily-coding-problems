# ------------------------------
# Author: Tuan Nguyen
# Date created: 20200507
#!360.py
# ------------------------------
"""
You have access to ranked lists of songs for various users. 
Each song is represented as an integer, and more preferred songs appear earlier in each list. 
For example, the list [4, 1, 7] indicates that a user likes song 4 the best, followed by songs 1 and 7.

Given a set of these ranked lists, interleave them to create a playlist that satisfies everyone's priorities.

For example, suppose your input is {[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]}. 
In this case a satisfactory playlist could be [2, 1, 6, 7, 3, 9, 5].
"""
def satisfied_playlist(lists):
    if len(lists) == 0:  # trivial cases
        return []
    if len(lists) == 1:
        return lists[0]
    final_list = lists[0].copy()  # initialize with 1st ranked list
    for ranked_list in lists[1:]:
        final_list = update(ranked_list, final_list)
    return final_list

def update(ranked_list, final_list):
    for i in range(len(ranked_list)-1):
        higher_rated_song, lower_rated_song = ranked_list[i], ranked_list[i+1]
        final_list = update_rank(higher_rated_song, lower_rated_song, final_list)
    return final_list

def update_rank(high_song, low_song, final_list):
    if (low_song not in final_list) and (high_song not in final_list):
        final_list.append(high_song)
        final_list.append(low_song)
    elif (low_song not in final_list) and (high_song in final_list):
        high_index = final_list.index(high_song)
        final_list.insert(high_index + 1, low_song)
    elif (low_song in final_list) and (high_song not in final_list):
        low_index = final_list.index(low_song)
        final_list.insert(low_index, high_song)
    else:  # both songs in final list
        final_list = update_rank_2_songs_already_in_list(high_song, low_song, final_list)
    return final_list

def update_rank_2_songs_already_in_list(high_song, low_song, final_list):
    high_index = final_list.index(high_song)
    low_index = final_list.index(low_song)
    if high_index > low_index:
        final_list.pop(low_index)
        final_list.insert(high_index + 1, low_song)
    return final_list


def test1():
    assert satisfied_playlist([[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]]) == [2, 1, 6, 7, 3, 9, 5]

def test2():
    assert satisfied_playlist([]) == []

def test3():
    assert satisfied_playlist([[1, 2, 3]]) == [1, 2, 3]

def test4():
    assert satisfied_playlist([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]

def test5():
    assert satisfied_playlist([[1, 7, 3], [2, 1, 6, 8, 9], [3, 9, 5]]) == [2, 1, 6, 8, 7, 3, 9, 5]

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()