import sumator
from instruments_for_all_operations import *


def calculate(operation_number, order_x, order_y, sign_x, sign_y, mantis_x, mantis_y):
    """All variables must have type string."""
    operation_number = int(operation_number)
    memory_buffer.clear_operation(operation_number)
    number_of_digits = len(mantis_x)
    order_x_in_list = list(order_x)
    order_y_in_list = list(order_y)
    sign_x_in_list = list(sign_x)
    sign_y_in_list = list(sign_y)
    mantis_x_in_list = list(mantis_x)
    mantis_y_in_list = list(mantis_y)
    type_converter(order_x_in_list, int)
    type_converter(order_y_in_list, int)
    type_converter(sign_x_in_list, int)
    type_converter(sign_y_in_list, int)
    type_converter(mantis_x_in_list, int)
    type_converter(mantis_y_in_list, int)
    sumator.full_addition_procedure(order_x_in_list, order_y_in_list, True)
    order_of_operation = sumator.sumator_answer
    sign_of_operation = sumator.use_only_sumator_core(1, sign_x_in_list, sign_y_in_list)
    mantis_of_operation = list()

    if operation_number == 4:
        RG1 = list()
        RG1.extend([0, 0])
        RG1.extend(mantis_y_in_list)
        RG2 = list()
        RG2.extend([0, 0])
        RG2.extend(mantis_x_in_list)
        RG3 = [1 for i in range(number_of_digits + 1)]
        k = 0
        microoperations = list()
        microoperations.append("RG3:= {0}".format(RG3))
        microoperations.append("RG1:= {0}".format(RG1))
        microoperations.append("RG2:= {0}".format(RG2))
        make_records(k, RG1, RG2, RG3, microoperations, on=operation_number)
        while RG3[0] != 0:
            k += 1
            microoperations = list()
            if RG2[0] == 1:
                make_records(k, "", RG1, "", "", on=operation_number)
                RG2 = sumator.use_only_sumator_core(2 + number_of_digits, RG2, RG1)
                make_records("", "", RG2, "", "", on=operation_number)
                RG3.reverse()
                RG3.pop()
                RG3.reverse()
                RG3.insert(len(RG3), int(not bool(RG2[0])))
                RG2.reverse()
                RG2.pop()
                RG2.reverse()
                RG2.insert(len(RG2), 0)
                microoperations.append("RG2:= RG2 + RG1")
                microoperations.append("RG3:= l(RG3).not(RG2[1])")
                microoperations.append("RG2:= l(RG2).0")
            elif RG2[0] == 0:
                addRG = list()
                addRG.extend(RG1)
                sumator.mok_transform([1], addRG)
                list_with_one = [0 for i in range(number_of_digits + 1)]
                list_with_one.append(1)
                addRG = sumator.use_only_sumator_core(2 + number_of_digits, addRG, list_with_one)
                make_records("", "", addRG, "", "", "", on=operation_number)
                RG2 = sumator.use_only_sumator_core(2 + number_of_digits, addRG, RG2)
                make_records("", "", RG2, "", "", "", on=operation_number)
                RG3.reverse()
                RG3.pop()
                RG3.reverse()
                RG3.insert(len(RG3), int(not bool(RG2[0])))
                RG2.reverse()
                RG2.pop()
                RG2.reverse()
                RG2.insert(len(RG2), 0)
                microoperations.append("RG2:= RG2 + not(RG1) + 1")
                microoperations.append("RG3:= l(RG3).(RGA)")
                microoperations.append("RG2:= l(RG2).0")
            make_records(k, RG1, RG2, RG3, microoperations, on=operation_number)
        mantis_of_operation = RG3[1:number_of_digits + 1]

    elif operation_number == 5:
        RG1 = list()
        RG1.extend([0])
        RG1.extend(mantis_y_in_list)
        RG1.extend([0 for i in range(number_of_digits)])
        RG2 = list()
        RG2.extend([0])
        RG2.extend(mantis_x_in_list)
        RG2.extend([0 for i in range(number_of_digits)])
        RG3 = list()
        RG3.extend([1 for i in range(number_of_digits + 1)])
        k = 0
        microoperations = list()
        microoperations.append("RG3:= {0}".format(RG3))
        microoperations.append("RG1:= {0}".format(RG1))
        microoperations.append("RG2:= {0}".format(RG2))
        make_records(k, RG1, RG2, RG3, microoperations, on=operation_number)
        while RG3[0] == 1:
            k += 1
            microoperations = list()
            if RG2[0] == 1:
                make_records("", "", RG1, "", "", "", on=operation_number)
                RG2 = sumator.use_only_sumator_core(2 * number_of_digits + 1, RG1, RG2)
                make_records("", "", RG2, "", "", "", on=operation_number)
                RG1.pop()
                RG1.insert(0, 0)
                RG3.reverse()
                RG3.pop()
                RG3.reverse()
                RG3.insert(len(RG3), sumator.transposition)
                microoperations.append("RG2:= RG2 + RG1")
                microoperations.append("RG1:= 0.r(RG1)")
                microoperations.append("RG3:= l(RG3).SM(p)")
            elif RG2[0] == 0:
                addRG = list()
                addRG.extend(RG1)
                sumator.mok_transform([1], addRG)
                list_with_one = [0 for i in range(2 * number_of_digits)]
                list_with_one.append(1)
                addRG = sumator.use_only_sumator_core(2 * number_of_digits + 1, addRG, list_with_one)
                make_records("", "", addRG, "", "", "", on=operation_number)
                RG2 = sumator.use_only_sumator_core(2 * number_of_digits + 1, RG2, addRG)
                make_records("", "", RG2, "", "", "", on=operation_number)
                RG1.pop()
                RG1.insert(0, 0)
                RG3.reverse()
                RG3.pop()
                RG3.reverse()
                RG3.insert(len(RG3), sumator.transposition)
                microoperations.append("RG2:= RG2 + not(RG1) + not(RG2[1])")
                microoperations.append("RG1:= 0.r(RG1)")
                microoperations.append("RG3:= l(RG3).SM(p)")
            make_records(k, RG1, RG2, RG3, microoperations, on=operation_number)
        mantis_of_operation = RG3[1:number_of_digits + 1]
    save_results_in_buffer(operation_number, order_of_operation, sign_of_operation, mantis_of_operation)
