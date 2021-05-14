text = 'bread.vb'
import string

if set(text).difference(string.ascii_letters + string.digits):
    print('Special characters.')
else:
    print("NO special characters.")