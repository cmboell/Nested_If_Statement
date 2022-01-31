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

# calculations to take off cash discount, percent discount, and to add tax
cash_off_subtotal = purchase_amount - cash_off_coupon
percent_off_subtotal = cash_off_subtotal - ((percent_coupon/constants.DIVIDE_FOR_PERCENT) * cash_off_subtotal)
tax_added_subtotal = percent_off_subtotal + (constants.TAX * percent_off_subtotal)




