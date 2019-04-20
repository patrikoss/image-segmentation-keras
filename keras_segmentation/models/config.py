
IMAGE_ORDERING = 'channels_first'
if IMAGE_ORDERING == 'channels_first':
    axis=1
elif IMAGE_ORDERING == 'channels_last':
    axis=-1

INPUT_CHANNEL = 1