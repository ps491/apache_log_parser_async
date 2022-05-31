from database.connector import db_connector


# @db_connector
from parse.re_log import re_logs_to_dict


async def parse_logs(log_string):
    result = await re_logs_to_dict(log_string)
    print(result)
    return False
