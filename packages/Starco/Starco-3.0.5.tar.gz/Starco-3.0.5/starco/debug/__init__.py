import sys,os
import traceback
from datetime import datetime
from..utils.directories import path_maker

class Debug:
    def __init__(self,debug_mode=True,relative_path='',log_name='log') -> None:
        self.debug_mode = debug_mode
        self.relative_path= relative_path
        self.log_name =log_name
    def debug(self,error):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        pm = datetime.now().strftime("%H:%M") + f" , {fname}:{exc_tb.tb_lineno} => "
        try:
            if not isinstance(error,str):
                err= traceback.format_exc()
                errl = err.split('\n')
                err_msg = '\n\t'.join(errl[1:])
                pm+='\n'+err_msg
            else:
                error = str(error)
                pm+='\t'+error
            with open(path_maker([],self.relative_path)+'/'+self.log_name,'a+') as f:
                f.write(pm+'\n\n')
                if self.debug_mode:
                    print(pm)

        except:pass
