def bmi(weight: float, height: float):
    '''This function helps you to find the BMI range
       params: `wight(in pounds)`
       params: `height (in inches)`
    It is using this formula `(weight by height sqaure)`
    '''
    res = 703 * weight / (height * height)
    return res


if __name__ == '__main__':
    bmi_value = bmi(150, 70)
    print("BMI Value is:",bmi_value)
