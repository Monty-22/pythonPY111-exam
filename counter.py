def counter(bytes_, players):
    if len(players) == 1:
        print(f"победитель - {players[0]}")
        return players
    i = 0
    len_players = len(players)
    print(f" Len => {len_players}")
    for word in bytes_:
        if i > len_players - 1:
            i = 0
        print(f"{word} => {players[i]}")
        i += 1
    players_short = players[i:] + players[:i]
    players_short.pop(0)
    counter(bytes_, players_short)
    return players


if __name__ == '__main__':
    count = ["eny", "beny", "riky", "paky"]
    name = list(range(7))
    print(counter(count, name))

    import hashlib
