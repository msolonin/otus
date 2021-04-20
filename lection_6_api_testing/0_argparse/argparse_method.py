import argparse

# First, create parser object/class
parser = argparse.ArgumentParser()

# Second, define arguments
parser.add_argument('--method', '-m',
                    action='store',
                    help='Method to make request',
                    default='GET',
                    type=str,
                    choices=['GET', 'POST'])

parser.add_argument('--url', '-u',
                    # action='store',
                    type=str,
                    help='Url to make request',
                    required=False)

parser.add_argument('--secure', '-s',
                    action='store_false',
                    help='True or False param',
                    required=False)

# Parse passer arguments to args variable
args = parser.parse_args()

# Lets see the content
print("All params available:", args)

print(f"""
Arguments passed to script:
-m (--method) = {args.method}
-u (--url) = {args.url}
-s (--secure) = {args.secure}
""")

# python argparse_method.py -u localhost

# import os
# print("======  ENV VARS FOOBAR FROM OS  =======")
# print(os.getenv("FOOBAR", None))
