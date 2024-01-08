def birthdayCakeCandles(candles):
    heighest = max(candles)
    count = 0

    for candle in candles:
        if candle == heighest:
            count += 1

    return count


print(birthdayCakeCandles([3, 2, 1, 3]))
