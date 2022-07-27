#value = {
    # name : value
    #name : value
# }
def add_value(dict, value, times = 1):# add_value multiple times
	for i,j in value.items():
		if i in dict:
			dict[i] += j*times
		else:
			dict[i] = j*times
	return dict

def remove_value(dict, value, times = 1):	
	for i,j in value.items():
		if i in dict:
			if dict[i] >= j * times:
				dict[i] -= j * times	
			else:
				raise Exception("Value '%s' is greater than dict" % (i[0]))
		else:
			raise Exception("value '%s' is not a valid value" % (i[0]))
	return dict

def total_count(dict):
    count = 0
    for i,j in dict.items():
        count = count + j
    return count

def greater(dict, value, times = 1):	
	for i,j in value.items():
		if i in dict:
			if dict[i] < j * times:
				return False
		else:
			return False
	return True
    