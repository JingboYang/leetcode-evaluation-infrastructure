def fullJustify(self, words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    
    if len(words) == 0:
        return []

    start_index = 0
    word_index = 1
    cur_line_width = len(words[0])

    results = []
    while word_index < len(words):

        need_line_width = cur_line_width + 1 + len(words[word_index])
        print('Word {}, Cur line width {}. Need width {}'.format(words[word_index], cur_line_width, need_line_width))

        if need_line_width > maxWidth:

            diff = maxWidth - cur_line_width
            extra_spaces = diff // (word_index - start_index - 1)
            if word_index - start_index - 1 == 0:
                extra_extra = 0
            else:
                extra_extra = diff % (word_index - start_index - 1)

            print((start_index, word_index))
            print(cur_line_width)
            print((extra_spaces, extra_extra))

            out_string = ''
            for i in range(start_index, word_index - 1):
                out_string += words[i] + ' ' + ' ' * extra_spaces
                if extra_extra > 0:
                    out_string += ' '
                    extra_extra -= 1
            out_string += words[word_index - 1]

            print(out_string)
            print(len(out_string))
            results.append(out_string)

            start_index = word_index
            word_index += 1

            if word_index < len(words):
                cur_line_width = len(words[start_index])

        else:
            #print('Word -{}- okay'.format(words[word_index]))
            word_index += 1
            cur_line_width = need_line_width


    diff = maxWidth - cur_line_width
    extra_spaces = diff // (word_index - start_index)
    if word_index - start_index - 1 == 0:
        extra_extra = 0
    else:
        extra_extra = diff % (word_index - start_index - 1)

    out_string = ''
    for i in range(start_index, word_index - 1):
        out_string += words[i] + ' ' + ' ' * extra_spaces
        if extra_extra > 0:
            out_string += ' '
            extra_extra -= 1
    out_string += words[word_index - 1]
    out_string += ' ' * (maxWidth - len(out_string))

    print(out_string)
    results.append(out_string)

    return results


signature = 'fullJustify(self, words, maxWidth):'
input_string = """["This", "is", "an", "example", "of", "text", "justification."]
16
"""        