# # todo: make tests
#
# from utils.helpers import hash_dict_ignor_nested_values
#
# a = [
#     {"@announcementType": "Unknown", "@delayTime": "0", "@installationRef": "7eef685f-27af-47c9-8de5-b9b7ad3a3279", "path": {}},
#     {"@announcementType": "Normal", "@delayTime": "0", "@installationRef": "82167510-3db7-4040-be8d-1f7d861bd4bc", "path": {}},
# ]
#
# b = [
#     {"@announcementType": "Normal", "@delayTime": "0", "@installationRef": "82167510-3db7-4040-be8d-1f7d861bd4bc"},
#     {"@announcementType": "Unknown", "@delayTime": "0", "@installationRef": "7eef685f-27af-47c9-8de5-b9b7ad3a3279"},
# ]
#
#
# a_sorted = sorted(a, key=hash_dict_ignor_nested_values)
# b_sorted = sorted(b, key=hash_dict_ignor_nested_values)
