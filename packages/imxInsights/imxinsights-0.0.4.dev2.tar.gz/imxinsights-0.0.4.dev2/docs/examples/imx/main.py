from imxInsights import Imx

# load imx file
imx = Imx(r"imx_file.xml")
print(imx.imx_version)
print(imx.file_path)

# get metadata from project imx
print(imx.project.metadata.project_type)
print(imx.project.metadata.project_name)
print(imx.project.metadata.created_date)
print(imx.project.metadata.planned_delivery_date)
print(imx.project.metadata.project_areas)

# get metadata from situation
print(imx.project.initial_situation.reference_date)
print(imx.project.initial_situation.perspective_date)

# get objects by puic
imx_object = imx.project.initial_situation.get_by_puic("puic_value")
print(imx_object)
print(imx_object.properties)
print(imx_object.metadata.source)
print(imx_object.metadata.origin_type)
print(imx_object.metadata.location_accuracy)
print(imx_object.metadata.location_data_acquisition_method)

# get objects by types
list_of_signs_and_speedsigns = imx.project.initial_situation.get_by_types(["Sign", "SpeedSign"])
print(list_of_signs_and_speedsigns[0])

# use off imx object
print(imx_object.puic)
print(imx_object.name)

# get imx object geometry
print(imx_object.geometry)
print(imx_object.geometry.azimuth)
print(imx_object.shapely)

# project areas on individual objects
print(imx_object.area)
