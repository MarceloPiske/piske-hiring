def format_json(array):
    #print(array)
    formated_aray = []
    for i in array.get("manufacturer"):
        new_dict = {}
        new_dict['manufacturer'] = array.get('manufacturer').get(i)
        new_dict['model'] = array.get('model').get(i)
        new_dict['color'] = array.get('color').get(i)
        new_dict['carrier_plan_type'] = array.get('carrier_plan_type').get(i)
        new_dict['quantity'] = array.get('quantity').get(i)
        new_dict['price'] = array.get('price').get(i)
        formated_aray.append(new_dict)
    
    print(formated_aray)
    return formated_aray