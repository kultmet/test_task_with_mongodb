from dateutil.relativedelta import relativedelta

correct_format = (
    'Пример запроса:\n'
    '{\n"dt_from": "2022-09-01T00:00:00",\n"dt_upto": '
    '"2022-12-31T23:59:00",\n'
    '"group_type": "month"\n}'
)

FIELDS = ('dt_from', 'dt_upto', 'group_type')

year = {'$year': '$dt'}
month = {'$month': '$dt'}
day = {'$dayOfMonth': '$dt'}
hour = {'$hour': '$dt'}


GROUP_TIPES = {
    'year': {'year': year,},
    'month': {'year': year, 'month': month},
    'day': {'year': year, 'month': month, 'day': day},
    'hour': {'year': year, 'month': month, 'day': day, 'hour': hour},
}

periods = {
    'minute': relativedelta(minutes=1),
    'hour': relativedelta(hours=1),
    'day': relativedelta(days=1),
    'month': relativedelta(months=1),
    'year': relativedelta(years=1)

}