def recommend_size(shoulder, waist):

    if shoulder < 38:
        return "XS"

    elif 38 <= shoulder < 42:
        return "S"

    elif 42 <= shoulder < 46:
        return "M"

    elif 46 <= shoulder < 47:
        return "L"

    else:
        return "XL"