def get_options_ratio(option, total):
    ratio = option / total
    return ratio

def get_faculty_rating(ratio):
    rating = ""
    if (ratio >= 0.9 and ratio <=1.0):
        rating = "Excellent"
    elif (ratio >= 0.8 and ratio < 0.9):
        rating = "Very Good"
    elif (ratio >= 0.7 and ratio < 0.8):
        rating = "Good"
    elif (ratio >= 0.6 and ratio < 0.7):
        rating = "Needs Improvement"
    elif (ratio >= 0 and ratio < 0.6):
        rating = "Unacceptable"
        
    else:
        rating = "Invalid Rating"
        
    return rating

def get_bonus_pay(sales):

    sales = ""

    if (sales >= 0 and sales <= 499):
        return "5%"
    
    

