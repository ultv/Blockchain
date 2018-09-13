import json
import os

def write_block(name, amount, to_whom, prev_hash=''):

    blockchain_dir = os.curdir + '/blockchain/'

    data = {'name': name,
             'amount': amount,
             'to_whom': to_whom,
             'hash': prev_hash}

    with open(blockchain_dir + 'test', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block(name='ivan', amount=2, to_whom='semen')








if __name__ == '__main__':
    main()