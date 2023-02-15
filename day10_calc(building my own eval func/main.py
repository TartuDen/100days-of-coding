# the task is to creat interactive calculator


def eval_analogue(inp):
    print("Input is: ", inp)

    def simpl_op(a, sign, b):
        """a func for simple math op."""
        a = float(a)
        b = float(b)
        if sign == "*":
            return (a * b)
        elif sign == "/":
            return (a / b)
        elif sign == "+":
            return (a + b)
        elif sign == "-":
            return (a - b)

    def list_it(n):
        """turns str input into list"""
        operators = ["=", "+", "-", "*", "/", "^", "(", ")"]
        list_ = []
        temp_num = ""
        for ch in inp:
            if ch in operators:
                list_.append(temp_num)
                list_.append(ch)
                temp_num = ""
            elif ch.isdigit():
                temp_num += ch
        if temp_num:
            list_.append(temp_num)
        return (list_)

    def logic(t_list):
        """this func runs itself as long as there are math operations in the list. It checks what math op are and calls for them func simpl_op and creates another shorter list with obtained result """

        if len(t_list) > 1:
            if "*" in t_list or "/" in t_list:
                list_temp = []
                if "*" in t_list:
                    idx = t_list.index("*")
                else:
                    idx = t_list.index("/")
                idx_left = idx - 1
                idx_right = idx + 1
                res = simpl_op(t_list[idx - 1], t_list[idx], t_list[idx + 1])
                for ix, i in enumerate(t_list):
                    if ix != idx and ix != idx_left and ix != idx_right:
                        list_temp.append(i)
                    elif ix == idx_left:
                        list_temp.append(res)
                logic(list_temp)

            elif "-" in t_list or "+" in t_list:
                list_temp = []
                if "-" in t_list:
                    idx = t_list.index("-")
                else:
                    idx = t_list.index("+")
                idx_left = idx - 1
                idx_right = idx + 1
                res = simpl_op(t_list[idx - 1], t_list[idx], t_list[idx + 1])
                for ix, i in enumerate(t_list):
                    if ix != idx and ix != idx_left and ix != idx_right:
                        list_temp.append(i)
                    elif ix == idx_left:
                        list_temp.append(res)
                logic(list_temp)
        else:
            print("equalst to: ", t_list[0])
            return (t_list)

    logic(list_it(inp))


def get_input():
    """a funct. to get input and start the whole script"""
    # inp_str=input("type your equation: \n")
    # return(eval_analogue(inp_str))
    to_solve = "10+2 - 3 * 2 / 5"
    print("check: ", eval(to_solve)
          )  #here to check obtained result against original eval function
    return (eval_analogue(to_solve))


get_input()
