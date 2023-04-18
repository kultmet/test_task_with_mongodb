# test_task_with_mongodb
This test task  to demonstrate skills in working with mongoDB and asynchronous telegram bot libraries.

## How to start
With command <code>cd yor_derectory</code> go to your directory

clone the project

```
git clone https://github.com/kultmet/test_task_with_mongodb.git
```
Type this in the command shell.

```
python -m venv venv
sourse venv/Scripts/activate
```
next

```
pip install -r requiremants.txt
```

create <code>.env</code> file and add your and token
```
touch .env
echo API_TOKEN=your_token >> .env
```
and run

```
python telegram_bot.py
```
and enjoy

## Use case

Let's follow the link https://t.me/KazbackAggrigationBot

Press /start
and feed the bot with this request
```
{
"dt_from": "2022-09-01T00:00:00",
"dt_upto": "2022-12-31T23:59:00",
"group_type": "month"
}
```
and he reverently returns to us
```
{"dataset": [5906586, 5515874, 5889803, 6092634], "labels": ["2022-09-01T00:00:00", "2022-10-01T00:00:00", "2022-11-01T00:00:00", "2022-12-01T00:00:00"]}
```
result of aggregation, salaries of employees, for a certain period.

<code>"group_type" can have values, - year, month, day, hour.</code>

thanks for watching
