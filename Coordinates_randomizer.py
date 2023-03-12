import pandas as pd
import random
from shapely.geometry import Polygon, Point

POLY = Polygon([
    (29.323132695737534, -98.55862015742626),
    (29.336751454482062, -98.4837757970747),
    (29.432839901272136, -98.47914093989696),
    (29.421238382494945, -98.5884892370161)
])


def polygon_random_points(poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points_local = []
    while len(points_local) < num_points:
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        point = Point(x, y)
        if point.within(poly):
            points_local.append((x, y))
    return points_local


def main():
    points = polygon_random_points(POLY, 92)
    df = pd.DataFrame(points)
    #print(df)
    df.to_csv(r'C:\Users\MikeyO\Desktop\test.csv')


main()


# Polygon_A
# 29.58556326942255, -98.36056612821575
# 29.581383341276485, -98.58372591825481
# 29.44992603547386, -98.51025484891888
# 29.46666644514618, -98.41481112333294

# #Polygon_B
# 29.586160387882842, -98.48484896512981
# 29.5013342173057, -98.68878268095013
# 29.43617291834848, -98.61325167509075
# 29.40776384505494, -98.51368807645794

# #Polygon_C
# 29.362292810706986, -98.40657137723919
# 29.456204012835197, -98.41206454130169
# 29.466965355925403, -98.49995516630169
# 29.335958190082245, -98.49549197050091

# #Polygon_D
# 29.323132695737534, -98.55862015742626
# 29.336751454482062, -98.4837757970747
# 29.432839901272136, -98.47914093989696
# 29.421238382494945, -98.5884892370161
