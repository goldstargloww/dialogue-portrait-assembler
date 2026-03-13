from PIL import Image
import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--base", type=str, help="path to a single base image to use, eg. \"./character/bases/default.png\"", required=False)
parser.add_argument("-B", "--bases", type=str, help="path to a directory of bases to use, eg. \"./character/bases\"", required=False)
parser.add_argument("-o", "--overlay", type=str, help="single overlay; TBA, not implemented", required=False)
parser.add_argument("-O", "--overlays", type=str, help="path to a directory of overlays to use, eg. \"./character/overlays\"", required=False)
parser.add_argument("-f", "--folder", type=str, help="the folder to output to. defaults to \"./generated\"", required=False)
parser.add_argument("-t", "--template", type=str, help="naming template for files. defaults to \"{base}_{overlay}.png\". you can use / for nesting of directories. also you need to write the .png (can't do other file types sorgy)", required=False)
args = parser.parse_args()

def overlayificate(base, overlay):
    out = base
    out.paste(overlay, (0,0), mask=overlay)
    return out

def one_base_multiple_overlays(base_image_path: str, overlay_paths: list[str]) -> list:
    out_list = []
    for overlay_path, overlay_file in overlay_paths:
        new_image = overlayificate(Image.open(base_image_path), Image.open(overlay_path))
        out_list.append((new_image, overlay_file, base_image_path))
    return out_list

def save_one_base_multiple_overlays(base_image_path, overlay_images, output_folder="generated", name_template="{base}_{overlay}.png"):
    if "/" in name_template:
        name_template = "/" + name_template
        filename_template = name_template.split("/")[-1]
        output_folder += name_template.removesuffix(f"/{filename_template}")

    for image, image_name, base_path in one_base_multiple_overlays(base_image_path, overlay_images):
        base_path = base_path.split("/")[-1].removesuffix(".png")
        image_name = image_name.removesuffix(".png")

        format_values = {
            "base": str(base_path),
            "overlay": str(image_name)
        }

        output_folder = output_folder.format(**format_values)

        new_filepath = "./" + output_folder + "/" + filename_template.format(**format_values)
        os.makedirs(f"./{output_folder}", exist_ok=True)
        image.save(new_filepath)


# PARSING!!!!!!

if (args.base or args.bases) and (args.overlay or args.overlays):
    if (args.base and args.overlays):
        overlay_images = [(f"{args.overlays}/{file}", file) for file in os.listdir(args.overlays) if file.endswith("png")]

        # there is definitely a better way to do this but i Don't Care right now
        if args.folder and args.template:
            save_one_base_multiple_overlays(args.base, overlay_images, output_folder=args.folder, name_template=args.template)
        elif args.folder:
            save_one_base_multiple_overlays(args.base, overlay_images, output_folder=args.folder)
        elif args.template:
            save_one_base_multiple_overlays(args.base, overlay_images, name_template=args.template)
        else:
            try:
                save_one_base_multiple_overlays(args.base, overlay_images)
            except Exception as e:
                print(e)
                print("how'd you do that. what")

    elif (args.bases and args.overlays):
        bases = [f"{args.bases}/{file}" for file in os.listdir(args.bases) if file.endswith("png")]
        for base in bases:
            overlay_images = [(f"{args.overlays}/{file}", file) for file in os.listdir(args.overlays) if file.endswith("png")]

            if args.folder and args.template:
                save_one_base_multiple_overlays(base, overlay_images, output_folder=args.folder, name_template=args.template)
            elif args.folder:
                save_one_base_multiple_overlays(base, overlay_images, output_folder=args.folder)
            elif args.template:
                save_one_base_multiple_overlays(base, overlay_images, name_template=args.template)
            else:
                try:
                    save_one_base_multiple_overlays(base, overlay_images)
                except Exception as e:
                    print(e)
                    print("how'd you do that. what")
    else:
        print("sorry i couldn't be bothered to do that yet. gotta use multiple overlays and one base")
else:
    print("...you didn't give me anything. use -h for help")