def iteams_and_units():

    items = input("Enter you'r items List Here : ")
    units = input("Enter you'r units List Here : ")
    units_val = units.split(',')

    items_cost_dict = {'A':50,'B':30,'C':10}
    discount_items_dict = {'A':3,'B':2}
    discount_items_value = {'A':43.33333,'B':22.5}

    for cnt,i in enumerate(items.split(',')):
        price = items_cost_dict[i]
        discounted_price = 0
        count = int(units_val[cnt])
        if (i in discount_items_dict.keys()):
            if(int(units_val[cnt]) >= discount_items_dict[i]):
                count1 = int(units_val[cnt]) // discount_items_dict[i]
                discounted_price = discount_items_value[i]*count1*discount_items_dict[i]
                count = count-(discount_items_dict[i]*count1)
        value = round((price * count) + discounted_price)
        print(value)

if __name__ == '__main__':
    iteams_and_units()