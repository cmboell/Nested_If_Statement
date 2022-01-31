"""
Assignment name: Nested if statement Assignment
Program: if_elif.py
Author: Colby Boell
Last date modified: 01/31/2022

SuperAwesomeCouponDealAndStuff.com offers two types of discounts: cash-off coupons and percent discount coupons.
Add tax after coupons. Cash coupons must be applied before the percent coupons. 6% is the tax rate.
The purpose of this project is to prompt user for the amount of the purchase, the cash coupon, the percent
coupon. Then calculate and return the total order item.
up to $10 dollars, shipping is $5.95, $10 and up to $30 dollars, shipping is $7.95, $30 and up to $50 dollars, shipping is $11.95
Shipping is free for $50 and over. Order of calculation: cash off coupons ($5 or $10),%(5%,15%, or 20%),tax, and then shipping.
"""
# file for constant variables
DIVIDE_FOR_PERCENT = 100
TAX = .06

SHIP_TIER_1 = 10
SHIP_TIER_2 = 30
SHIP_TIER_3 = 50

