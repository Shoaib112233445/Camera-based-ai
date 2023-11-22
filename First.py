
class Camera:
    def __init__(self, brand, resolution):
        self._brand = brand
        self._resolution = resolution

    def capture_image(self):
        raise NotImplementedError("Subclasses must implement this method")

    def record_video(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        return f"{self._brand} Camera with Resolution: {self._resolution}"


class AICamera(Camera):
    def process_image(self):
        print("Applying AI image processing")

    def analyze_scene(self):
        print("Analyzing the scene using AI")

    def capture_image(self):
        print("AI-based image capture")


class VideoCamera(Camera):
    def record_video(self):
        print("Recording video")

    def stabilize_video(self):
        print("Applying video stabilization")


# Example usage:

ai_camera = AICamera(brand="AI-Cam", resolution="1080p")
video_camera = VideoCamera(brand="Vid-Cam", resolution="4K")

print(ai_camera)
ai_camera.capture_image()
ai_camera.process_image()
ai_camera.analyze_scene()

print("\n" + "=" * 30 + "\n")

print(video_camera)
video_camera.record_video()
video_camera.stabilize_video()