from services import comparison_service
import json

# Open the data file.
with open('image_data.json') as f:
    _image_data = json.load(f)

# Getting the size, keeps the code flexible.
sum_of = len(_image_data)

# Define the list that will contain the Tuple.
groups_db = []

# Current position for matching the ad for the correct groups.
current_group_position = -1

# -------------------------------------------------------------------------------------------------------------
# I HAVE BUILT THE COMPARISON ALGORITHM IN THE FOLLOWING WAY:
# 622 ==  0  =>  622 ==  1  =>  622 ==  2  =>  622 ==  3  =>  ......  =>  622 == 621
# WHEN IT COMES  622 == 622,  SKIP IT AND LOWER THE SIZE BY 1,
#  AND...
# 621 ==  0  =>  621 ==  1  =>  621 ==  2  =>  621 ==  3  =>  ......  =>  621 == 620
# 620 ==  0  =>  620 ==  1  =>  620 ==  2  =>  620 ==  3  =>  ......  =>  620 == 619
# IN THIS WAY I DON'T MISS ANYONE.
# -------------------------------------------------------------------------------------------------------------

# X and Y are locations index for comparison,
# X run from end to start (622 => 0).
for x in range((sum_of - 1), -1, -1):
    # Previous value -1 to start at 0.
    current_group_position += 1
    # Set the first tuple in the list in any round of X.
    groups_db.append([(_image_data[x]['ad_group_id'], _image_data[x]['ad_id'])])
    # Y run from start to end (0 => 622).
    for y in range(sum_of):
        if x == y:
            # If they are equals skip it end lower the sum by 1.
            sum_of -= 1
        else:
            # I started with the "urls_are_equal" func because it's the fastest initial filter.
            if comparison_service.urls_are_equal(_image_data[x]['url'], _image_data[y]['url']):
                if comparison_service.strings_are_equal(_image_data[x]['url'], _image_data[y]['url']):
                    if comparison_service.images_are_equal(_image_data[x]['url'], _image_data[y]['url']):
                        # Here i use the var:  "current_group_position" in order to locate the group tuple in the list,
                        # And append all "(ad_group_id, ad_id)" that belong.
                        groups_db[current_group_position].append(
                            (_image_data[y]['ad_group_id'], _image_data[y]['ad_id']))

# SHOW THE RESULT.
print(groups_db)
#                                                  Thank you it was really fun
#                                                            Beni S.

