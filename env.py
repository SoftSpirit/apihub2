SERVER_PORT = 8000
URL_PREFIX = 'apis2'
session_cookie_name = 'apihub2'  ##建议和前端项目共享约定的词 django 会默认加上前缀 ':1:django.contrib.sessions.cache'
redis_db_id = 3  # 默认的redis db index
redis_db_port = 6379  # 默认的redis db port
pg_port = '5432'
pg_name = 'apihub2'
pg_host = 'pg12'
redis_db_ip = 'redis'
redis_db_pwd = 'Vs5588'
rabbitmq_host = 'rabbitmq'
pg_user = 'postgres'
pg_pwd = '123456'
ext_apps = []

skylark_upload_url = 'https://up.qbox.me/'
data_pg_name = 'apihub2_data'

ssl_verify = False