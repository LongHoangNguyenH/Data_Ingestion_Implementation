import sys

def Get_error_Message(error, error_details:sys):
    _,_,exc = error_details.exc_info()#take traceback object
    file_name_error = exc.tb_frame.f_code.co_filename  #take file name error
    Error_Message = "Error occur in python script name [{0} line number [{1}]] error message [{2}]".format(file_name_error,exc.tb_lineno,str(error))
    return Error_Message

class CustomException(Exception):
    def __init__(self, message_error, error_details:sys):
        super().__init__(message_error)
        self.Error_Message = Get_error_Message(message_error,error_details)

    def __str__(self):
        return self.Error_Message