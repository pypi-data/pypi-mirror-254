# Libraries

from sys import displayhook
import pandas as pd
import numpy as np
from datetime import timedelta
import re
from . import nda_version_8_0


def _keys_check(df):
    """
    Internal Function. Do not use.

    To check for coloumns of the df being passed into the step, cycle, recipe functions.
    """
    counter1 = True
    col_list1 = [
        "record_ID",
        "cycle",
        "step_ID",
        "step_name",
        "time_in_step",
        "voltage_V",
        "current_mA",
        "capacity_mAh",
        "energy_mWh",
        "timestamp",
    ]

    col_list2 = [
        "DataPoint",
        "Cycle Index",
        "Step Index",
        "Step Type",
        "Time",
        "Voltage(V)",
        "Current(A)",
        "Capacity(Ah)",
        "Energy(Wh)",
        "Date",
    ]

    for i in col_list1:
        # print(i)
        if i not in df.keys():
            counter1 = False
            break
    if counter1 == True:
        return 0

    counter2 = True
    for i in col_list2:
        if i not in df.keys():
            counter2 = False
    if counter2 == True:
        return 1

    if counter1 == False & counter2 == False:
        return -1
    return -1


def _validator_cycle(df):
    """
    Internal Function. Do not use.

    To validate the data generated for the function cycle.
    """
    for id, i in df.iterrows():
        if pd.to_datetime(i["End_Date"]) > pd.to_datetime(i["Onset_Date"]):
            raise ValueError("Date error with cycle number " + str(i["Cycle_Index"]))
        if i["Cycle_Index"] < 1:
            raise ValueError("Cycle Index out of range; please check data.")
        if i["Chg_Onset_Volt_(V)"] < 1.5 or i["DChg_Onset_Volt_(V)"] < 1.5:
            raise ValueError(
                "Voltage value too low in cycle number " + str(i["Cycle_Index"])
            )
        if i["DCIR(mOhm)"] < 0:
            raise ValueError(
                "DCIR is negative in cycle number " + str(i["Cycle_Index"])
            )


def get_barcode(nda):
    """
    ## Parameters

    #### nda
        Path to the nda file.\n
    ----------
    ----------
    returns barcode entered during the test for the passed nda file
    """
    if nda.split(".")[-1] != "nda":
        raise ValueError("File passed in function is not an nda file")
    return nda_version_8_0.get_barcode(nda)


def get_start_time(nda):
    """
    ## Parameters

    #### nda
        Path to the nda file.\n
    ----------
    ----------
    returns start time for the passed nda file
    """
    if nda.split(".")[-1] != "nda":
        raise ValueError("File passed in function is not an nda file")
    return nda_version_8_0.get_st_time(nda)


def get_process_name(nda):
    """
    ## Parameters

    #### nda
        Path to the nda file.\n
    ----------
    ----------
    Returns recipe name for the passed NDA file
    """
    if nda.split(".")[-1] != "nda":
        raise ValueError("File passed in function is not an nda file")
    return nda_version_8_0.get_process_name(nda)


def get_remarks(nda):
    """
    ## Parameters

    #### nda
        Path to the nda file.\n
    ----------
    ----------
    Returns remarks entered during test for the passed NDA file
    """
    if nda.split(".")[-1] != "nda":
        raise ValueError("File passed in function is not an nda file")
    return nda_version_8_0.get_remarks(nda)


def records(
    nda: str, rename: bool = False, step_cycle: bool = False, include_aux: bool = False
):
    """
    ## Parameters

    #### nda:
        str\n
        Path to the nda file \n
    #### rename:
        bool (optional, by default is False)\n
        Set it to True if coloumns need to be renamed.\n
    #### step_cyclic:
        bool (optional, by default is False)\n
        Set it to true if you want the repeating step id field\n
    ----------
    ----------
    Returns a Dataframe record-wise for the nda file \n
    Use the rename argument if you want to rename the columns \n
    Use the step_cycle arguement if you want to include the cyclic/repetetive step_ID\n
    """
    if nda.split(".")[-1] != "nda":
        raise ValueError("File passed in function is not an nda file")
    df = nda_version_8_0.nda_in_df_out(nda, step_cycle, include_aux)
    rec_columns = {
        "record_ID": "DataPoint",
        "cycle": "Cycle Index",
        "step_ID": "Step Index",
        "step_name": "Step Type",
        "time_in_step": "Time",
        "voltage_V": "Voltage(V)",
        "current_mA": "Current(A)",
        "capacity_mAh": "Capacity(Ah)",
        "energy_mWh": "Energy(Wh)",
        "timestamp": "Date",
        "Validated": "Validated",
        "DCIR(mOhm)": "DCIR(mOhm)",
    }
    if rename == True:
        df["current_mA"] = df["current_mA"].div(1000)
        df["capacity_mAh"] = df["capacity_mAh"].div(1000)
        df["energy_mWh"] = df["energy_mWh"].div(1000)

        df = df.rename(columns=rec_columns)
    return df


def cycle(df, last_cycle_skip: bool = False):  #! Function to group the data cycle-wise
    """
    ## Parameters

    #### df:
        str/DataFrame \n
        Path to the nda file (Preferred) \n
        Or recordwise data without renamed fields\n
    #### last_cycle_skip:
        bool (optional, by default is False)\n
        Set it to True if the last cycle is to be skipped in case of an test that's\n
        still running or an incomplete test.\n
    ----------
    When passed an nda file or the records data,
    it returns Cycle-wise data identical to the
    cycle sheet in the excel file of the test.
    """
    try:
        if type(df) != type(pd.DataFrame()):
            df = nda_version_8_0.nda_in_df_out(df)

    except Exception:
        raise ValueError(
            "Argument pushed into the function is neither an appropiate DataFrame nor a path to an nda file"
        )
    rec_columns = {
        "DataPoint": "record_ID",
        "Cycle Index": "cycle",
        "Step Index": "step_ID",
        "Step Type": "step_name",
        "Time": "time_in_step",
        "Voltage(V)": "voltage_V",
        "Current(A)": "current_mA",
        "Capacity(Ah)": "capacity_mAh",
        "Energy(Wh)": "energy_mWh",
        "Date": "timestamp",
        "Validated": "Validated",
        "DCIR(mOhm)": "DCIR(mOhm)",
    }
    # print(df.head(2))
    keycheck = _keys_check(df)
    if keycheck == -1:
        raise ValueError(
            "Wrong dataframe entered. Kindly check the coloumn names. Or pass the nda file."
        )

    if keycheck == 1:
        df = df.rename(columns=rec_columns)

    if "DCIR(mOhm)" not in df.keys():
        df["prev_cur"] = df["current_mA"].shift(periods=1)
        df["prev_vol"] = df["voltage_V"].shift(periods=1)
        df["DCIR(mOhm)"] = -1
        df.loc[((df["prev_cur"] == 0) & (df["current_mA"] != 0)), "DCIR(mOhm)"] = (
            abs(
                (df["voltage_V"] - df["prev_vol"]) / (df["current_mA"] - df["prev_cur"])
            )
            * 1000000
        )
        df.drop(columns=["prev_cur", "prev_vol"], inplace=True)

    temp_list = []
    complete_list = []

    chg_temp = "CCCV_Chg"  # default values
    dchg_temp = "CC_Dchg"
    step_col = list(df["step_name"].unique()[1:])
    if not ((chg_temp in step_col) & (dchg_temp in step_col)):
        for col in step_col:
            if re.search("chg", col, re.IGNORECASE):
                if not re.search("d", col, re.IGNORECASE):
                    chg_temp = col
            if re.search("dchg", col, re.IGNORECASE):
                dchg_temp = col

    lastcycle_counter = 0
    if (
        df[df["cycle"] == max(df["cycle"])].step_ID.nunique()
        == df.groupby(["cycle"]).step_ID.nunique().mode()[0]
    ):
        lastcycle_counter = 1

    if last_cycle_skip == True:
        lastcycle_counter = 0

    for i in range(min(df["cycle"]), max(df["cycle"] + lastcycle_counter)):
        df2 = df[df["cycle"] == i].reset_index()
        cycle = i

        starting_date = df2.at[0, "timestamp"]
        end_date = df2.iloc[-1].at["timestamp"]

        df_chg = df2[(df2["step_name"] == chg_temp)].reset_index()
        df_dchg = df2[(df2["step_name"] == dchg_temp)].reset_index()

        charging_capacity = df_chg.iloc[-1].at["capacity_mAh"]
        discharging_capacity = df_dchg.iloc[-1].at["capacity_mAh"]

        charging_energy = df_chg.iloc[-1].at["energy_mWh"]
        discharging_energy = df_dchg.iloc[-1].at["energy_mWh"]

        chg_starting_volt = df_chg.at[0, "voltage_V"]
        chg_ending_volt = df_chg.iloc[-1].at["voltage_V"]

        dchg_starting_volt = df_dchg.at[0, "voltage_V"]
        dchg_ending_volt = df_dchg.iloc[-1].at["voltage_V"]

        chg_starting_current = df_chg.at[0, "current_mA"]
        chg_ending_current = df_chg.iloc[-1].at["current_mA"]

        dchg_starting_current = df_dchg.at[0, "current_mA"]
        dchg_ending_current = df_dchg.iloc[-1].at["current_mA"]

        chgtime = df_chg.iloc[-1].at["time_in_step"]
        charging_time = "{:02}:{:02}:{:02}".format(
            chgtime // 3600, chgtime % 3600 // 60, chgtime % 60
        )
        dchgtime = df_dchg.iloc[-1].at["time_in_step"]
        discharging_time = "{:02}:{:02}:{:02}".format(
            dchgtime // 3600, dchgtime % 3600 // 60, dchgtime % 60
        )

        dcir_cyl = df2.loc[df2["DCIR(mOhm)"] > 0, "DCIR(mOhm)"]

        DCIR_avg = dcir_cyl.mean()

        temp_list = [
            cycle,
            starting_date,
            end_date,
            charging_capacity,
            discharging_capacity,
            charging_energy,
            discharging_energy,
            charging_time,
            discharging_time,
            chg_starting_volt,
            dchg_starting_volt,
            chg_ending_volt,
            dchg_ending_volt,
            chg_starting_current / 1000,
            dchg_starting_current / 1000,
            chg_ending_current / 1000,
            dchg_ending_current / 1000,
            DCIR_avg,
        ]

        complete_list.append(temp_list)
    df3 = pd.DataFrame(
        complete_list,
        columns=[
            "Cycle Index",
            "Onset Date",
            "End Date",
            "Chg. Cap.(Ah)",
            "DChg. Cap.(Ah)",
            "Chg. Energy(Wh)",
            "DChg. Energy_(Wh)",
            "Chg_Time(hh:mm:ss)",
            "DChg_Time(hh:mm:ss)",
            "Chg_Onset_Volt_(V)",
            "DChg_Onset_Volt_(V)",
            "End_of_Chg_Volt(V)",
            "End_of_DChg_Volt(V)",
            "Chg_Oneset_Current(A)",
            "DChg_Oneset_Curent(A)",
            "End_of_Chg_Current(A)",
            "End_of_DChg_Current(A)",
            "DCIR(mOhm)",
        ],
    )
    return df3


def _validator_step(df):
    for id, i in df.iterrows():
        if pd.to_datetime(i["End Date"]) > pd.to_datetime(i["Onset Date"]):
            raise ValueError("Date error with cycle number " + str(i["Cycle_Index"]))
        if i["Cycle_Index"] < 1:
            raise ValueError("Cycle Index out of range; please check data.")
        if i["Chg_Onset_Volt_(V)"] < 1.5 or i["DChg_Onset_Volt_(V)"] < 1.5:
            raise ValueError(
                "Voltage value too low in cycle number " + str(i["Cycle_Index"])
            )
        if i["DCIR(mOhm)"] < 0:
            raise ValueError(
                "DCIR is negative in cycle number " + str(i["Cycle_Index"])
            )


def step(df):  #! Function to group the data step-wise
    """
    ## Parameters

    #### df:
        str/DataFrame\n
        Path to the nda file (Preferred) \n
        Or recordwise data without renamed fields\n
    #### last_step_skip:
        bool (optional, by default is False)\n
        Set it to True if the last step is to be skipped in case of an test that's
        still running or an incomplete test.\n
    ----------
    ----------
    When passed an nda file or the records data,
    it returns Step-wise data identical to the
    step sheet in the generated excel file of a test.
    """
    try:
        if type(df) != type(pd.DataFrame()):
            df = nda_version_8_0.nda_in_df_out(df)
    except:
        raise ValueError(
            "Argument pushed into the function is neither an appropriate DataFrame nor a path to an nda file"
        )

    rec_columns = {
        "DataPoint": "record_ID",
        "Cycle Index": "cycle",
        "Step Index": "step_ID",
        "Step Type": "step_name",
        "Time": "time_in_step",
        "Voltage(V)": "voltage_V",
        "Current(A)": "current_mA",
        "Capacity(Ah)": "capacity_mAh",
        "Energy(Wh)": "energy_mWh",
        "Date": "timestamp",
        "Validated": "Validated",
        "DCIR(mOhm)": "DCIR(mOhm)",
    }
    # print(df.head(2))
    keycheck = _keys_check(df)
    if keycheck == -1:
        raise ValueError(
            "Wrong dataframe entered. Kindly check the coloumn names. Or pass the nda file."
        )

    if keycheck == 1:
        df = df.rename(columns=rec_columns)

    if "DCIR(mOhm)" not in df.keys():
        df["prev_cur"] = df["current_mA"].shift(periods=1)
        df["prev_vol"] = df["voltage_V"].shift(periods=1)
        df["DCIR(mOhm)"] = -1
        df.loc[((df["prev_cur"] == 0) & (df["current_mA"] != 0)), "DCIR(mOhm)"] = (
            abs(
                (df["voltage_V"] - df["prev_vol"]) / (df["current_mA"] - df["prev_cur"])
            )
            * 1000000
        )
        df.drop(columns=["prev_cur", "prev_vol"], inplace=True)

    df["prev_cur"] = df["current_mA"].shift(periods=1)
    df["prev_vol"] = df["voltage_V"].shift(periods=1)
    df["prev_step"] = df["step_ID"].shift(periods=1)

    temp_list = []
    complete_list = []

    for i in range(min(df["step_ID"]), max(df["step_ID"]) + 1):
        df2 = df[df["step_ID"] == i]
        DCIR = list(df2["DCIR(mOhm)"])[0]
        Starting_Volt = list(df2["voltage_V"])[0]
        End_Voltage = list(df2["voltage_V"])[-1]
        Starting_current = list(df2["current_mA"])[0]
        End_Current = list(df2["current_mA"])[-1]
        Capacity = list(df2["capacity_mAh"])[-1]
        Energy = list(df2["energy_mWh"])[-1]
        Starting_Date = list(df2["timestamp"])[0]
        End_Date = list(df2["timestamp"])[-1]
        Step_Time = timedelta(seconds=list(df2["time_in_step"])[-1])
        step_ID = i
        Maximum_voltage = max(list(df2["voltage_V"]))
        Minimum_voltage = min(list(df2["voltage_V"]))
        Step_Type = list(df2["step_name"])[0]
        Cycle_Index = list(df2["cycle"])[0]

        temp_list = [
            Cycle_Index,
            step_ID,
            Step_Type,
            str(Step_Time),
            Starting_Date,
            End_Date,
            Capacity / 1000,
            Energy / 1000,
            Starting_Volt,
            End_Voltage,
            Starting_current / 1000,
            End_Current / 1000,
            Maximum_voltage,
            Minimum_voltage,
            DCIR,
        ]
        complete_list.append(temp_list)

    col_list = [
        "Cycle Index",
        "Step Number",
        "Step Type",
        "Step Time",
        "Onset Date",
        "End Date",
        "Capacity(Ah)",
        "Energy(Wh)",
        "Onset Volt.(V)",
        "End Voltage(V)",
        "Starting current(A)",
        "Termination current(A)",
        "Max Volt.(V)",
        "Min Volt(V)",
        "DCIR(mOhm)",
    ]

    df = pd.DataFrame(complete_list, columns=col_list)
    return df


# Function to find distinct-recipes
def _df_diff(df1, df2):
    """
    Internal Function. Do not use.
    """
    vol_diff = abs(df1["Voltage"]) - abs(df2["Voltage"])
    curr_diff = abs(df1["Current"]) - abs(df2["Current"])
    cutoff_curr_diff = abs(df1["Cutoff_current"]) - abs(df2["Cutoff_current"])
    cutoff_vol_diff = abs(df1["Cutoff_voltage"]) - abs(df2["Cutoff_voltage"])
    if list(df1["Step_Name"]) != list(df2["Step_Name"]):
        return -1
    if list(df1["Rest_time"]) != list(df2["Rest_time"]):
        return -1
    combined = []
    for i in range(len(vol_diff)):
        combined.append(vol_diff[i])
        combined.append(curr_diff[i])
        combined.append(cutoff_curr_diff[i])
        combined.append(cutoff_vol_diff[i])
    for i in combined:
        if abs(i) > 0.05:
            return -1
    return 1


def recipe(df):
    """
    ## Parameters

    #### df:
        str or pandas.DataFrame
        Path to the nda file (Preferred) \n
        Or recordwise data without renamed fields\n

    ----------
    When passed an nda file or the records data,
    it prints the recipe(s) with the cycle numbers by analysing the values of the data.
    It also returns two dictionaries. First one with the cycle numbers denoting the cycle numbers corresponding to the recipe.
    And the second one with the recipe(s) based off the data and its values.
    """
    try:
        if type(df) != type(pd.DataFrame()):
            df = nda_version_8_0.nda_in_df_out(df)
    except:
        raise ValueError(
            "Argument pushed into the function is neither an appropriate DataFrame nor a path to an nda file"
        )

    dict_voltage = {}
    dict_recipe = {}
    dict_rest = {}
    dict_current = {}
    dict_step = {}
    dict_cycle = {}
    recipe_cycle = []
    dict_stepid = {}
    dict_cutoff_curr = {}
    dict_cutoff_vol = {}
    chg_temp = ""
    dchg_temp = ""
    step_col = list(df["step_name"].unique()[1:])
    for col in step_col:
        if re.search("_chg", col, re.IGNORECASE):
            chg_temp = col
        if re.search("_dchg", col, re.IGNORECASE):
            dchg_temp = col

    for i in range(min(df["cycle"]), max(df["cycle"])):
        # For non-validated files

        df2 = df[df["cycle"] == i]
        recipe_cycle.append(i)
        dict_recipe[i] = []
        dict_rest[i] = []
        dict_voltage[i] = []
        dict_current[i] = []
        dict_step[i] = []
        dict_cycle[i] = []
        dict_stepid[i] = []
        dict_cutoff_curr[i] = []
        dict_cutoff_vol[i] = []
        for j in range(min(df2["step_ID"]), max(df2["step_ID"]) + 1):
            df3 = df2[df2["step_ID"] == j]
            dict_recipe[i].append(df3["step_name"].iloc[0])

            dict_step[i].append(j)

            dict_cycle[i].append(i)

            dict_stepid[i].append(j)

            if df3["step_name"].iloc[0] == "Rest":
                dict_rest[i].append(timedelta(seconds=list(df3["time_in_step"])[-1]))
            else:
                dict_rest[i].append(0)

            if df3["step_name"].iloc[0] == chg_temp:
                dict_voltage[i].append(round(df3["voltage_V"].max(), 2))
                dict_cutoff_vol[i].append(0)
            elif df3["step_name"].iloc[0] == dchg_temp:
                dict_voltage[i].append(round(df3["voltage_V"].min(), 2))
                dict_cutoff_vol[i].append(round(list(df3["voltage_V"])[-1], 2))
            else:
                dict_voltage[i].append(0)
                dict_cutoff_vol[i].append(0)

            if df3["step_name"].iloc[0] == chg_temp:
                dict_current[i].append(round(df3["current_mA"].iloc[0] / 1000, 2))
                dict_cutoff_curr[i].append(round(list(df3["current_mA"])[-1] / 1000, 2))
            elif df3["step_name"].iloc[0] == dchg_temp:
                dict_current[i].append(round(df3["current_mA"].iloc[0] / 1000, 2))
                dict_cutoff_curr[i].append(0)
            else:
                dict_current[i].append(0)
                dict_cutoff_curr[i].append(0)

    recipe = []
    rest = []
    voltage = []
    current = []
    cycle = []
    stepid = []
    cutoff_curr = []
    cutoff_vol = []

    for i in recipe_cycle:
        for j in range(len(dict_recipe[i])):
            recipe.append(dict_recipe[i][j])
            rest.append(dict_rest[i][j])
            voltage.append(dict_voltage[i][j])
            current.append(dict_current[i][j])
            cycle.append(dict_cycle[i][j])
            stepid.append(dict_stepid[i][j])
            cutoff_curr.append(dict_cutoff_curr[i][j])
            cutoff_vol.append(dict_cutoff_vol[i][j])

    df_recipe = pd.DataFrame(
        zip(
            np.array(stepid).reshape(-1, 1),
            np.array(cycle).reshape(-1, 1),
            np.array(recipe).reshape(-1, 1),
            np.array(voltage).reshape(-1, 1),
            np.array(current).reshape(-1, 1),
            np.array(rest).reshape(-1, 1),
            np.array(cutoff_curr).reshape(-1, 1),
            np.array(cutoff_vol).reshape(-1, 1),
        ),
        columns=[
            "Step_Id",
            "Cycle",
            "Step_Name",
            "Voltage",
            "Current",
            "Rest_time",
            "Cutoff_current",
            "Cutoff_voltage",
        ],
    )

    for col in df_recipe.columns:
        df_recipe[col] = df_recipe[col].apply(lambda x: x[0])

    # df_recipe.replace(r'nan',r' ',regex=True,inplace=True)

    recipe_unmatch = [1]
    for i in range(len(recipe_cycle) - 1):
        # df_temp1=df_recipe.groupby('Cycle').get_group(recipe_cycle[i])
        df_temp1 = df_recipe[df_recipe["Cycle"] == recipe_cycle[i]]
        # df_temp2=df_recipe.groupby('Cycle').get_group(recipe_cycle[i+1])
        df_temp2 = df_recipe[df_recipe["Cycle"] == recipe_cycle[i + 1]]
        df_temp1 = df_temp1.drop(["Cycle", "Step_Id"], axis=1)
        df_temp2 = df_temp2.drop(["Cycle", "Step_Id"], axis=1)
        if (df_temp1.reset_index(drop=True).shape) == (
            df_temp2.reset_index(drop=True).shape
        ) and _df_diff(
            df_temp1.reset_index(drop=True), df_temp2.reset_index(drop=True)
        ) == 1:
            continue
        else:
            recipe_unmatch.append(recipe_cycle[i + 1])
    recipe_unmatch.append(df_recipe["Cycle"].max())
    recipe_unmatch = sorted(list(set(recipe_unmatch)))

    dict_consecutive = {}
    for i in range(len(recipe_unmatch) - 1):
        dict_consecutive[recipe_unmatch[i]] = recipe_unmatch[i + 1]

    # print('Done')

    dict = {}
    for i in range(len(recipe_unmatch) - 1):
        dict[recipe_unmatch[i]] = []
        # df1=df_recipe.groupby('Cycle').get_group(recipe_unmatch[i]).reset_index(drop=True)
        df1 = df_recipe[df_recipe["Cycle"] == recipe_unmatch[i]].reset_index(drop=True)
        df1 = df1.drop(["Cycle", "Step_Id"], axis=1)
        for j in range(i + 1, len(recipe_unmatch)):
            # df2=df_recipe.groupby('Cycle').get_group(recipe_unmatch[j]).reset_index(drop=True)
            df2 = df_recipe[df_recipe["Cycle"] == recipe_unmatch[j]].reset_index(
                drop=True
            )
            df2 = df2.drop(["Cycle", "Step_Id"], axis=1)
            if df1.shape == df2.shape and _df_diff(df1, df2) == 1:
                dict[recipe_unmatch[i]].append(recipe_unmatch[j])

    # print(dict)

    dict_temp = {}
    for i in dict:
        if i in dict_consecutive:
            dict_temp[i] = [[i, dict_consecutive[i] - 1]]
            if len(dict[i]) != 0:
                for j in dict[i]:
                    if j in dict_consecutive:
                        dict_temp[i].append([j, dict_consecutive[j] - 1])
                        del dict_consecutive[j]

    # print(dict_temp)
    iter = 1
    dict_recipe_range = {}
    for x in dict_temp:
        dict_recipe_range["Recipe-{k}".format(k=x)] = dict_temp[x]
        iter += 1
    print(dict_recipe_range)

    arr = []
    dict_ = {}
    k = 0
    temp_list = list(dict_temp.keys())
    for i in range(len(temp_list)):
        k += 1
        # df_temp=df_recipe.groupby('Cycle').get_group(recipe_unmatch[i])
        df_temp = df_recipe[df_recipe["Cycle"] == temp_list[i]]
        df_temp = df_temp.drop(["Cycle", "Step_Id"], axis=1).reset_index(drop=True)
        arr.append(df_temp)
        print("Recipe-{k}".format(k=k))
        dict_["Recipe-{k}".format(k=k)] = df_temp
        displayhook(df_temp)
    return dict_recipe_range, dict_
    # print('\ntest:\n')


def nda_to_excel(nda: str, save_path: str):
    """
    ## Parameters

    #### nda
        Path to the nda file.\n
    #### save_path
        Path where to save the excel \n
        file including the name of the file (with the extension .xlsx).\n
    ----------
    ----------
    Returns cycle,step,record sheets same as generated by the BTS celltesting software.
    """
    writer = pd.ExcelWriter(save_path)
    df = records(nda)
    cycle(df).to_excel(writer, sheet_name="cycle", engine="xlsxwriter", index=False)
    step(df).to_excel(writer, sheet_name="step", engine="xlsxwriter", index=False)
    df.to_excel(writer, sheet_name="records", engine="xlsxwriter", index=False)
    writer.close()
