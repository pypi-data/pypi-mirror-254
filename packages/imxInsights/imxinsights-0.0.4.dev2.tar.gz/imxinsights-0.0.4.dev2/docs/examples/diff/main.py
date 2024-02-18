from imxInsights import Imx, ImxDiff

imx = Imx(r"imx_file.xml")

# make diff from 2 situation
diff = ImxDiff(imx.project.initial_situation, imx.project.initial_situation)

# get diff dataframe
dict_of_df_of_all_types = diff.pandas_dataframe_dict()
df_micro_nodes = diff.pandas_dataframe("MicroNode", geometry=False)
df_signals = diff.pandas_dataframe("Signal", geometry=True)
df_rail_con = diff.pandas_dataframe("RailConnection", geometry=True)

# generate excel
diff.generate_excel("./diff.xlsx")
