from cval_lib.patterns.singleton import Singleton


class MainConfig(metaclass=Singleton):
    main_url = 'https://cval.ai/api'
