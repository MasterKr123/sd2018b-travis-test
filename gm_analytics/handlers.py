import logging

def get_user_info(username=None):
    logging.info('exec get_user_info')
    logging.debug('username=%s',username)
    return {"user_info": username}

def get_commits_info(username=None, time_range=None):
    logging.info('exec get_commits_info')
    logging.debug('username=%s',username)
    logging.debug('time_range=%s',time_range)
    return [{'commits_count': 10, 'yyyymmdd_date': '20180101'},
            {'commits_count': 10, 'yyyymmdd_date': '20180102'}]

def get_health():
    logging.info('service health')
    return {"message":"OK"}
