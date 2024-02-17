from .base import *
from time import time
class Conversation(Base):
    def __init__(self,role:list[Role],super_self, defulat_lang_code=0,languages:dict[str:int]={},*args, **kwargs) -> None:
        super().__init__(super_self,defulat_lang_code=defulat_lang_code,languages=languages,*args, **kwargs)
        self.element_name=None
        self.nodes:list[ConversationNode] =[]
        if not isinstance(role,list):
            role=[role]
        self.role=role

        self.init_setter()
        self.init_pagination()
        self.init_menu()
        self.init_closer()

    def closer(self,*args):
        self.delete_message(self.get_msg_id())
        return -1
    
    def not_fount(self,*args):
        not_fount_status = self.get_setting('not_fount_status')
        if not_fount_status and not_fount_status==1:
            self.send('not_fount',self.menu_keys)
        return -1
    ############### init_setter###################
    def init_setter(self):
        e = Node()
        e.filters = ~Filters.contact & IsReplied()
        e.callback = self.setter_entry
        self.node('setter',entry=[e])

    def setter_entry(self, *args):
        if (self.super_self.edit_mode) and (self.user('editor') == 1 or self.is_super_admin() or self.id in self.super_self.editors_id):
            try:
                self.setter()
            except Exception as e:
                self.debug.debug(e)
            return  -1

    ############### init_pagination###################

    def init_pagination(self):
        e1 = Node()
        e1.pattern = self.check_inline_keyboards('next_page:pagination',regex=True)
        e1.callback = self.pagination_entry

        e2 = Node()
        e2.pattern = self.check_inline_keyboards('back_page:pagination',regex=True)
        e2.callback = self.pagination_entry
        self.node('setter',entry=[e1,e2])

    def pagination_entry(self, *args):
        order = self.splited_query_data()[0]
        if 'pagination_iter' in self.context.user_data:
            if order == 'next_page':
                self.userdata('pagination_iter',
                              self.userdata('pagination_iter')+1)
            elif order == 'back_page':
                self.userdata('pagination_iter',
                              self.userdata('pagination_iter')-1)
            try:
                msg = self.pagination_msg_maker()
                btn = self.pagination_btn_maker()
                self.edit_message_text(new_msg=msg,message_id=self.get_msg_id(),btns=btn,chat_id=self.id,translat=False)
            except Exception as e:
                self.debug.debug(e)
                self.delete_message(self.get_msg_id())
        else:
            self.delete_message(self.get_msg_id())
        return -1
    ############### init_menu###################
    def init_menu(self):
        e = Node()
        e.filters = match_btn(self.back_menu_key,self)
        e.callback =self.menu
        self.node('menu',entry=[e])
    
    def init_closer(self):
        e = Node()
        e.pattern = self.check_inline_keyboards('close')
        e.callback =self.closer
        self.node('closer',entry=[e])

    
