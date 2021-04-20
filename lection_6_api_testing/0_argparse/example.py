"""Script for creating url based on script parameters"""
import argparse
import requests

parser = argparse.ArgumentParser()

parser.add_argument('--schema', '-s',
                    help='schema',
                    type=str,
                    default='https',
                    choices=['http', 'https'])

parser.add_argument('--domain', '-d',
                    help='domain',
                    type=str,
                    default="localhost")

parser.add_argument('--path', '-p',
                    default='/',
                    type=str,
                    help='Path to make request on host',
                    required=False)


def url_maker(schema, host, path):
    url = schema + "://" + host + path
    # print(f"Created url: {url}")
    return url


args = parser.parse_args()

print(url_maker(args.schema, args.domain, args.path))
response = requests.get(url=url_maker(args.schema, args.domain, args.path))

print("Got response status code:", response.status_code)

# python example.py -d google.com -p /search?q=new
# python example.py --domain google.com
