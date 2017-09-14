from datetime import datetime
from flask import flash, request, url_for
from threading import Thread


def flash_errors(form, category='danger'):
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                u'%s - %s' % (getattr(form, field).label.text, error),
                category
            )


def url_for_other_page(remove_args=[], **kwargs):
    args = request.args.copy()
    remove_args = ['_pjax']
    for key in remove_args:
        if key in args.keys():
            args.pop(key)
    new_args = [x for x in kwargs.items()]
    for key, value in new_args:
        args[key] = value
    return url_for(request.endpoint, **args)


#https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-email-support
def run_as_thread(f):
    """Async decorator"""

    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def timeago(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime, timezone
    #now = datetime.now(timezone.utc)
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return f"{second_diff:.2f} seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return f"{second_diff/60:.2f} minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return f"{second_diff/3600:.2f} hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return f"{day_diff} days ago"
    if day_diff < 31:
        return f"{day_diff/7:.2f} weeks ago"
    if day_diff < 365:
        return f"{day_diff/30:.2f} months ago"
    return f"{day_diff/365:.2f} years ago"


