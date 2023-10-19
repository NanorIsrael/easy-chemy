import os
from dotenv import load_dotenv
load_dotenv()
# print(os.getenv('HW'))

args = "\"the quoted string\""

# res = args.find('\"', 1)

print(os.environ.get('HW'))
# print(args[18] )
# print(res )