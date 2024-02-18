from imxInsights import Imx

# load imx file
imx = Imx(r"imx_file.xml")

# get objects by path
locks_single_and_double_diamond = imx.project.initial_situation.get_by_paths(
    ["SingleSwitch.SwitchMechanism.Lock", "DoubleDiamondCrossing.SwitchMechanism.Lock"]
)
print(locks_single_and_double_diamond)
imx_object = locks_single_and_double_diamond[0]

# loop true children
for child in imx_object.children:
    print(child)
    print(child.parent)

# rail connection objects including geometry
rail_connections = imx.project.initial_situation.get_by_types(["RailConnection"])
rail_connection = rail_connections[0]
print(rail_connection.shapely)
print(rail_connection.geometry.shapelyM)

# access reffed objects
for reffed_object in rail_connections[0].reffed_objects:
    print(reffed_object)

# track fragments
pcc_tracks = imx.project.initial_situation.get_by_types(["PpcTrack"])
for track_fragment in pcc_tracks[0].reffed_objects:
    print(track_fragment)

# demarcation markers
operational_point_track = imx.project.initial_situation.get_by_types(["OperationalPointTrack"])
for demarcation_marker in operational_point_track[0].demarcation_markers:
    print(demarcation_marker)

# get objects as pandas dataframe
signals_df = imx.project.initial_situation.get_pandas_df(object_type_or_path="Signals")
print(signals_df)
dict_of_all_objects_df = imx.project.initial_situation.get_pandas_df_dict()
print(dict_of_all_objects_df["Signal"])

# get objects as geojson
signals_geojson_string = imx.project.initial_situation.get_geojson(object_type_or_path="Signals")
print(signals_geojson_string)
all_object_geojson = imx.project.initial_situation.get_geojson_dict()
print(all_object_geojson["Signal"])
