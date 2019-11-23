def str123():  # я теперь буду извращаться, чтобы такое точно ни с кем не совпало
    zero, one, two = map(int, input().split())

    def sequence_maker(a=0, b=0, c=0, sequence=" "):
        print(sequence[::-1].strip()) if sum([a, b, c]) == sum([zero, one, two]) else None
        sequence_maker(a + 1, b, c, "0" + sequence) if a < zero else None
        sequence_maker(a, b + 1, c, "1" + sequence) if b < one else None
        sequence_maker(a, b, c + 1, "2" + sequence) if c < two else None

    sequence_maker()


str123()
