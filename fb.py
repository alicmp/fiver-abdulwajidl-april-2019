import os
import facebook

token = 'EAAIghCwTMBwBAPSxGZAXeoRAt7YGPuSDggfYB9djqZBagHM6aWRn7HKIcjA3I1XOdeuyCgj1XvvMgPUxhvvRKCphZCK0uhbl4ZBsDQytwJajC7kVZCD3oVYxGZCnZBSMuTVKo0Vnk113W2QDpmR1F8yY478dkZCsqGyJs3KnVkClAmZCQ78E6Y5QxvryVjAPHsqMoZC7xjX57FSQZDZD'

fb = facebook.GraphAPI(
    access_token=token
)

# fb.put_object(parent_object='me', connection_name='feed',
#     message='Hello, world')

fb.put_photo(image=open('media/photo_2019-04-21_18-29-14.jpg', 'rb'),
    message='Look at this cool photo!')