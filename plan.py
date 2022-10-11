import threading
def function1():
    print("function1")
def function2():
    print("function2")
def function3():
    print("function3")


predicted_function = "function1"
function_to_run = globals()[predicted_function]

functions_list = ["function1", "function2", "function3", "function4"]

if predicted_function in functions_list:
    t1 = threading.Thread(target=function_to_run).start()

        














