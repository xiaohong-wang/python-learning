
import random
import string



def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

def unique_order_no_generate(instance):
    order_no = random_string_generator()
    klass = instance.__class__
    qs = klass.objects.filter(order_no=order_no)
    if qs.count() >= 1:
        return unique_order_no_generate(instance)
    return  order_no