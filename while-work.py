secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    # pw = input('what`s the secret word?')
    if count > max_attempt: break
    pw = input(f'{count}: what`s the secret word?')
    count += 1
