from telegram.utils.request import Request
from telegram.ext import Updater, Filters
from telegram.ext import MessageHandler, ConversationHandler
import json
from threading import Thread
from .util.filteres import RoleFilter
from .classes import Base, Conversation
from .util.enum import ConversationNode
from ...utils.scheduler import Scheduler
from telegram import Bot, Update
from starco.debug import Debug
from starco.db import DB


class TlgBot:
    def __init__(
        self, token: str, super_admin: int,
            db_config: dict[dict] = {},
            db_tables_need_init: dict[dict] = {},
            webhook_url: str = None, port: int = 443,
            ssl_key_path: str = None, ssl_cert_path: str = None,
            db_relative_path: str = '.', debug_relative_path: str = '.',
            debug_mode=False, host_id: str = None,
            proxy=None, scheduler_status: bool = True,
            edit_mode: bool = False,
            editors_id:list=[],
            respond_bad_order=True,
    ) -> None:
        '''
        '''
        self.token = token
        self.respond_bad_order=respond_bad_order
        self.edit_mode = edit_mode
        self.editors_id=editors_id
        
        self.super_admin = super_admin
        self.webhook_url = webhook_url
        self.port = port
        self.ssl_key_path = ssl_key_path
        self.ssl_cert_path = ssl_cert_path
        self.host_id = host_id
        self.db_relative_path = db_relative_path
        self.db_type = 'sqlite'
        self.debug_relative_path = debug_relative_path
        self.debug_mode = debug_mode
        self.debug = Debug(debug_mode=debug_mode,
                           relative_path=debug_relative_path)
        request_kwargs = None
        if proxy:
            self.bot = Bot(self.token, request=Request(proxy_url=proxy))
            request_kwargs = {'proxy_url': proxy}
        else:
            self.bot = Bot(self.token)
        
        self.updater = Updater(self.token, use_context=True,
                               request_kwargs=request_kwargs)
        self.dp = self.updater.dispatcher
        self.bot_username = self.dp.bot.get_me().username
        
        self.db_config = db_config
        self.db_tables_need_init = db_tables_need_init
        self.init_db()
        self.scheduler_status = scheduler_status
        self.scheduler = Scheduler(self)

    def init_db(self):
        self.forced_tables_init()
        self.db = DB(self.db_config, relative_path=self.db_relative_path,
                     debug_mode=self.debug_mode, debug_relative_path=self.debug_relative_path)
        self.need_init_tables()
        self.settings_subset_update()

    def forced_tables_init(self):
        users_cfg = {'id': 0, 'name': '', 'last_name': '', 'username': '', 'role': 0, 'editor': 0,
                     'status': 0, 'phone': 0, 'language': 0, 'get_alarm': 0, 'is_online': 0, 'time': 0, 'last_seen': 0}
        setting_cfg = {'key': '', 'value': '',
                       'unit': '', 'type': '', 'subset': '','hide':0,'toggle':0}
        texts_cfg = {'id': 0, 'key': '', 'value': '', 'language': 0, 'role': 0}
        media_cfg = {'id': 0, 'key': '', 'msg_id': '',
                     'channel_id': '', 'language': 0, 'role': 0}

        def check(table_name, cfg):
            if table_name not in self.db_config:
                self.db_config[table_name] = cfg
            else:
                for k, v in cfg.items():
                    if k not in self.db_config[table_name]:
                        self.db_config[table_name][k] = v
        check('users', users_cfg)
        check('setting', setting_cfg)
        check('texts', texts_cfg)
        check('media', media_cfg)

    def need_init_tables(self):
        tables_data = self.db_tables_need_init
        defulat_setting = {}
        setting = {**tables_data.get('setting', {}), **defulat_setting}
        tables_data['setting'] = setting
        if tables_data:

            for table in tables_data:
                res = self.db.do(table)
                keys = [i['key'] for i in res]
                for k, v in tables_data[table].items():
                    if k not in keys:
                        self.db.do(table, {**{'key': k}, **v})

                tables_in_db = self.db.do(table)
                keys = [i['key'] for i in tables_in_db]
                must_be_remove = list(
                    set(keys) - set(tables_data[table].keys()))
                for k in must_be_remove:
                    self.db.do(table, condition=f"key='{k}'", delete=True)

    def settings_subset_update(self):
        tables_data = self.db_tables_need_init
        setting_init = tables_data.get('setting', {})
        if setting_init:
            for key in setting_init:
                sub = setting_init[key]['subset']
                hide = setting_init[key]['hide']
                toggle = setting_init[key]['toggle']
                self.db.do('setting', {'subset': sub,'hide': hide,'toggle': toggle},
                           condition=f"key='{key}'")

    def add(self, class_item: Base):

        if class_item.type == 'Conversation':
            item: Conversation = class_item
            for node in item.nodes:
                node: ConversationNode = node
                self.dp.add_handler(ConversationHandler(
                    entry_points=node.entries,
                    states=node.states,
                    fallbacks=node.fallbacks,
                    allow_reentry=node.arges.get('allow_reentry', True),
                    **node.arges
                ))
            if self.respond_bad_order:
                self.dp.add_handler(MessageHandler(
                    Filters.all & RoleFilter(item) , item.add_method(item.not_fount)))

    def add_schedual_action(self,func,run_evry_sec:int,first_run=False):
        self.scheduler.add(func=func,run_evry_sec=run_evry_sec,first_run=first_run)

    def befor_run_action(self):
        self.init_db()
        if self.scheduler_status:
            Thread(target=self.scheduler.run).start()

    def init_webhook(self):
        self.bot.deleteWebhook()
        print(self.bot_username)
        self.befor_run_action()

        webhook_url = self.webhook_url
        if self.port not in [443, 80]:
            webhook_url += f':{self.port}'
        webhook_url += f'/webhook/{self.token}'
        print(webhook_url)
        self.bot.setWebhook(webhook_url, max_connections=100)

    def run_poll(self):
        self.bot.deleteWebhook()
        print(self.bot_username)
        self.befor_run_action()
        self.updater.start_polling()
        self.updater.idle()

    def webhook(self, json_data):
        try:
            data = json.loads(json_data)
            update = Update.de_json(data, self.bot)
            self.dp.process_update(update)
        except Exception as e:
            print(e)
