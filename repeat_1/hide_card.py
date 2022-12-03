'''print output for func hide_card(card)
    should be ************3456'''
card_1= '1234567890123456'
card_2 = '3456 9012 5678 1234'
card_3 = '905 678123 45612 56'

def hide_card(x):
    x_nosp = x.replace(' ', '')
    b = '************'
    a = x_nosp[-4:]
    c = b+a
    return c

print(hide_card(card_1))
print(hide_card(card_2))
print(hide_card(card_3))