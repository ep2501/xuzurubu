"""
Xuzu module description
=======================
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed cursus purus ac tellus finibus efficitur. Pellentesque varius
cursus quam sollicitudin faucibus. Aliquam bibendum augue enim,
nec euismod arcu tincidunt at. Ut ligula purus, pretium in hendrerit
sit amet, consequat eu justo.

Fusce eu massa ac sapien consequat consectetur ac id ante.
Nullam et tortor sagittis, sodales est quis, suscipit orci.
Pellentesque pellentesque mauris lorem, nec scelerisque
sem euismod non. Phasellus elementum justo orci. Ut molestie, nunc
eu rhoncus egestas, arcu est dignissim nunc, placerat aliquet elit
augue fringilla enim.

Curabitur tincidunt quam non risus rutrum luctus vitae nec turpis.
Curabitur scelerisque purus ante, et vulputate tortor lacinia pretium.
Nam iaculis fermentum consectetur. In eu luctus ligula. Maecenas nec
lectus urna. Phasellus fringilla eget enim id fringilla. Ut accumsan
lobortis velit id eleifend.
"""


def line_cap(text, cap='#'):
    capped = cap + text + cap + '\n'
    return capped


def box_text(text, cap='#', line_char='-', width=79):
    # Check args
    w = width - 2  # two additional spaces req'd for comment chars
    assert len(text) <= (w - 2) # 4-spaces total for padding text

    # Format main text
    text_padded = text.center(w)
    text_capped = line_cap(text_padded)

    # Format lines
    line = line_char * (w)
    line_capped = line_cap(line)

    # Format text box
    text_box = line_capped + text_capped + line_capped
    return text_box
