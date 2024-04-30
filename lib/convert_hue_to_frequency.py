def convert_hue_to_frequency(hue, scale_frequencies):
    thresholds = [26, 52, 78, 104, 128, 154, 180]
    if hue <= thresholds[0]:
        note = scale_frequencies[0]
    elif thresholds[0] < hue <= thresholds[1]:
        note = scale_frequencies[1]
    elif thresholds[1] < hue <= thresholds[2]:
        note = scale_frequencies[2]
    elif thresholds[2] < hue <= thresholds[3]:
        note = scale_frequencies[3]
    elif thresholds[3] < hue <= thresholds[4]:
        note = scale_frequencies[4]
    elif thresholds[4] < hue <= thresholds[5]:
        note = scale_frequencies[5]
    elif thresholds[5] < hue <= thresholds[6]:
        note = scale_frequencies[6]
    else:
        note = scale_frequencies[0]

    return note
