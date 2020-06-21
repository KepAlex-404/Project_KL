import sumator, memory_buffer


def calculate(operation_number, order_x, order_y, sign_x, sign_y, mantis_x, mantis_y):
    """All variables must have type string."""
    operation_number = int(operation_number)
    memory_buffer.clear_operation(operation_number)
    order_of_operation = list()
    mantis_of_operation = list()
    maximum_number_for_counter = max(len(mantis_x), len(mantis_y)) + 1
    code_table = {}
    for number in range(maximum_number_for_counter):
        code_table[number] = str(bin(number))[2:]
    normal_length_for_counter = len(code_table[maximum_number_for_counter - 1])
    for key in code_table.keys():
        line_for_transform = code_table[key]
        while len(line_for_transform) < normal_length_for_counter:
            line_for_transform = "0" + line_for_transform
        code_table[key] = line_for_transform

    def type_converter(arg_list, type_flag):
        for number in range(len(arg_list)):
            arg_list[number] = type_flag(arg_list[number])

    def record_corector(arg_list):
        return ''.join(str(arg_list).replace('[', '').replace(']', '').replace(', ', '').replace(',', '').replace("'", ''))

    def make_records(counter, rg1, rg2, rg3, mo, ct=None):
        tact_line = list()
        tact_line.append(str(counter))
        tact_line.append(record_corector(rg1))
        tact_line.append(record_corector(rg2))
        tact_line.append(record_corector(rg3))
        if ct is not None:
            tact_line.append(ct)
        tact_line.append(record_corector(mo))
        memory_buffer.write_one_line(operation_number, tact_line)

    order_x_in_list = list(order_x)
    order_y_in_list = list(order_y)
    mantis_x_in_list = list(mantis_x)
    mantis_y_in_list = list(mantis_y)
    type_converter(order_x_in_list, int)
    type_converter(order_y_in_list, int)
    type_converter(mantis_x_in_list, int)
    type_converter(mantis_y_in_list, int)
    sumator.full_addition_procedure(order_x_in_list, order_y_in_list)
    order_of_operation.extend(sumator.sumator_answer)
    sign_x_in_list = list(sign_x)
    sign_y_in_list = list(sign_y)
    type_converter(sign_x_in_list, int)
    type_converter(sign_y_in_list, int)
    sign_of_operation = sumator.use_only_sumator_core(1, sign_x_in_list, sign_y_in_list)

    if operation_number == 0:
        RG1 = [0, 0, 0, 0, 0, 0, 0]
        RG2 = list()
        RG3 = [0]
        addRG = list()
        RG2.extend(mantis_x_in_list)
        RG3.extend(mantis_y_in_list)
        CT = code_table[6]
        CT_count = 6
        k = 0
        microoperations = list()
        microoperations.append("RG1:= {0}".format(RG1))
        microoperations.append("RG2:= {0}".format(RG2))
        microoperations.append("RG3:= {0}".format(RG3))
        microoperations.append("CT:= {0}".format(CT))
        make_records(k, RG1, RG2, RG3, microoperations, code_table[CT_count])
        while CT_count != 0:
            k += 1
            microoperations = list()
            if RG2[5] == 1:
                print("  {0}         {1}{2}".format(k, RG3, "(Доданок)"))
                RG1 = sumator.use_only_sumator_core(7, RG1, RG3)
                print("  {0}         {1}{2}".format(" ", RG1, "(Сума)"))
                microoperations.append("RG1: = RG1 + RG3")
            RG2.insert(0, RG1[6])
            RG2.pop()
            RG1.insert(0, 0)
            RG1.pop()
            CT_count -= 1
            microoperations.append("RG2: = RG1[7].r(RG2)")
            microoperations.append("RG1: = 0.r(RG1)")
            microoperations.append("CT = CT-1")
            if CT_count == 0:
                microoperations.append("CT = 0")
            make_records(k, RG1, RG2, RG3, microoperations, code_table[CT_count])
        RG1.extend(RG2)
        mantis_of_operation = RG1[1:13]

    elif operation_number == 1:
        RG1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        RG2 = list()
        RG3 = [0, 0, 0, 0, 0, 0]
        RG2.extend(mantis_x_in_list)
        RG3.extend(mantis_y_in_list)
        k = 0
        microoperations = list()
        microoperations.append("RG1:= {0}".format(RG1))
        microoperations.append("RG2:= {0}".format(RG2))
        microoperations.append("RG3:= {0}".format(RG3))
        make_records(k, RG1, RG2, RG3, microoperations)
        while sum(RG2) != 0:
            k += 1
            microoperations = list()
            if RG2[5] == 1:
                print("  {0}         {1}(Доданок)".format(k, RG3))
                RG1 = sumator.use_only_sumator_core(12, RG1, RG3)
                print("            {0}(Сума)".format(RG1))
                microoperations.append("RG1: = RG1 + RG3")
            RG3.reverse()
            RG3.pop()
            RG3.reverse()
            RG3.insert(len(RG3), 0)
            RG2.pop()
            RG2.insert(0, 0)
            microoperations.append("RG3: = l(RG3).0")
            microoperations.append("RG2: = 0.r(RG2)")
            make_records(k, RG1, RG2, RG3, microoperations)
        mantis_of_operation.extend(RG1)

    elif operation_number == 2:
        RG1 = [0, 0, 0, 0, 0, 0]
        RG2 = list()
        RG2.extend(mantis_x_in_list)
        RG2.append(0)
        RG3 = list()
        RG3.extend(mantis_y_in_list)
        CT = 6
        second_number = list()
        second_number.extend([0, 0, 0, 0, 0, 0, 0])
        second_number.extend(RG3)
        k = 0
        microoperations = list()
        microoperations.append("RG1: ={0}".format(RG1))
        microoperations.append("RG2: ={0}".format(RG2))
        microoperations.append("RG3: ={0}".format(RG3))
        microoperations.append("CT: ={0}".format(code_table[CT]))
        make_records(k, RG1, RG2, RG3, microoperations, code_table[CT])
        while CT != 0:
            k += 1
            microoperations = list()
            first_number = list()
            first_number.extend(RG2)
            first_number.extend(RG1)
            suma_list = list()
            suma_list.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            if RG2[0] == 1:
                suma_list = sumator.use_only_sumator_core(13, first_number, second_number)
                print("  {0}         {1}(Доданок)".format(k, RG3))
                RG2 = suma_list[0:7]
                RG1 = suma_list[7:13]
                print("  {0}         {1}(Сума)  {2}(Сума)".format(" ", RG1, RG2))
                microoperations.append("RG1: = RG1 + RG3")
                microoperations.append("RG2: = RG2 + 0 + CI")
            RG1.reverse()
            CI = RG1.pop()
            RG1.reverse()
            RG1.insert(len(RG1), 0)
            RG2.reverse()
            RG2.pop()
            RG2.reverse()
            RG2.insert(len(RG2), CI)
            CT -= 1
            microoperations.append("RG1: = l(RG1).0")
            microoperations.append("RG2: = l(RG2).RG1[1]")
            microoperations.append("CT: = CT - 1")
            if CT == 0:
                microoperations.append("CT = 0")
            make_records(k, RG1, RG2, RG3, microoperations, code_table[CT])
        RG2.extend(RG1)
        mantis_of_operation.extend(RG2[0:12])

    elif operation_number == 3:
        RG1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        RG2 = list()
        RG2.extend(mantis_y_in_list)
        RG3 = list()
        RG3.append(0)
        RG3.extend(mantis_x_in_list)
        RG3.extend([0, 0, 0, 0, 0])
        k = 0
        microoperations = list()
        microoperations.append("RG1: ={0}".format(RG1))
        microoperations.append("RG2: ={0}".format(RG2))
        microoperations.append("RG3: ={0}".format(RG3))
        make_records(k, RG1, RG2, RG3, microoperations)
        while sum(RG2) != 0:
            k += 1
            microoperations = list()
            if RG2[0] == 1:
                print("  {0}         {1}{2}".format(k, RG3, "(Доданок)"))
                RG1 = sumator.use_only_sumator_core(12, RG1, RG3)
                print("  {0}         {1}{2}".format(" ", RG1, "(Сума)"))
                microoperations.append("RG1: = RG1 + RG3")
            RG3.insert(0, 0)
            RG3.pop()
            RG2.reverse()
            RG2.pop()
            RG2.reverse()
            RG2.insert(len(RG2), 0)
            microoperations.append("RG3: = 0.r(RG3)")
            microoperations.append("RG2: = l(RG2).0")
            make_records(k, RG1, RG2, RG3, microoperations)
        mantis_of_operation.extend(RG1)

    memory_buffer.write_answer(operation_number, sign_of_operation, mantis_of_operation)
    memory_buffer.write_order(operation_number, order_of_operation)
