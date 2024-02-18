import clickhouse_connect
from dist_alx.util import timestamp

class RovaClient():
    
    def __init__(self, key):
        self.verified = False
        self.accounts = ['buster_dev']
        if(not self.check_key(key)):
            raise Exception("Invalid key!")
        else:
            print("Key verified! You may begin using the client. ")
            self.client = clickhouse_connect.get_client(host='tbbhwu2ql2.us-east-2.aws.clickhouse.cloud', port=8443, username='default', password='V8fBb2R_ZmW4i')
            template = 'USE {}'
            self.client.command(template.format(key))
            self.key = True


    def check_key(self, key):
        return (key in self.accounts)
    
    def log_product(self, args: dict):
        # Check if 'name' and 'price' keys are present in the dictionary
        required_keys = {'event_name', 'user_id', 'data_source_id'}
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
    