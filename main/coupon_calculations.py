"""
Assignment name: Nested if statement Assignment
Program: if_elif.py
Author: Colby Boell
Last date modified: 01/31/2022

SuperAwesomeCouponDealAndStuff.com offers two types of discounts: cash-off coupons and percent discount coupons.
Add tax after coupons. Cash coupons must be applied before the percent coupons. 6% is the tax rate.
The purpose of this project is to prompt user for the amount of the purchase, the cash coupon, the percent
coupon. Then calculate and return the total order item.
up to $ 10 dollars, shipping is $5.95, $10 and up to $ 30 dollars, shipping is $7.95, $30 and up to $ 50 dollars, shipping is $11.95
Shipping is free for $50 and over. Order of calculation: cash off coupons ($5 or $10),%(10%,15%, or 20%),tax, and then shipping.
"""
# imports constants file
import constants
# prints out initial sentence for program
print("Thank you for using SuperAwesomeCouponDealAndStuff.com!! Let's get started!")

# prompts for user input for purchase amount (double), (int) cash off coupon, (percent discount coupon
purchase_amount = float(input('Enter the total amount of your purchase: '))
cash_off_coupon = int(input('Enter your cash off coupon amount (5 or 10): '))
percent_coupon = int(input('Enter your percent discount coupon (10, 15, or 20): '))

# nested if statement to make sure we are not giving free stuff
if purchase_amount <= 5:
    cash_off_coupon = 0
    print('Your order must be more than $5 dollars to use cash off coupon')
elif purchase_amount > 5:
    if purchase_amount <= 10:
        cash_off_coupon = 5
        print('Your order was less than $10, we have given you $5 off')

# calculations to take off cash discount, percent discount, and to add tax
cash_off_subtotal = purchase_amount - cash_off_coupon
percent_off_subtotal = cash_off_subtotal - ((percent_coupon/constants.DIVIDE_FOR_PERCENT) * cash_off_subtotal)
tax_added_subtotal = percent_off_subtotal + (constants.TAX * percent_off_subtotal)

# nested if statement for shipping costs
if tax_added_subtotal <= constants.SHIP_TIER_1:
    shipping = 5.95
    if constants.SHIP_TIER_1 < tax_added_subtotal <= constants.SHIP_TIER_2:
        shipping = 7.95
        if constants.SHIP_TIER_2 < tax_added_subtotal <= constants.SHIP_TIER_3:
            shipping = 11.95
else:
    shipping = 0

# variable to calculate final total
final_total = tax_added_subtotal + shipping

# prints out customer order details all the way until final total
print(f'Original Purchase: ${purchase_amount: 5.2f}\nAfter Cash Discount: ${cash_off_subtotal: 5.2f}\nAfter Percent Discount:'
      f' ${percent_off_subtotal: 5.2f}\nWith Taxes Added: {tax_added_subtotal: 5.2f}\nYour'
      f' final total with shipping is: ${final_total: 5.2f}')

"""
Tests: 
Input: 15.99   output:  Original Purchase: $ 15.99             
       5       After Cash Discount: $ 10.99
       20      After Percent Discount: $ 8.79
               With Taxes Added:  9.32
               Your final total with shipping is: $ 15.27

Input: 5       Your order must be more than $5 dollars to use cash off coupon
       10      Original Purchase: $ 5.00
       15      After Cash Discount: $ 5.00
               After Percent Discount: $ 4.25
               With Taxes Added:  4.50
               Your final total with shipping is: $ 10.46
"""
