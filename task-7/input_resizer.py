import os
from PIL import Image

# Settings
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
NEW_SIZE = (800, 800)  # Width x Height in pixels
OUTPUT_FORMAT = "PNG"  # Options: "PNG", "JPEG", etc.

def resize_and_convert_images():
    # Create output folder if not exists
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for filename in os.listdir(INPUT_FOLDER):
        file_path = os.path.join(INPUT_FOLDER, filename)

        try:
            with Image.open(file_path) as img:
                # Resize image
                img_resized = img.resize(NEW_SIZE)

                # Prepare output file path
                base_name = os.path.splitext(filename)[0]
                output_file = os.path.join(OUTPUT_FOLDER, f"{base_name}.{OUTPUT_FORMAT.lower()}")

                # Save in chosen format
                img_resized.save(output_file, OUTPUT_FORMAT)
                print(f"✅ Processed: {filename} -> {output_file}")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

if __name__ == "__main__":
    resize_and_convert_images()
