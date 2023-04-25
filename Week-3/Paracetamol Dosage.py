
def calculate_dose(weight, time, total_doze_24):
    """

    :param weight: weight of the patient
    :param time: time from previous dose
    :param total_doze_24:
    :return:
    """

    dose_per_weight = 15
    dose_base_on_weight = weight*dose_per_weight
    if time >= 6:
        if total_doze_24 == 0:
            amt_para = dose_base_on_weight
        elif total_doze_24 == dose_base_on_weight:
            amt_para = dose_base_on_weight
        else:
            amt_para = 4000 - total_doze_24
        return amt_para
    else:
        amt_para = 0
    return amt_para

def main():

    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_doze_24 = int(input("The total dose for the last 24 hours (mg): "))

    amt = calculate_dose(weight, time, total_doze_24)
    print(f"The amount of Parasetamol to give to the patient: {amt} ")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)

main()