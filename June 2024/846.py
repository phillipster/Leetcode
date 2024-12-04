def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size != 0:
        return False
    deck = {}
    for card in hand:
        if card not in deck:
            deck[card] = 1
        else:
            deck[card] += 1
    for card in deck:
        if deck[card] > 0:
            for i in range(group_size):
                try:
                    deck[card + i] -= 1
                except:
                    return False
            deck[card] -= 1
    return True


print(is_n_straight_hand([2, 1], 2))
