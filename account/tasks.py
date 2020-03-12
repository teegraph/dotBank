from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from account.models import Account


@shared_task()
def hold():
    try:
        models = Account.objects.filter(hold__gt=0).all()
    except ObjectDoesNotExist:
        return
    for model in models:
        if not model.status:
            continue
        if model.balance >= model.hold:
            model.balance = model.balance - model.hold
            model.hold = 0
            model.save()
