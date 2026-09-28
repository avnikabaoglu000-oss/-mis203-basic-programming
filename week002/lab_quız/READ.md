# Week 2 Lab: Two-Item Purchase Quote

This project calculates the total cost of buying two different items.

## What the program does

The program asks for:

* Two item names
* Quantity for each item
* Unit price for each item
* Delivery fee
* Tax percentage

Then it calculates:

* Each item's total
* Subtotal
* Tax
* Delivery fee
* Final total

Tax is applied to the item subtotal before the delivery fee is added.

## Test

I tested the program with:

* Item 1: 2 × 50 TRY
* Item 2: 1 × 80 TRY
* Delivery fee: 20 TRY
* Tax: 10%

Expected calculation:

* Subtotal: 180.00 TRY
* Tax: 18.00 TRY
* Delivery: 20.00 TRY
* Final total: 218.00 TRY

The program produced:

`Final total: 218.00 TRY`

## Change after testing

After testing, I changed the money output to use two decimal places with `:.2f`.

For example:

`218` is displayed as `218.00 TRY`.

I also tested an invalid quantity by entering letters instead of a number and observed a `ValueError`.
