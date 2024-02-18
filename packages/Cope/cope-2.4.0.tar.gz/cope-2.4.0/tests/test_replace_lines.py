from Cope import *

def test_comment():
    # Don't test this except for manually
    return
    # line 4
    replace_line('teeeeeeeeeeeeeeest')
    # line 6

    # comment('commeeennnttttt')
    comment('commeeennnttttt')

    # comment('')
    comment('')

    # comment(' ')
    comment(' ')

    # comment('comemnt', char='~')
    comment('comemnt', char='~')

    # comment('comment', start=' ')
    comment('comment', start=' ')

    # comment('comment', start='!', end='!')
    comment('comment', start='!', end='!')

    # comment('comment', line_limit=60)
    comment('comment', line_limit=60)

    # comment('commant', char='')
    comment('commant', char='')

    # comment('commant', char='-~')
    comment('commant', char='-~')

    # comment('commant', start='$-$')
    comment('commant', start='$-$')

    # comment('commant', end='$-$')
    comment('commant', end='$-$')

    # comment()
    comment()

    # comment(char='~')
    comment(char='~')

    # comment(lineLimit=30)
    comment(lineLimit=30)

    # comment('Seperator!')
    comment('Seperator!')

    # comment('Seperator!', '~')
    comment('Seperator!', '~')

    # comment('Seperator!', '~', '{')
    comment('Seperator!', '~', '{')

    # comment('Seperator!', '~', '{', 50)
    comment('Seperator!', '~', '{', 50)

def test_replace_line():
    return
    replaceLine("\t\t# This Line has been replaced! 1", -1)
    replaceLine("\t\t# This Line has been replaced! 2")
    replaceLine("# This Line has been replaced! 3")

    # replaceLine("\t\t# This Line has been replaced! 1", -1)
    # replaceLine("\t\t# This Line has been replaced! 2")
    # replaceLine("# This Line has been replaced! 3")

# test_comment()
