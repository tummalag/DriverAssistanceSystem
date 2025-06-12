from camera import Camera

def main():
    with Camera() as cam:
        cam.stream()

if __name__ == "__main__":
    main()
