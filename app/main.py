from fastapi import FastAPI, Body
from typing import Any

app = FastAPI()

def match_checker(search_term: str, current_obj: dict):
    # Returns a tuple to represent the result of searching the object
    # First tuple element is a boolean representing if an exact match was found
    # Second element is a number of characters matched (can be 0)
    chars_matched = 0

    search_term = search_term.lower()

    for val in current_obj.values():
        val_str = str(val).lower()
        if search_term == val_str:
            # Can stop searching if an exact match is found
            return (True, len(search_term))
        
        # Check for longest partial substring match
        for substr_len in range(len(search_term), 0, -1):
            # If a match longer than this already found, stop
            if substr_len <= chars_matched:
                break

            # Stop decreasing substr_len as soon as a match is found (longest to shortest)
            found_match = False

            # Check every substring of the search_term with correct substr_length
            for start_idx in range(len(search_term) - substr_len + 1):
                current_substr = search_term[start_idx : start_idx + substr_len]

                if current_substr in val_str:
                    chars_matched = substr_len
                    found_match = True
                    # Break out of the start_idx loop
                    break
            
            # Break out of the substr_len loop when a match is found
            if found_match:
                break
    
    return (False, chars_matched)

        

def perform_merge(search_term: str, left_set: list, right_set: list):
    result = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left_set) and right_idx < len(right_set):
        left_exact, left_len = match_checker(search_term, left_set[left_idx])
        right_exact, right_len = match_checker(search_term, right_set[right_idx])

        # Pick the better match (left default)
        right_superior = False
        if (right_exact and not left_exact) or (right_len > left_len and not left_exact):
            right_superior = True
        
        if right_superior:
            result.append(right_set[right_idx])
            right_idx += 1
        else:
            result.append(left_set[left_idx])
            left_idx += 1
    
    # Handle remaining items in either half that havent been examined yet
    result.extend(left_set[left_idx:])
    result.extend(right_set[right_idx:])
    return result
        

def merge_sort(search_term: str, data_set: list):
    # Recursive function to perform a merge sort on the data set

    # Base case: One or less objects in the data set
    if len(data_set) <= 1:
        return data_set
    
    mid_idx = len(data_set) // 2
    left_set = merge_sort(search_term, data_set[:mid_idx])
    right_set = merge_sort(search_term, data_set[mid_idx:])

    return perform_merge(search_term, left_set, right_set)

@app.post("/search/{search_term}")
async def search_data(search_term: str, data: list[dict[str, Any]] = Body(...)):
    return merge_sort(search_term, data)