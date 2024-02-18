import clickhouse_connect
from rova_client.util import timestamp
from rova_client.util import UniqueIDGenerator

class RovaClient():

    def __init__(self, key, timeout=1800):
        self.verified = False
        self.accounts = ['buster_dev']
        if(not self.check_key(key)):
            raise Exception("Invalid key!")
        else:
            self.client = clickhouse_connect.get_client(host='tbbhwu2ql2.us-east-2.aws.clickhouse.cloud', port=8443, username='default', password='V8fBb2R_ZmW4i')
            template = 'USE {}'.format(key)
            self.client.command(template)
            self.key = True
            print("Key verified! You may begin using the client. ")
        self.last_times = dict()
        self.timeout = timeout
        # Example usage
        self.generator = UniqueIDGenerator()


    def check_key(self, key):
        return (key in self.accounts)
    
    def get_session_id(self, user_id, timestamp):
        if(user_id not in self.last_times):
            session_id = self.generator.get_unique_id()
            self.last_session_ids[user_id] = session_id
            self.last_times[user_id] = timestamp
            return session_id
        elif(timestamp - self.last_times[user_id] > self.timeout):
            self.last_times[user_id] = timestamp
            session_id = self.generator.get_unique_id()
            self.last_session_ids[user_id] = session_id
            return session_id
        else:
            return self.last_session_ids[user_id]
    
    def log_product(self, args: dict):
        # Check if 'name' and 'price' keys are present in the dictionary
        required_keys = {'event_name', 'user_id', 'data_source_id'}
        if('timestamp' not in args):
            args['timestamp'] = timestamp()
        if('session_id' not in args):
            args['session_id'] = self.get_session_id(args['user_id'], args['timestamp'])
        if not isinstance(args, dict):
            raise TypeError("Argument 'args' must be a dictionary")

        if not required_keys.issubset(args.keys()):
            missing_keys = required_keys - set(args.keys())
            raise ValueError(f"Missing required data: {missing_keys}")
        try:
            columns, values = zip(*args.items())
            data = [values]
            self.client.insert("product", data, column_names=columns)
            return 0
        
        except Exception as e:
            print(e)
            return -1
    
    def log_llm(self, args: dict):
        required_keys = {'event_name', 'user_id', 'data_source_id', 'input_content', 
                         'output_content', 'llm_in_use', 'input_token_count',  'output_token_count',
                         'cost', 'time_to_first_token', 'latency', 'error_status', 'chat_id'}
        if('timestamp' not in args):
            args['timestamp'] = timestamp()
        if not isinstance(args, dict):
            raise TypeError("Argument 'args' must be a dictionary")

        if not required_keys.issubset(args.keys()):
            missing_keys = required_keys - set(args.keys())
            raise ValueError(f"Missing required data: {missing_keys}")
        
        try:
            columns, values = zip(*args.items())
            data = [values]
            self.client.insert("product", data, column_names=columns)
            return 0
        
        except Exception as e:
            print(e)
            return -1