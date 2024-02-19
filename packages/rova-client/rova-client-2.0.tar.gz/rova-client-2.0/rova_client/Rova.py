import clickhouse_connect
from rova_client.utils import SessionTracker, TraceTracker, DateTracker

class Rova:

    def __init__(self, auth, timeout=1440):
        
        self.accounts = ['buster_dev']

        if(not self.check_auth(auth)):
            raise Exception("Invalid key!")
        else:
            self.client = clickhouse_connect.get_client(host='tbbhwu2ql2.us-east-2.aws.clickhouse.cloud', port=8443, username='default', password='V8fBb2R_ZmW4i')
            template = 'USE {}'.format(auth)
            self.client.command(template)
            self.auth = auth
            print("Key verified! You may begin using the client. ")

        # init clients
        self.session_client = SessionTracker(timeout)
        self.trace_client = TraceTracker()
        self.date_client = DateTracker()

    def check_auth(self, auth):
        return (auth in self.accounts)


    def log_product(self, args: dict):

        if not isinstance(args, dict):
            raise TypeError("Argument 'args' must be a dictionary")

        # Check if 'name' and 'price' keys are present in the dictionary
        required_keys = {'event_name', 'user_id', 'data_source_id', 'session_id', 'trace_id'}
        if('timestamp' not in args):
            args['timestamp'] = self.date_client.get_timestamp()
        
        args['session_id'] = self.session_client.get_session_id(args['user_id'], args['timestamp'])
        args['trace_id'] = self.trace_client.get_trace_id(args['user_id'], args['session_id'], 'product')

        if not required_keys.issubset(args.keys()):
            missing_keys = required_keys - set(args.keys())
            raise ValueError(f"Missing required data: {missing_keys}")
        try:
            columns, values = zip(*args.items())
            data = [values]
            db = "{}.product".format(self.auth)
            self.client.insert(db, data, column_names=columns)
            self.trace_client.set_prev_log(args['user_id'], 'product')
            return 0

        except Exception as e:
            print(e)
            return -1

    def log_llm(self, args: dict):

        if not isinstance(args, dict):
            raise TypeError("Argument 'args' must be a dictionary")

        required_keys = {'event_name', 'user_id', 'data_source_id', 'input_content',
                         'output_content', 'llm_in_use', 'input_token_count',  'output_token_count', 'trace_id',
                         'cost', 'time_to_first_token', 'latency', 'error_status', 'chat_id', 'session_id'}

        if('timestamp' not in args):
            args['timestamp'] = self.date_client.get_timestamp()

        args['session_id'] = self.session_client.get_session_id(args['user_id'], args['timestamp'])
        args['trace_id'] = self.trace_client.get_trace_id(args['user_id'], args['session_id'], 'llm')

        if not required_keys.issubset(args.keys()):
            missing_keys = required_keys - set(args.keys())
            raise ValueError(f"Missing required data: {missing_keys}")

        try:
            columns, values = zip(*args.items())
            data = [values]
            db = "{}.llm".format(self.auth)
            self.client.insert(db, data, column_names=columns)
            self.trace_client.set_prev_log(args['user_id'], 'llm')
            return 0

        except Exception as e:
            print(e)
            return -1