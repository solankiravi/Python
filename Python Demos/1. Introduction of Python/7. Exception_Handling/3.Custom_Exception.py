import traceback
class VALRANGEERROR(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
        
def isvalid_input(val):
    try:
        if(val > 0 and val <= 10):   
            print('input is valid')
        else:
            raise VALRANGEERROR("Input is not in range")
    except ValueError as ex:
        print(f"Value Error - {ex}")
    except VALRANGEERROR as ex:
        val = 1/0
    except ZeroDivisionError:
        print("Division by Zero error")
    except Exception as ex:
        # traceback.print_exc()
        print(ex)

isvalid_input(0)
#isvalid_input('a')
