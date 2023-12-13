def get_key(hand):
    card_order = 'AKQJT98765432'
    key1 = sorted(-hand.count(card) for card in set(hand))
    key2 = [card_order.index(card) for card in hand]
    return (key1, key2)

def get_key2(hand):
    card_order = 'AKQT98765432J'
    num_jokers = hand.count('J')
    if num_jokers == 5:
        return ([-5], [len(card_order)-1]*5)
    key1 = sorted(-hand.count(card) for card in set(hand)-{'J'})
    key1[0] -= num_jokers
    key2 = [card_order.index(card) for card in hand]
    return (key1, key2)

def solve(f):
    bids = {}
    for line in open(f).read().splitlines():
        hand, bid = line.split(' ')
        bids[hand] = int(bid)
    
    s = 0
    for i, hand in enumerate(sorted(bids, key=get_key)):
        s += (len(bids)-i) * bids[hand]
    return s

def solve2(f):
    bids = {}
    for line in open(f).read().splitlines():
        hand, bid = line.split(' ')
        bids[hand] = int(bid)
    
    s = 0
    for i, hand in enumerate(sorted(bids, key=get_key2)):
        s += (len(bids)-i) * bids[hand]
    return s
    

if __name__ == '__main__':
    # print(solve('07_test.txt'))
    print(solve('07.txt'))
    # print(solve2('07_test.txt'))
    print(solve2('07.txt'))