import sumator
from instruments_for_all_operations import *


def calculate(order_x, sign_x, mantis_x):
    """All variables must be string."""
    operation_number = 7
    code_table = table_code_generator(mantis_x, "", 2)
    number_of_digits = len(mantis_x)
    order_x_in_list = list(order_x)
    sign_x_in_list = list(sign_x)
    mantis_x_in_list = list(mantis_x)
    order_of_operation = list()
    sign_of_operation = [0]
    mantis_of_operation = list()
    type_converter(order_x_in_list, int)
    type_converter(mantis_x_in_list, int)
    if order_x_in_list[4] == 1:
        sumator.full_addition_procedure(order_x_in_list, [0, 1])
        order_x_in_list = sumator.sumator_answer
        mantis_x_in_list.insert(0, 0)
        list_with_one = [0 for i in range(number_of_digits)]
        list_with_one.append(1)
        mantis_x_in_list = sumator.use_only_sumator_core(number_of_digits + 1, mantis_x_in_list, list_with_one)
        mantis_x_in_list.pop()
    order_x_in_list.pop()
    order_x_in_list.insert(0, 0)
    order_of_operation.extend(order_x_in_list)
    RGA = list()
    RGA.extend([0 for i in range(number_of_digits)])
    RGB = list()
    RGB.extend([0 for i in range (number_of_digits + 2)])
    RGC = list()
    RGC.extend(mantis_x_in_list)
    CT = number_of_digits
    k = 0
    microoperations = list()
    microoperations.append("RGA: ={0}".format(RGA))
    microoperations.append("RGB: ={0}".format(RGB))
    microoperations.append("RGC: ={0}".format(RGC))
    make_records(k, RGA, RGB, RGC, microoperations, code_table[CT], operation_number)
    k += 1
    microoperations = list()
    microoperations.append("2 (RGC: = l(RGC).0, RGB: = l(RCB).RGC[0])")
    for step in range(0, 2):
        RGC.reverse()
        transposition = RGC.pop()
        RGC.reverse()
        RGC.insert(len(RGC), 0)
        RGB.reverse()
        RGB.pop()
        RGB.reverse()
        RGB.insert(len(RGB), transposition)
    make_records(k, RGA, RGB, RGC, microoperations, "", operation_number)
    addRG = list()
    addRG.extend(RGA)
    sumator.mok_transform([1], addRG)
    addRG.extend([1, 1])
    microoperations = list()
    microoperations.append("RGB = RGB + not(RGA).11")
    make_records("", "", addRG, "", microoperations, "", operation_number)
    RGB = sumator.use_only_sumator_core(number_of_digits + 2, RGB, addRG)
    make_records("", "", RGB, "", "", code_table[CT], operation_number)
    while CT != 0:
        k += 1
        make_records(k, RGA, RGB, RGC, "", "", operation_number)
        RGC.reverse()
        transposition = RGC.pop()
        RGC.reverse()
        RGC.insert(len(RGC), 0)
        RGB.insert(len(RGB), transposition)
        RGB.reverse()
        transposition = RGB.pop()
        RGB.reverse()
        RGA.insert(len(RGA), int(not bool(transposition)))
        RGA.reverse()
        RGA.pop()
        RGA.reverse()
        microoperations = list()
        microoperations.append("RGC: = l(RGC).0")
        microoperations.append("RGB: = l(RGB).RGC[0]")
        microoperations.append("RGA: = l(RGA).not(RGB[0])")
        make_records("", RGA, RGB, RGC, microoperations, "", operation_number)
        RGC.reverse()
        transposition = RGC.pop()
        RGC.reverse()
        RGC.insert(len(RGC), 0)
        RGB.insert(len(RGB), transposition)
        RGB.reverse()
        transposition = RGB.pop()
        RGB.reverse()
        microoperations = list()
        microoperations.append("RGC: = l(RGC).0")
        microoperations.append("RGB: = l(RGB).RGC[0]")
        make_records("", "", RGB, RGC, microoperations, "", operation_number)
        if transposition == 0:
            addRG = list()
            addRG.extend(RGA)
            sumator.mok_transform([1], addRG)
            addRG.extend([1, 1])
            microoperations = list()
            microoperations.append("RGB[0] = 0 ⇒")
            microoperations.append("RGB: = RGB + not[R]A).11")
            make_records("", "", addRG, "", microoperations, "", operation_number)
            RGB = sumator.use_only_sumator_core(number_of_digits + 2, RGB, addRG)
        elif transposition == 1:
            addRG = list()
            addRG.extend(RGA)
            addRG.extend([1, 1])
            microoperations = list()
            microoperations.append("RGB[0] = 1 ⇒")
            microoperations.append("RGB: = RGB + RGA.11")
            make_records("", "", addRG, "", microoperations, "", operation_number)
            RGB = sumator.use_only_sumator_core(number_of_digits + 2, RGB, addRG)
        CT -= 1
        microoperations = list()
        if CT != 0:
            microoperations.append("CT: = CT - 1; CT ≠ 0")
        elif CT == 0:
            microoperations.append("CT: = CT - 1; CT = 0")
        make_records("", "", RGB, "", microoperations,  code_table[CT], operation_number)
    mantis_of_operation.extend(RGA)
    save_results_in_buffer(operation_number, order_of_operation, sign_of_operation, mantis_of_operation)
