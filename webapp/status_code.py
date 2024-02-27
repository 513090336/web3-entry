class STATUS:
    SUCCESS = 0

    DB_COMMON_ERROR = 10001
    DB_CREATE_ERROR = 10002
    DB_DELETE_ERROR = 10003
    DB_UPDATE_ERROR = 10004
    DB_QUERY_ERROR = 10005

    AUTH_COMMON = 20001

    PARAM_COMMON_ERROR = 30001
    PARAM_TYPE_ERROR = 30002
    PARAM_MISSING_ERROR = 30003
    PARAM_JSON_ERROR = 30004

    CODE_FREEZE = 50003
    TASK_DELETE_ERROR = 50004

    MANUAL_TYPE_ERROR = 60000
    NO_TRADE_TIME = 60001
    UN_SUPPORT_POSITION_MODE = 60002
    NO_ENOUGH_AVAILABLE_POSITION = 60003
    NO_ENOUGH_AVAILABLE_AMOUNT = 60004

    BEFORE_RISK_CONTROL_SUCCESS = 70000
    BLACK_LIST_FAILED = 70001
    WHITE_LIST_FAILED = 70002
    TIME_ALLOW_FAILED = 70003
    NOT_ALLOW_BY_SAME_CODE_FAILED = 70004
    MARKET_RISK_CONTROL_FAILED = 70005
    DURING_MONITOR_SUCCESS = 71000
