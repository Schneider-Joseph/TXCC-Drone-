import argparse
import os
import subprocess
import time


def take_photo(filename: str) -> bool:
    print(f"Taking photo and saving as {filename}...")
    command = (
        f'fswebcam -S 75 -r 1280x720 --no-banner '
        f'--set "exposure_auto=1" '
        f'--set "exposure_absolute=80" '
        f'--set "gain=20" '
        f'--set "brightness=40" '
        f'"{filename}"'
    )

    try:
        subprocess.run(command, shell=True, check=True)
        print("Photo taken successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error taking photo: {e}")
    except FileNotFoundError:
        print("Error: fswebcam command not found.")

    return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Take n photos and save them as photo1, photo2, ..."
    )
    parser.add_argument("n", type=int, help="Number of photos to take")
    parser.add_argument(
        "--delay",
        type=float,
        default=0.1,
        help="Delay in seconds between photos (default: 0.1)",
    )
    args = parser.parse_args()

    if args.n <= 0:
        raise ValueError("n must be greater than 0")

    save_dir = "/home/tunxis001/pi/photoloop_file"
    os.makedirs(save_dir, exist_ok=True)
    print(f"[INFO] Saving images to: {save_dir}")

    for i in range(1, args.n + 1):
        filename = os.path.join(save_dir, f"photo{i}.jpg")
        take_photo(filename)
        if i < args.n:
            time.sleep(args.delay)

    print("[INFO] Finished taking photos.")


if __name__ == "__main__":
    main()
