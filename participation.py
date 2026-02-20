"""Rajani Baraili, Feb 20 2026,
Stores pet in dictionary with type of animal and owner and prints list
"""


pets = {
    "whiskers": {
        "animal": "bunny",
        "owner": "sara s"
    },

    "buddy": {
        "animal": "dog",
        "owner": "mira m"
    },

    "coco": {
        "animal": "cat",
        "owner": "kira a"
    },
    "mimi": {
        "animal": "dog",
        "owner": "emma m"
    },

    "sisca": {
        "animal": "bunny",
        "owner": "nina a"
    }

}


for pet in pets:

    print("Pet: ", pet, ", Pet type:", pets[pet]["animal"],", Owner name: ", pets[pet]["owner"]);