#!/usr/bin/env python

import click

def greedy_coin(amount, coins):
    # Sort coins in descending order to prioritize larger denominations.
    coins.sort(reverse=True)
    remaining_amount = 0
    # Initialize variables
    num_coins = 0
    coin_counts = {coin: 0 for coin in coins}  # Dictionary to track coin usage

    # Iterate through coin denominations
    for coin in coins:
        # While the remaining amount is greater than or equal to the current coin denomination
        while remaining_amount >= coin:
        # Use the current coin denomination and deduct it from the remaining amount
            remaining_amount -= coin
            num_coins += 1
            coin_counts[coin] += 1  # Increment the count for the used coin

    return num_coins, coin_counts

@click.command()
@click.argument('amount', type=int)
@click.argument('coins', type=list)
def main(amount, coins):
    """
    Calculates the minimum number of coins needed for making change using a greedy algorithm and prints the types and number of coins used.
    """
    print(coins)
    min_coins, coin_counts = greedy_coin(amount, coins.copy())  # Use a copy to avoid modifying the original list

    print(f"Minimum number of coins for ${amount} change:", min_coins)
    print("Coins used:")
    for coin, count in coin_counts.items():
        if count > 0:  # Print only coins that were actually used
            print(f"{count} x {coin}")

if __name__ == '__main__':
  main()
