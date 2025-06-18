import requests
import argparse

def give_me_facts():
    """
    Fetches a random Chuck Norris fact from the Chuck Norris API.
    
    Returns:
        str: A random Chuck Norris fact
    """
    response = requests.get('https://api.chucknorris.io/jokes/random')
    if response.status_code == 200:
        return response.json()['value']
    else:
        raise Exception(f"Failed to fetch fact. Status code: {response.status_code}")

def main():
    """
    Command-line interface for the Chuck Norris facts package.
    """
    parser = argparse.ArgumentParser(description='Get random Chuck Norris facts')
    parser.add_argument('-n', '--number', type=int, default=1,
                      help='Number of facts to display (default: 1)')
    
    args = parser.parse_args()
    
    try:
        for _ in range(args.number):
            print(give_me_facts())
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == '__main__':
    main() 