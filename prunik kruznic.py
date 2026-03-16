import math
def radius_sum(r1, r2):
    return r1 + r2

def euclid_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def has_intersection(circle_1, circle_2):
    x1, y1, r1 = circle_1["x"], circle_1["y"], circle_1["r"]
    x2, y2, r2 = circle_2["x"], circle_2["y"], circle_2["r"]

    d= euclid_distance(x1, y1, x2, y2)
    rs = radius_sum(r1, r2)

    if d > rs:
        return {"is_intersection": False, "intersection_count": 0}
    elif math.isclose(d , rs):
        return {"is_intersection": True, "intersection_count": 1}
    else: return {"is_intersection": True, "intersection_count": 2}

import matplotlib.pyplot as plt
def draw_data(circle_1, circle_2):
    fig, ax = plt.subplots()
    c1 = plt.Circle((circle_1["x"], circle_1["y"]),circle_1["r"], fill=False, color="blue")
    c2 = plt.Circle((circle_2["x"], circle_2["y"]), circle_2["r"], fill=False, color="red")

    ax.add_patch(c1)
    ax.add_patch(c2)

    ax.set_aspect("equal")
    plt.grid()
    plt.show()


circle_1 = {"x": 0, "y":0, "r": 2}
circle_2 = {"x": 3, "y":0, "r": 1}

result = has_intersection(circle_1, circle_2)
if result["is_intersection"]:
    print(f"Kružnice se protínají a mají {result['intersection_count']} průnik.")
else: print("krůžnice se neprotínají.")

draw_data(circle_1, circle_2)