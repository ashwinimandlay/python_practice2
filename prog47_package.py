# packages (directory or folder)
# collection of modules
# two ways :
# 1. new directory ->directory name -> new python file->
# __init__ (now it takes this as a package)
# 2. new package -> automatically creates init file
# in this program we created ecommerce package and now
# we import it to this file

# m1
import ecommerce.shipping
ecommerce.shipping.cal_shipping()

# m2
from ecommerce.shipping import cal_shipping, cal_tax
cal_tax()
cal_shipping()

# m3
from ecommerce import shipping
shipping.cal_shipping()
shipping.cal_tax()

