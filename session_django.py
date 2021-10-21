# Get a session value by its key (e.g. 'name'), raising a KeyError if the key is not present
my_car = request.session['name']

# Get a session value, setting a default if it is not present ('tom')
my_car = request.session.get('my_car', 'mini')

# print all variable in session
for key, value in request.session.items():
    print('{} => {}'.format(key, value))

# Set a session value
request.session['name'] = 'tom'

# Delete a session value
del request.session['name']

# check data in session
if 'admin_id' in request.session:
    print('yes')
