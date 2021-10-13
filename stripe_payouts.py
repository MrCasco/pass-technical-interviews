import datetime as dt

def get_next_date(date, holidays):
    year, month, day = date.split('-')
    cur_date = dt.datetime(int(year), int(month), int(day))
    str_cur_date = cur_date.strftime('%Y-%m-%d')

    while str_cur_date in holidays:
        cur_date += dt.timedelta(days=1)
        str_cur_date = cur_date.strftime('%Y-%m-%d')
    return str_cur_date

def process_payouts(holidays, payouts):
    processed_payouts = {}
    for payout in payouts:
        next_date = payout['date']
        if payout['date'] in holidays:
            next_date = get_next_date(payout['date'], holidays)
        if next_date in processed_payouts:
            processed_payouts[next_date] += payout['amount']
        else:
            processed_payouts[next_date] = payout['amount']
    return processed_payouts

holidays = ['2021-01-01', '2021-12-25', '2021-12-31', '2022-01-01', '2022-01-02', '2022-01-03']
payouts = [{"amount": 500, "date": '2021-12-07'}, {"amount": 500, "date": '2021-12-25'}, {"amount": 500, "date": '2021-12-31'}, {"amount": 500, "date": '2021-12-31'}]
print(process_payouts(holidays, payouts))
