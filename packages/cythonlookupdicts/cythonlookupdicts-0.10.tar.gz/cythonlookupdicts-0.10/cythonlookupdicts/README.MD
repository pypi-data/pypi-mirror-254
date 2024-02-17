# Insanely fast Cython lookup dicts for tedious datatypes (useful for Sports betting) 

Analyzing sports league data often involves complex operations, especially when dealing with team lineups and match statistics. The cythonlookupdicts library provides efficient and powerful tools, including LookUpDictMultiIndex and LookUpDictMultiValues and MultiIndexFinder, designed to streamline data retrieval, making it an ideal choice for sports analysts, coaches, and enthusiasts.


## Tested against Windows / Python 3.11 / Anaconda

## pip install cythonlookupdicts

## Copy + Paste Code (Explanation below)

```python

from cythonlookupdicts import (
    LookUpDictMultiIndex,
    LookUpDictMultiValues,
    MultiIndexFinder,
)

reps = 5 # Generate some random data, 

# Sample data: Teams and corresponding match statistics
_team_lineups = [
    ["TeamA", "Player1", "Player2"],
    ["TeamB", "Player3", "Player4"],
    ["TeamA", "Player1", "Player2"],
    ["TeamB", "Player3", "Player4"],
    ["TeamC", "Player5", "Player6"],
    ["TeamB", "Player3", "Player4"],
    ["TeamC", "Player5", "Player6"],
    ["TeamB", "Player3", "Player4"],
    ["TeamA", "Player1", "Player2"],
    ["TeamA", "Player1", "Player2"],
    ["TeamB", "Player3", "Player4"],
    ["TeamC", "Player5", "Player6"],
]
team_lineups = []
for h in range(reps):
    team_lineups.extend(_team_lineups)

_match_results = [
    {"goals_scored": 1, "goals_conceded": 2},
    {"goals_scored": 3, "goals_conceded": 1},
    {"goals_scored": 2, "goals_conceded": 0},
    {"goals_scored": 1, "goals_conceded": 2},
    {"goals_scored": 0, "goals_conceded": 1},
    {"goals_scored": 3, "goals_conceded": 0},
    {"goals_scored": 2, "goals_conceded": 1},
    {"goals_scored": 1, "goals_conceded": 2},
    {"goals_scored": 2, "goals_conceded": 0},
    {"goals_scored": 1, "goals_conceded": 2},
    {"goals_scored": 3, "goals_conceded": 1},
    {"goals_scored": 2, "goals_conceded": 0},
]
match_results = []
for h in range(reps):
    match_results.extend(_match_results)
# Create a LookUpDictMultiIndex instance for team lineups
team_lineup_index = LookUpDictMultiIndex(
    team_lineups, match_results, ignore_exceptions=False
)

# Example: Get match results for specific team lineups
selected_lineups = [["TeamA", "Player1", "Player2"], ["TeamB", "Player3", "Player4"]]
lineup_results = team_lineup_index[selected_lineups]

# Print the match results for the selected lineups
for lineup_indices in lineup_results:
    for idx, result_index in enumerate(lineup_indices):
        print(team_lineups[result_index], match_results[result_index], idx + 1)


# ['TeamA', 'Player1', 'Player2'] {'goals_scored': 1, 'goals_conceded': 2} 1
# ['TeamA', 'Player1', 'Player2'] {'goals_scored': 2, 'goals_conceded': 0} 2
# ['TeamA', 'Player1', 'Player2'] {'goals_scored': 2, 'goals_conceded': 0} 3
# ['TeamA', 'Player1', 'Player2'] {'goals_scored': 1, 'goals_conceded': 2} 4
# ['TeamA', 'Player1', 'Player2'] {'goals_scored': 1, 'goals_conceded': 2} 5
# ['TeamA', 'Player1', 'Player2'] {'goals_scored': 2, 'goals_conceded': 0} 6
# ['TeamA', 'Player1', 'Player2'] {'goals_scored': 2, 'goals_conceded': 0} 7
# ['TeamA', 'Player1', 'Player2'] {'goals_scored': 1, 'goals_conceded': 2} 8
# ['TeamA', 'Player1', 'Player2'] {'goals_scored': 1, 'goals_conceded': 2} 9
# ['TeamA', 'Player1', 'Player2'] {'goals_scored': 2, 'goals_conceded': 0} 10
# ['TeamA', 'Player1', 'Player2'] {'goals_scored': 2, 'goals_conceded': 0} 11
# ....

print("0000000000000000000000000000000000000000000000000000000000000000000000000000000")
# Ignoring Exceptions:

team_lineup_index["ignore_exceptions"] = True
selected_lineups = [
    ["TeamA", "Player1", "Player2"],
    ["TeamB", "Player3", "Player444444444444444444444444"],
    ["TeamC", "Player5", "Player6"],
]
lineup_results = team_lineup_index[selected_lineups]
print(lineup_results)

# [[0, 2, 8, 9, 12, 14, 20, 21, 24, 26, 32, 33, 36, 38, 44, 45, 48, 50, 56, 57], [], [4, 6, 11, 16, 18, 23, 28, 30, 35, 40, 42, 47, 52, 54, 59]]
print("1111111111111111111111111111111111111111111111111111111111111111111111111111111")
import random

input_data1x = team_lineups.copy()
input_data2x = match_results.copy()
random.shuffle(input_data1x)
random.shuffle(input_data2x)

dd = LookUpDictMultiValues(input_data1x, input_data2x, ignore_exceptions=True)
searchlist2 = [
    ["TeamB", "Player3", "Player4"],
    ["TeamC", "Player5", "Player6"],
    ["TeamC", "Player5", "Player67777777777"], # Exception ignored -> empty list 
]
allresus = dd[searchlist2]
print(allresus)
# [[{'goals_scored': 1, 'goals_conceded': 2}, {'goals_scored': 3, 'goals_conceded': 1},
# {'goals_scored': 2, 'goals_conceded': 0}, {'goals_scored': 1, 'goals_conceded': 2},
# {'goals_scored': 2, 'goals_conceded': 0}, {'goals_scored': 3, 'goals_conceded': 1},
# {'goals_scored': 0, 'goals_conceded': 1}, {'goals_scored': 2, 'goals_conceded': 1},
#  {'goals_scored': 1, 'goals_conceded': 2}, {'goals_scored': 1, 'goals_conceded': 2},
#  {'goals_scored': 1, 'goals_conceded': 2}, {'goals_scored': 2, 'goals_conceded': 0},
# {'goals_scored': 3, 'goals_conceded': 1}, {'goals_scored': 2, 'goals_conceded': 0},
# ....
print("22222222222222222222222222222222222222222222222222222222222222222222222222222")

import random

input_data1x = team_lineups.copy()
random.shuffle(input_data1x)

dd = MultiIndexFinder(input_data1x, ignore_exceptions=False)
searchlist2 = [
    ["TeamB", "Player3", "Player4"],
    ["TeamC", "Player5", "Player6"],
]
allresus = dd[searchlist2]
print(allresus)
# [[0, 4, 7, 8, 12, 13, 16, 17, 18, 19, 20, 21, 22, 24, 25, 32, 38, 40, 42, 46, 47, 51, 52, 53, 57], [2, 3, 5, 10, 11, 26, 27, 29, 30, 35, 39, 44, 49, 54, 56]]
print("333333333333333333333333333333333333333333333333333333333333333333333333333")
```

## Explanation


```python
Example: Team Lineups and Match Results
In the given example, we have simulated team lineups (team_lineups) and corresponding match results (match_results). The LookUpDictMultiIndex class enables the quick retrieval of match results based on specific team lineups, offering a seamless way to analyze team performance over multiple matches.


# Create a LookUpDictMultiIndex instance for team lineups
team_lineup_index = LookUpDictMultiIndex(
    team_lineups, match_results, ignore_exceptions=False
)

# Example: Get match results for specific team lineups
selected_lineups = [["TeamA", "Player1", "Player2"], ["TeamB", "Player3", "Player4"]]
lineup_results = team_lineup_index[selected_lineups]

# Print the match results for the selected lineups
for lineup_indices in lineup_results:
    for idx, result_index in enumerate(lineup_indices):
        print(team_lineups[result_index], match_results[result_index], idx + 1)
		
		
Advantage 1: Exception Handling
One notable advantage of CythonLookupDicts is its robust exception handling. By default, exceptions are raised for unmatched queries, providing clarity in data integrity. However, the library allows users to set ignore_exceptions to True for scenarios where partial matches are acceptable, offering flexibility in data exploration.


# Ignoring Exceptions:
team_lineup_index["ignore_exceptions"] = True
selected_lineups = [
    ["TeamA", "Player1", "Player2"],
    ["TeamB", "Player3", "Player444444444444444444444444"],
    ["TeamC", "Player5", "Player6"],
]
lineup_results = team_lineup_index[selected_lineups]
print(lineup_results)
# [[0, 2, 8, 9, 12, 14, 20, 21, 24, 26, 32, 33, 36, 38, 44, 45, 48, 50, 56, 57], [], [4, 6, 11, 16, 18, 23, 28, 30, 35, 40, 42, 47, 52, 54, 59]]


Advantage 2: Multi-Scenario Analysis
For users who need to analyze multiple scenarios simultaneously, CythonLookupDicts offers the LookUpDictMultiValues class. It allows users to efficiently retrieve match statistics for specified scenarios, providing a comprehensive overview of team performance.


# Multi-Scenario Analysis:
searchlist2 = [
    ["TeamB", "Player3", "Player4"],
    ["TeamC", "Player5", "Player6"],
    ["TeamC", "Player5", "Player67777777777"],
]
allresus = dd[searchlist2]
print(allresus)
# [[{'goals_scored': 1, 'goals_conceded': 2}, {'goals_scored': 3, 'goals_conceded': 1}, ...]]
Advantage 3: Multi-Index Finder
For scenarios where direct value retrieval is not necessary, the MultiIndexFinder class allows users to find indices of matching entries efficiently. This is particularly useful when working with large datasets and the focus is on identifying relevant indices.


# Multi-Index Finder:
searchlist3 = [
    ["TeamB", "Player3", "Player4"],
    ["TeamC", "Player5", "Player6"],
]
allresus = dd[searchlist3]
print(allresus)
# [[0, 4, 7, 8, 12, 13, 16, 17, 18, ...], [2, 3, 5, 10, 11, 26, 27, 29, 30, ...]]
```


