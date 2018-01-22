def get_casualtime(dt):
    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    WEEK = 7 * DAY
    from datetime import datetime
    import pytz

    now = datetime.utcnow()

    # convert both datetimes to aware
    if now.tzinfo is None:
        now = pytz.utc.localize(now)

    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)

    seconds = int((now - dt).total_seconds())

    if seconds < 0:
        raise ValueError('Your datetime object is in the future!')

    quotient = int(seconds / WEEK)

    if quotient > 1:
        if now.year == dt.year:
            return '{} {}'.format(dt.strftime("%B"), dt.day)
        else:
            return '{} {}, {}'.format(dt.strftime("%B"), dt.day, dt.year)
    elif quotient < 1:
        quotient = int(seconds / DAY)

        if quotient < 1:
            quotient = int(seconds / HOUR)

            if quotient < 1:
                quotient = int(seconds / MINUTE)

                if quotient < 1:
                    # difference is less than one minute
                    quotient = int(seconds / SECOND)

                    if quotient < 1:
                        # difference is less than one second
                        return 'now'
                    else:
                        # difference is one second or more
                        if quotient == 1:
                            return 'one second'
                        else:
                            return '{} seconds'.format(quotient)
                else:
                    # difference is one minute or more
                    if quotient == 1:
                        return 'one minute'
                    else:
                        return '{} minutes'.format(quotient)
            else:
                # difference is one hour or more
                if quotient == 1:
                    return 'one hour'
                else:
                    return '{} hours'.format(quotient)
        else:
            # difference is one day or more
            if quotient == 1:
                return 'one day'
            else:
                return '{} days'.format(quotient)
    else:
        # difference is exactly one week
        return 'one week'
