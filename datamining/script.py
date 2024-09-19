import numpy as np

# Dataset
users = {
    "Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
                 "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
    "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0,
             "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
    "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0,
             "Phoenix": 5.0, "Slightly Stoopid": 1.0},
    "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0,
            "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
    "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
               "Vampire Weekend": 1.0},
    "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0,
               "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
    "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0,
            "Slightly Stoopid": 4.0, "The Strokes": 5.0},
    "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                 "The Strokes": 3.0}
}

def manhattan_distance(ratings1, ratings2):
    """Calcula la distancia de Manhattan entre dos usuarios."""
    all_items = set(ratings1.keys()).union(set(ratings2.keys()))
    distance = sum(abs(ratings1.get(item, 0) - ratings2.get(item, 0)) for item in all_items)
    return distance

def compute_nearest_neighbor(user, user_data):
    """Encuentra el vecino más cercano al usuario dado."""
    nearest_neighbor = None
    min_distance = float('inf')
    
    for other_user in user_data:
        if other_user != user:
            distance = manhattan_distance(user_data[user], user_data[other_user])
            if distance < min_distance:
                min_distance = distance
                nearest_neighbor = other_user
    
    return nearest_neighbor

# Ejemplo de uso
test_user = "Angelica"
nearest = compute_nearest_neighbor(test_user, users)

print(f"El vecino más cercano a {test_user} es: {nearest}")
