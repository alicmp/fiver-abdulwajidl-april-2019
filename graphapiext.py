from facebook import *

class GraphAPIExt(GraphAPI):

    def put_video(self, video=None, video_name=None, album_path="me/videos", **kwargs):
        """
        Upload a video using multipart/form-data.
        video - A file object representing the video to be uploaded.
        album_path - A path representing where the video should be uploaded.
        """

        post_args = {}

        if video and video_name:
            post_args = {
                "source":  (video_name, video)
            }

        post_args.update(kwargs) 

        return self.request(
            "{0}/{1}".format(self.version, album_path),
            post_args=post_args,
            method="POST",
        )
