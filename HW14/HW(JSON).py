# Task 4
# 6
import json


fk1 = {
    'name': 'Bavaria',
    'country': 'Germany',
    'wins': 33
}
fk2 = {
    'name': 'Legia',
    'country': 'Poland',
    'wins': 22
}
fk3 = {
    'name': 'Leh',
    'country': 'Poland',
    'wins': 11
}

fks = [fk1, fk2, fk3]

json_data = json.dumps(fks)


def get_wins(club):
    return club['wins']


max_wins_fk = max(fks, key=get_wins)

print(json_data)
print(f"Клуб с наибольшим количеством побед:{max_wins_fk}")
print()
