
from .models import Product
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete

from django.dispatch import receiver

@receiver(pre_save, sender=Product)
def check_product_name_description(sender, instance, **kwargs):
    print(f' Pre Save Model Signals \nInstance data is: {instance}')

    if  not instance.name:
        print('Product name is blank')
    else:
        instance.name += ' System'
    
    if not instance.description:
        print('Product description can not blank')
    else:
        custom = "Go to the YouTube Studio. Choose the Settings option from the menu. Select the Upload defaults option. Fill out the description box."
        instance.description += custom

@receiver(post_save, sender=Product)
def created_products(instance, created, **kwargs):
    print(f'\n instance is Created {instance}')
    if created:
        print('\nCongrats! Product is inserted')

        print(f'{instance.name} {instance.description} ')
    else:
        print('Product is not inserted')

@receiver(pre_delete, sender=Product)
def product_deletion_confirmation(sender, instance, using, **kwargs):
   
    action = 'no'

    if 'yes' in action.lower():
        instance.delete()
        print('\nCongrats data deleted  ')
    else:
        print('\nOk will not delete product  ')

@receiver(post_delete, sender=Product)
def after_product_deletion(sender, instance, *args, **kwargs):
    print(f'\nSender is: {sender}')
    print(f'instance is: {instance}')
    print(f'Args: {args} and kwargs: {kwargs}')
    pass